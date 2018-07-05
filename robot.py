import sys

adjective=""
if len(sys.argv)==2:
    adjective=sys.argv[1]
print("Hello, I am a %s robot"%adjective)
