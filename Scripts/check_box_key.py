import os
import json

path = "D:\\UnrealProjects\\PCGWarehouse5_4\\Scripts\\exported_scenes"
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(root, file), "r") as f:
                data = json.load(f)
                if not any("Box" in key for key in data.keys()):
                    print()
                    print(file)
                    for key in data.keys():
                        print("-", key, ":\t", len(data[key]))
