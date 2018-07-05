import sys
from module import module

adjective=""
if len(sys.argv)==2:
    adjective=sys.argv[1]

if len(adjective)>0 and adjective[0] in ['a', 'e', 'i', 'o', 'u']:
    adjective="an "+adjective
elif len(adjective)>0:
    adjective="a "+adjective
else:
    adjective="a"




rgbcam=module("rgb camera", "recieving visual data", "rgb image")
motors=module("motors", "operating at optimal rpm", "odometry")
battery=module("battery", "fully charged", "voltage")
gps=module("GPS", "recieving location data",  "location data")
imu=module("IMU", "getting quaternions",  "quaternions")
depthcam=module("depth camera", "recieving depth data",  "depth image")

parts=[rgbcam, motors, battery, gps, imu, depthcam]

print("Hello, I am %s robot"%adjective)
print("These are the parts I have installed")
for part in parts:
    part.start()

for part in parts:
    part.stop()
