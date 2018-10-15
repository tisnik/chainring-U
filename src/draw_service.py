#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import requests

from exporters.json_exporter import *


class DrawServiceInterface:
    API_PREFIX = "api/v1"

    @staticmethod
    def get_url(address, port):
        return "http://{address}:{port}".format(address=address, port=port)

    def __init__(self, service_url="http://localhost:3000"):
        self._service_url = service_url

    def get(self, endpoint):
        url = "{url}/{api}/{endpoint}".format(url=self._service_url,
                                              api=DrawServiceInterface.API_PREFIX,
                                              endpoint=endpoint)
        response = requests.get(url, timeout=10)
        return response.status_code, response.json()

    def check_liveness(self):
        try:
            code, data = self.get("liveness")
            if code != 200:
                return False, "Návratový kód {code}".format(code=code)
            if "status" in data and data["status"] == "ok":
                return True, None
            return False, "Neplatná data vrácená serverem"
        except Exception as e:
            return False, repr(e)

    def read_version(self):
        try:
            code, data = self.get("info")
            if code != 200:
                return False, "Návratový kód {code}".format(code=code)
            if "service-version" in data:
                return True, data["service-version"], "Success"
            return False, None, "Neplatná data vrácená serverem"
        except Exception as e:
            return False, None, repr(e)

    def read_aoid(self, url, selector, error_message):
        try:
            code, data = self.get(url)
            if code != 200:
                return None, "Návratový kód {code}".format(code=code)
            if "status" in data and data["status"] == "ok":
                if selector in data:
                    return data[selector], "Ok"
                else:
                    return None, error_message
            return None, "Neplatná data vrácená serverem"
        except Exception as e:
            return None, repr(e)

    def read_areals(self, valid_from):
        url = "areals?valid-from={date}".format(date=valid_from)
        return self.read_aoid(url, "areals", "Seznam areálů je prázdný")

    def read_buildings(self, valid_from, aoid):
        url = "buildings?valid-from={date}&areal-id={aoid}".format(date=valid_from, aoid=aoid)
        return self.read_aoid(url, "buildings", "Seznam budov je prázdný")

    def read_floors(self, valid_from, aoid):
        url = "floors?valid-from={date}&building-id={aoid}".format(date=valid_from, aoid=aoid)
        return self.read_aoid(url, "floors", "Seznam podlaží je prázdný")

    def read_rooms(self, valid_from, aoid):
        url = "rooms?valid-from={date}&floor-id={aoid}".format(date=valid_from, aoid=aoid)
        return self.read_aoid(url, "rooms", "Seznam místností je prázdný")

    def check_input_data(self, data):
        return "projects" in data and \
               "buildings" in data and \
               "floors" in data and \
               "drawings" in data

    def send_drawing(self, drawing):
        endpoint = "drawing-data?drawing={id}&format=json".format(id=drawing.drawing_id)
        url = "{url}/{api}/{endpoint}".format(url=self._service_url,
                                              api=DrawServiceInterface.API_PREFIX,
                                              endpoint=endpoint)
        json_exporter = JSONExporter("output.json", drawing)
        payload = json_exporter.as_string()
        try:
            response = requests.post(url, data=payload, timeout=30)
            code, data = self.get("info")
            print(code, data)
            if code != 200:
                return False, "Návratový kód {code}".format(code=code)
            else:
                message = "Výkres byl uložen pod ID {id} ({b} bajtů)".format(id=drawing.drawing_id, b=len(payload))
                return True, message
        except Exception as e:
            return False, e

    def read_all_drawings(self):
        try:
            code, data = self.get("all-drawings")
            if code != 200:
                return False, "Návratový kód {code}".format(code=code)
            if self.check_input_data(data):
                return True, data, "Success"
            return False, None, "Neplatná data"
        except Exception as e:
            return False, None, repr(e)
