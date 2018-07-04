parts={"rgb camera": "recieving visual data", "motors": "operating at optimal rpm", 
        "battery": "fully charged", "depth camera": "recieving depth data"}
print("Hello, I am a robot")
print("These are the parts I have installed")
for part in parts:
    print("%s: %s" %(part, parts[part]))
