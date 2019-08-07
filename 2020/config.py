#
# vision parameter groups (aka configs)
#
# given the name of a config (eg "greenled") access via:
#
#  import config
#  cfg = getattr(config, "greenled")
#
#  (see bottom for details on parameters)
import numpy as np
import copy

# ------ Base -------

_base = {
    "picam": {
        "resolution": (640, 480), # (320,240) has less range
        "framerate": 60,
        "sensormode": 7,    # auto-calc based on res and framerate
                            # Fixes auto wb 'hidden' settings
    },
    "algo": {
        # Assuming retro-reflective tape
        "hsvRange0": np.array([30,150,170]),
        "hsvRange1": np.array([90,255,255]),
        "pnpCam": "pi"
    }
}
# ------ Debugging/At Home Copy -------

# picam parameters ---------------------------------------------
# see: https://picamera.readthedocs.io/en/release-1.13/api_camera.html
#
#  analog_gain: read-only after setting exposure/iso
#  annotate_*
#  awb_gains:  red-blue balance depends upon awb_mode != "off"
#              range: 0-8, typically: .9-1.9
#  awb_mode: ("auto") ["off", "auto", "cloudy", ...' (white balance)
#  brightness: (50) [0-100]
#  clock_mode
#  closed: read-only
#  color_effects: (None) or (u,v) between 0-255
#  contrast: (0) [-100, 100]
#  crop: (see zoom)
#  digital_gain: read-only after setting exposure/iso
#  drc_strength (off) [off, low, medium, high] (dynamic range compression)
#  exposure_compensation (0) [-25, 25]
#  exposure_mode (auto) [off, auto, ..., fixedfps, ...]
#       off is special: disabled auto-gain-control fixing values for 
#       digital_gain and analog_gain.  These are set indirectly via
#       iso call which should be made (and allowed to settle) before
#       setting the mode to off.
#  exposure_speed: read-only microseconds, relates to shutter-speed
#                   note this value tends to drift torwards a few values
#  flash_mode:
#  frame:
#  framerate: pertains to video-port captures. Coupled with resolution
#       determines the mode that the camera operates in. 
#       see also sensor_mode
#  framerate_range:
#  hflip, vflip:  (False)
#  image_denoise: (True)
#  image_effect: (none) [none,negative,blur,...,posterize...]
#  iso (light sensitivity): sets analog_gain and digital_gain
#       (0) [0,100,200,320,400,500,640,800] (0 is auto)
#   certain exposure_modes override iso (esp "off") 
#  led (False)
#  meter_mode: (average) [average,spot,backlit,matrix]
#  preview...
#  raw_format: deprecated
#  recording: read-only
#  resolution: (X,Y), 'XxY', etc
#  revision: read-only  [ov5647, imx219]  means V1 or V2 cam module
#  saturation: (0) [-100, 100]
#  sensor_mode: (0) [0-7]  (0 computes based on framerate & res, 7 is fastest)
#  sharpness: (0) [-100,100]
#  shutter_speed: (0) microsecs (set with framerate, overlap exposure_speed)
#  still_stats
#  timestamp
#  vflip, hflip: (False)
#  video_denoise: (True)
#  video_stabilization: (False)
#  zoom: (0,0,1,1)

# algo parameters ---------------------------------------------

