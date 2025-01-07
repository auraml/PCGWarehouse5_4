import os
import random
import json
from .utils import spawn_obj, get_objects_map, clear_level
import unreal

objecs_map = get_objects_map(asset_path="/Game/PCG/Racks/Meshes")

if __name__ == "__main__":
    base_dir = "D:\\UnrealProjects\\PCGWarehouse5_4\\Scripts\\exported_scenes"
    files = os.listdir(base_dir)
    random_file = random.choice(files)
    print(random_file)
    with open(os.path.join(base_dir, random_file), "r") as f:
        output_json = json.load(f)
        for sm_name, value_list in (output_json.items()):
            sm_obj = objecs_map[sm_name]

            for value in value_list:
                transform = value["translations"]
                spawn_location = unreal.Vector(
                    transform[0], transform[1], transform[2])
                rotation = value["angles"]
                spawn_rotation = unreal.Rotator(
                    rotation[0], rotation[1], rotation[2])
                spawn_obj(
                    sm_obj,
                    spawn_location,
                    spawn_rotation
                )
