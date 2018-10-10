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
        response = requests.get(url)
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

    def read_areals(self, valid_from):
        try:
            code, data = self.get("areals?valid-from=" + valid_from)
            if code != 200:
                return None, "Návratový kód {code}".format(code=code)
            print(data)
            if "status" in data and data["status"] == "ok":
                if "areals" in data:
                    return data["areals"], "Ok"
                else:
                    return None, "Seznam areálů je prázdný"
            return None, "Neplatná data vrácená serverem"
        except Exception as e:
            return None, repr(e)

    def read_buildings(self, valid_from, aoid):
        try:
            code, data = self.get("buildings?valid-from=" + valid_from + "&areal-id=" + aoid)
            if code != 200:
                return None, "Návratový kód {code}".format(code=code)
            print(data)
            if "status" in data and data["status"] == "ok":
                if "buildings" in data:
                    return data["buildings"], "Ok"
                else:
                    return None, "Seznam budov je prázdný"
            return None, "Neplatná data vrácená serverem"
        except Exception as e:
            return None, repr(e)

    def check_input_data(self, data):
        return "projects" in data and \
               "buildings" in data and \
               "floors" in data and \
               "drawings" in data

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
