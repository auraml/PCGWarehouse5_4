import unreal
import json
import random
import time

scene_data = {}


def get_arrary_from_vector(input_vector):
    return [input_vector.x, input_vector.y, input_vector.z]


def get_hism_instance_transforms(hism_component):
    instance_transforms = {}
    static_mesh = hism_component.static_mesh
    static_mesh_name = static_mesh.get_name()

    for i in range(hism_component.get_instance_count()):
        transform = hism_component.get_instance_transform(i, False)
        location = get_arrary_from_vector(transform.translation)
        rotation = get_arrary_from_vector(transform.rotation)
        scale = get_arrary_from_vector(transform.scale3d)

        instance_data = {
            'translations': location,
            'angles': rotation,
            'sizes': scale
        }

        if static_mesh_name not in scene_data:
            scene_data[static_mesh_name] = []
        scene_data[static_mesh_name].append(instance_data)

    return instance_transforms


def get_rack_actor(actors):
    for actor in actors:
        actor_name = actor.get_actor_label()  # Get the actor's name
        if actor_name == "BP_Racks":
            return actor
    return None


def get_scene_data(rack_actor):
    # get all HISMC of rack_actor
    hismc = rack_actor.get_components_by_class(
        unreal.HierarchicalInstancedStaticMeshComponent)
    for component in hismc:
        get_hism_instance_transforms(component)


if __name__ == "__main__":
    previous_config_path = "D:\\UnrealProjects\\PCGWarehouse5_4\\Scripts\\prev_config.json"
    prev_row = 1
    prev_col = 1
    with open(previous_config_path, 'r') as file:
        data = json.load(file)
        prev_row = data['rows']
        prev_col = data['columns']

    current_row = random.randint(1, 10)
    current_col = random.randint(1, 10)

    # write current data to json file
    data = {
        "rows": current_row,
        "columns": current_col
    }
    with open(previous_config_path, 'w') as file:
        json.dump(data, file)

    rack_actor = None
    editor_actor_subsystem = unreal.get_editor_subsystem(
        unreal.EditorActorSubsystem)
    actors = editor_actor_subsystem.get_all_level_actors()
    rack_actor = get_rack_actor(actors)

    rack_actor.set_editor_property("Rack Rows", int(current_row))
    rack_actor.set_editor_property("Rack Columns", int(current_col))

    get_scene_data(rack_actor)

    timestamp = int(time.time() * 1000)
    file_name = f"D:\\UnrealProjects\\PCGWarehouse5_4\\Scripts\\exported_scenes\\{timestamp}_{prev_row}_{prev_col}.json"
    with open(file_name, 'w') as file:
        json.dump(scene_data, file)
