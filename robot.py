parts={"rgb camera": "recieving visual data", "motors": "operating at optimal rpm", 
        "battery": "fully charged", "GPS": "recieving location data", 
        "IMU":"getting quaternions", "depth camera": "recieving depth data"}
print("Hello, I am a robot")
for part in parts:
    print("%s: %s" %(part, parts[part]))
