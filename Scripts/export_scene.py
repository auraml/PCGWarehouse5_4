import unreal
import json
import random
import time


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

        if static_mesh_name not in instance_transforms:
            instance_transforms[static_mesh_name] = []
        instance_transforms[static_mesh_name].append(instance_data)

    return instance_transforms


def get_rack_actor(actors):
    for actor in actors:
        actor_name = actor.get_actor_label()  # Get the actor's name
        if actor_name == "BP_Racks":
            return actor

    return None


def get_scene_data(rack_actor):
    scene_data = []

    # get all HISMC of rack_actor
    hismc = rack_actor.get_components_by_class(
        unreal.HierarchicalInstancedStaticMeshComponent)
    for component in hismc:
        scene_data.append(get_hism_instance_transforms(component))
    return scene_data


if __name__ == "__main__":
    row = random.randint(1, 10)
    col = random.randint(1, 10)
    print(row, col)

    rack_actor = None
    editor_actor_subsystem = unreal.get_editor_subsystem(
        unreal.EditorActorSubsystem)
    actors = editor_actor_subsystem.get_all_level_actors()
    rack_actor = get_rack_actor(actors)

    rack_actor.set_editor_property("Rack Columns", int(col))
    rack_actor.set_editor_property("Rack Rows", int(row))

    scene_data = get_scene_data(rack_actor)

    timestamp = int(time.time() * 1000)
    file_name = f"D:\\UnrealProjects\\PCGWarehouse5_4\\Scripts\\exported_scenes\\scene_data_{timestamp}.json"
    with open(file_name, 'w') as file:
        json.dump(scene_data, file)
