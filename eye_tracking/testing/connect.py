"""
Based on docs from:
    https://developer.tobiipro.com/python/python-getting-started.html
    https://developer.tobiipro.com/commonconcepts.html
    https://developer.tobiipro.com/commonconcepts/calibration.html
    https://developer.tobiipro.com/python/python-step-by-step-guide.html
    https://developer.tobiipro.com/python/python-sdk-reference-guide.html
"""

import os.path as osp, os
import sys
cwd = osp.dirname(osp.realpath(__file__))
sys.path.append(osp.dirname(cwd))
import utils
import re

try:
    from icecream import ic
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
    
import tobii_research as tr

DEBUG = 0
if DEBUG: ic.disable()

ignore_pattern = re.compile(r'__.+__')

def show_attr(obj):
    list(map(print, filter(lambda attr: not re.fullmatch(ignore_pattern, attr), dir(obj))))


def main():
    with utils.Timer() as t:
        available = tr.find_all_eyetrackers()
    ic(t.elapsed)
    
    try:
        eyetracker = available[0]
    except Exception as e:
        raise ConnectionError()

    addr = ic(eyetracker.address)
    model = (eyetracker.model)
    device_name = ic(eyetracker.device_name)
    firmware_version  = ic(eyetracker.firmware_version)
    runtime_version = ic(eyetracker.runtime_version)
    serial_number = ic(eyetracker.serial_number)
    
    
    


if __name__ == '__main__':
    main()