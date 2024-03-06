"""Interface to web service that provide list of rooms and drawing storage."""

#
#  (C) Copyright 2017, 2018, 2019  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from getpass import getuser
from platform import node
from time import asctime

import requests
from exporters.json_exporter import *


class DrawServiceInterface:
    """Interface to web service that provide list of rooms and drawing storage."""

    API_PREFIX = "api/v1"

    @staticmethod
    def get_url(address, port):
        """Get URL prefix to the service."""
        return "http://{address}:{port}".format(address=address, port=port)

    def __init__(self, service_url="http://localhost:3000", key=""):
        """Initialize the interface."""
        self._service_url = service_url
        self._user_key = key

    def get(self, endpoint):
        """Get full URL to selected endpoint."""
        url = "{url}/{api}/{endpoint}".format(url=self._service_url,
                                              api=DrawServiceInterface.API_PREFIX,
                                              endpoint=endpoint)
        response = requests.get(url, timeout=10)
        return response.status_code, response.json()

    def check_liveness(self):
        """Check service liveness."""
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
        """Read service API version."""
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
        """Read AOID from the web service."""
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

    def read_buildings(self, valid_from):
        """Read list of buildings from the web service."""
        url = "buildings?valid-from={date}".format(date=valid_from)
        return self.read_aoid(url, "buildings", "Seznam budov je prázdný")

    def read_floors(self, valid_from, aoid):
        """Read list of floors from the web service."""
        url = "floors?valid-from={date}&building-id={aoid}".format(date=valid_from, aoid=aoid)
        return self.read_aoid(url, "floors", "Seznam podlaží je prázdný")

    def read_rooms(self, valid_from, aoid):
        """Read list of rooms from the web service."""
        url = "rooms?valid-from={date}&floor-id={aoid}".format(date=valid_from, aoid=aoid)
        return self.read_aoid(url, "rooms", "Seznam místností je prázdný")

    def check_input_data(self, data):
        """Check the basic structure of data read from web service."""
        return "projects" in data and \
               "buildings" in data and \
               "floors" in data and \
               "drawings" in data

    def send_drawing(self, drawing):
        """Send drawing onto the web service."""
        endpoint = "drawing-data?drawing={id}&format=json".format(id=drawing.drawing_id)
        url = "{url}/{api}/{endpoint}&key={key}".format(url=self._service_url,
                                                        api=DrawServiceInterface.API_PREFIX,
                                                        endpoint=endpoint,
                                                        key=self._user_key)
        hostname = node()
        username = getuser()
        created = asctime()

        json_exporter = JSONExporter("output.json", drawing, hostname, username, created)
        payload = json_exporter.as_string()
        try:
            response = requests.post(url, data=payload, timeout=30)
            code = response.status_code
            if code != 200:
                return False, "Návratový kód {code}".format(code=code)
            else:
                message = "Výkres byl uložen pod ID {id} ({b} bajtů)".format(
                    id=drawing.drawing_id, b=len(payload))
                return True, message
        except Exception as e:
            return False, str(e)

    def read_all_drawings(self):
        """Read list of all drawings from the web service."""
        try:
            code, data = self.get("all-drawings")
            if code != 200:
                return False, "Návratový kód {code}".format(code=code)
            if self.check_input_data(data):
                return True, data, "Success"
            return False, None, "Neplatná data"
        except Exception as e:
            return False, None, repr(e)
