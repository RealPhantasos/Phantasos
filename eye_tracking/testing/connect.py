"""
Based on docs from:
    https://developer.tobiipro.com/python/python-getting-started.html
    https://developer.tobiipro.com/commonconcepts.html
    https://developer.tobiipro.com/commonconcepts/calibration.html
    https://developer.tobiipro.com/python/python-step-by-step-guide.html
    https://developer.tobiipro.com/python/python-sdk-reference-guide.html
"""

import os.path as osp
import sys
sys.path.append(osp.join(osp.realpath(__file__), *(2*[osp.pardir])))  # add parent dir to include path
from utils import Timer
import re
from collections import deque

try:
    from icecream import ic
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
    
import tobii_research as tr

DEBUG = 0
if DEBUG: ic.disable()

ignore_pattern = re.compile(r'__?.+(__)?')

def show_attrs(obj):
    """Prints all available attrs of obj"""
    deque(map(print, filter(lambda attr: not re.fullmatch(ignore_pattern, attr), dir(obj))), maxlen=0)


def main():
    with Timer() as t:
        devices = tr.find_all_eyetrackers()
    
    try:
        eyetracker = devices[0]
    except Exception as e:
        raise ConnectionError()
    
    ic(t.elapsed)
    addr = ic(eyetracker.address)
    model = (eyetracker.model)
    device_name = ic(eyetracker.device_name)
    firmware_version  = ic(eyetracker.firmware_version)
    runtime_version = ic(eyetracker.runtime_version)
    serial_number = ic(eyetracker.serial_number)
    

if __name__ == '__main__':
    main()