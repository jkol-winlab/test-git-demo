from module import module

rgbcam=module("rgb camera", "recieving visual data", "rgb image")
motors=module("motors", "operating at optimal rpm", "odometry")
battery=module("battery", "fully charged", "voltage")
gps=module("GPS", "recieving location data",  "location data")
imu=module("IMU", "getting quaternions",  "quaternions")
depthcam=module("depth camera", "recieving depth data",  "depth image")

parts=[rgbcam, motors, battery, gps, imu, depthcam]

print("Hello, I am a robot")
print("These are the parts I have installed")
for part in parts:
    part.start()

for part in parts:
    part.stop()
