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

import configparser


class Configuration:
    CONFIG_FILE_NAME = 'config.ini'

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(Configuration.CONFIG_FILE_NAME)

    @property
    def window_width(self):
        v = self.config.getint('ui', 'window_width')
        return v

    @property
    def window_height(self):
        return self.config.getint('ui', 'window_height')

    @property
    def server_address(self):
        return self.config.get('service', 'url')

    @property
    def server_port(self):
        return self.config.getint('service', 'port')

    def write(self):
        with open('config2.ini', 'w') as fout:
            self.config.write(fout)
