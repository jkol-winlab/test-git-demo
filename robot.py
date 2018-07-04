parts={"camera": "recieving visual data", "motors": "operating at optimal rpm", "battery": "fully charged"}
print("Hello, I am a robot")
for part in parts:
    print("%s: %s" %(part, parts[part]))
