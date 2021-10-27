"""
Based on docs from:
    Quick Start: https://developer.tobiipro.com/python/python-step-by-step-guide.html
    Common Concepts: https://developer.tobiipro.com/commonconcepts.html
    Custom Calibartion: https://developer.tobiipro.com/commonconcepts/calibration.html
    SDK Reference Guide: https://developer.tobiipro.com/python/python-sdk-reference-guide.html
"""

import time

import os.path as osp
import sys; sys.path.append(osp.join(osp.realpath(__file__), *(2*[osp.pardir])))  # add parent dir to include path
from utils import Timer, show_attrs

try:
    from icecream import ic
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
    
import tobii_research as tr

DEBUG = 1
if not DEBUG: ic.disable()

def gaze_cb(gaze_data):
    print(f'Left: {gaze_data['left_gaze_point_on_display_area']}')
    print(f'Right: {gaze_data['right_gaze_point_on_display_area'])}')

def main():
    with Timer() as t:
        devices = tr.find_all_eyetrackers()
    
    try:
        eyetracker = devices[0]
    except Exception as e:
        raise ConnectionError('Couldn\'t find device!')
    
    ic(t.elapsed)
    addr = ic(eyetracker.address)
    model = ic(eyetracker.model)
    device_name = ic(eyetracker.device_name)
    firmware_version  = ic(eyetracker.firmware_version)
    runtime_version = ic(eyetracker.runtime_version)
    serial_number = ic(eyetracker.serial_number)
    
    eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_cb, as_dictionary=True)
    time.sleep(5)
    eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_cb)
    

if __name__ == '__main__':
    main()
