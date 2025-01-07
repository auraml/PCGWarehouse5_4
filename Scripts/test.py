import unreal

# Define the path to the Static Mesh asset for a cube
cube_mesh_path = "/Engine/BasicShapes/Cube"

# Load the Static Mesh asset
cube_mesh = unreal.EditorAssetLibrary.load_asset(cube_mesh_path)

# Check if the mesh was loaded successfully
if cube_mesh is None:
    unreal.log_error("Failed to load cube mesh.")
else:
    # Define spawn location and rotation
    spawn_location = unreal.Vector(0, 0, 0)  # Change coordinates as needed
    spawn_rotation = unreal.Rotator(0, 0, 0)  # No rotation

    new_actor = unreal.EditorLevelLibrary().spawn_actor_from_object(
        cube_mesh,
        spawn_location,
        spawn_rotation
    )
