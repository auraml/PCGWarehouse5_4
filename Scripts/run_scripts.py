import unreal
import json
import random


def run_script(script_path, args):
    # Execute the script and capture output
    output = unreal.SystemLibrary.execute_python_script(script_path, args)
    return output


path = "D:/UnrealProjects/PCGWarehouse5_4/Scripts/prev_config.json"
prev = (1, 1)
with open(path, 'r') as file:
    data = json.load(file)
    prev = (data['rows'], data['columns'])

current_row = random.randint(1, 10)
current_col = random.randint(1, 10)

script = "D:/UnrealProjects/PCGWarehouse5_4/Scripts/export_scene.py"
command = f'py "{script}" "{prev[0]}" "{prev[1]}" "{current_row}" "{current_col}"'
output = unreal.SystemLibrary.execute_console_command(
    unreal.EditorLevelLibrary.get_editor_world(), command)

# write current data to json file
data = {
    "rows": current_row,
    "columns": current_col
}
with open(path, 'w') as file:
    json.dump(data, file)
