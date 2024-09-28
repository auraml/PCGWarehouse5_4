import os
import unreal


def export_static_mesh_to_obj(static_mesh, export_dir):
    static_mesh_name = static_mesh.get_name()
    file_name = export_dir + static_mesh_name + ".obj"
    print("Exporting static mesh to: {}".format(file_name))

    # exportTask
    exportTask = unreal.AssetExportTask()
    exportTask.object = static_mesh
    exportTask.filename = file_name
    exportTask.automated = True
    exportTask.replace_identical = True
    exportTask.prompt = False

    objExporter = unreal.StaticMeshExporterOBJ()
    exportTask.exporter = objExporter
    objExporter.run_asset_export_task(exportTask)


static_mesh_dir = "/Game/PCG/Racks/Meshes/"
export_dir = "D:\\UnrealProjects\\PCGWarehouse5_4\\Scripts\\exported_objs\\"

# iterate all static meshes in the directory - class should be StaticMesh
for asset_path in unreal.EditorAssetLibrary.list_assets(static_mesh_dir):
    static_mesh = unreal.EditorAssetLibrary.load_asset(asset_path)
    if isinstance(static_mesh, unreal.StaticMesh):
        # print(asset_path)
        export_static_mesh_to_obj(static_mesh, export_dir)

# delete all files with UV1 and Internal in the name
for file in os.listdir(export_dir):
    if "UV1" in file or "Internal" in file:
        os.remove(export_dir + file)
        print("Deleted: {}".format(file))
