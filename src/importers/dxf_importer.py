#
#  (C) Copyright 2017  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from dxf_reader_state import *
from dxf_entity_type import *


def dxf_entry(fin):
    """Generate pair dxf_code + dxf_data for each iteration."""
    while True:
        line1 = fin.readline()
        line2 = fin.readline()
        if not line1 or not line2:
            break
        code = int(line1.strip())
        data = line2.strip()
        yield code, data


def import_dxf(filename):
    state = DxfReaderState.BEGINNING
    entity_type = DxfEntityType.UNKNOWN
    codeStr = None
    dataStr = None
    blockName = None

    with open(filename) as fin:
        lines = 0
        for code, data in dxf_entry(fin):
            if state == DxfReaderState.BEGINNING:
                if code == 0:
                    if data == "SECTION":
                        state = DxfReaderState.BEGINNING_SECTION
                    elif data == "EOF":
                        state = DxfReaderState.EOF
                        print("eof")
                elif code == 999:
                    print(data)
                else:
                    raise Error("unknown code {c} for state BEGINNING".format(c=code))
            lines += 1
    print(lines)


if __name__ == "__main__":
    import_dxf("Branna_3np.dxf")
