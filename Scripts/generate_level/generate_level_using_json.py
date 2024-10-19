import json
from .utils import spawn_obj, get_objects_map, clear_level
import unreal

objecs_map = get_objects_map(asset_path="/Game/PCG/Racks/Meshes")

if __name__ == "__main__":
    # clear_level()
    with open("D:\\UnrealProjects\\PCGWarehouse5_4\\Scripts\\model_output\\bbox_params.json", "r") as f:
        output_json = json.load(f)
        keys = output_json["keys"]
        for index, sm_name in enumerate(keys[0]):
            # sm_obj = objecs_map[sm_name]
            sm_obj = objecs_map[sm_name]["static_mesh_obj"]
            # print(sm_obj)
            transform = output_json["translations"][0][index]
            spawn_location = unreal.Vector(
                transform[0], transform[1], transform[2])

            rotation = output_json["angles"][0][index]
            spawn_rotation = unreal.Rotator(
                rotation[0], rotation[1], rotation[2])

            # print(sm_name, spawn_location, spawn_rotation)

            spawn_obj(
                sm_obj,
                spawn_location,
                spawn_rotation
            )
