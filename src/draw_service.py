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

    def __init__(self, service_url="http://localhost:3000"):
        self._service_url = service_url

    def get(self, endpoint):
        url = "{url}/{api}/{endpoint}".format(url=self._service_url, api=DrawServiceInterface.API_PREFIX, endpoint=endpoint)
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

    def read_all_drawings(self):
        try:
            code, data = self.get("all-drawings")
            if code != 200:
                return False, "Návratový kód {code}".format(code=code)
            if "projects" in data and "buildings" in data and "floors" in data and "drawings" in data:
                return True, data, "Success"
            return False, None, "Neplatná data"
        except Exception as e:
            return False, None, repr(e)

