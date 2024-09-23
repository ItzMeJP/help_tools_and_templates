import bpy
import os
import re

def decimate_object(obj, ratio=0.5):
    """Apply a decimate modifier to simplify the mesh."""
    # Add or get the decimate modifier
    decimate_modifier = obj.modifiers.get('Decimate')
    if not decimate_modifier:
        decimate_modifier = obj.modifiers.new(name='Decimate', type='DECIMATE')
    
    # Set decimate type and parameters based on mode
    decimate_modifier.ratio = ratio
    decimate_modifier.decimate_type = 'COLLAPSE'
    
    # Apply the decimate modifier
    bpy.ops.object.modifier_apply(modifier='Decimate')
    
def scale_object(obj, scale_factor=1/1000):
    """Scale the object by a specified factor."""
    obj.scale = (scale_factor, scale_factor, scale_factor)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

def ensure_directory(path):
    """Ensure the directory exists. If not, create it."""
    if not os.path.exists(path):
        os.makedirs(path)

def clean_object_name(name):
    """Remove any trailing numbers and dots from the object name."""
    # Use regex to remove numbers and dots at the end of the name
    return re.sub(r'[.\d]+$', '', name).strip()

# Delete all existing objects to start fresh
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Define file paths
input_file_path = '/home/bruno/Workspace/Master/3D_Scans/Scans/Coffee_Box/Coffee_Box.obj'  # Update this path to your actual file
base_name = os.path.splitext(os.path.basename(input_file_path))[0]

# Define export directories
output_directory = os.path.dirname(input_file_path)
raw_folder = os.path.join(output_directory, "raw")
simple_folder = os.path.join(output_directory, "simple")

# Ensure the raw and simple folders exist
ensure_directory(raw_folder)
ensure_directory(simple_folder)

# Import the 3D object
try:
    bpy.ops.import_scene.obj(filepath=input_file_path)
except Exception as e:
    print(f"Error importing file: {e}")

# Ensure the imported object is selected and active
if bpy.context.selected_objects:
    obj = bpy.context.selected_objects[0]
    bpy.context.view_layer.objects.active = obj

    # Clean the object name (remove trailing numbers and dots)
    object_name = clean_object_name(obj.name)

    try:
        # Scale down the object by 1000
        scale_object(obj, scale_factor=1/1000)

        # Export the scaled raw object to the raw folder
        raw_file_path = os.path.join(raw_folder, f"{object_name}_raw.obj")
        bpy.ops.export_scene.obj(filepath=raw_file_path, use_selection=True)

        # Apply decimate modifier to the object
        decimate_object(obj, ratio=0.85)
        
        # Export the decimated object to the simple folder
        simple_file_path = os.path.join(simple_folder, f"{object_name}_simple.obj")
        bpy.ops.export_scene.obj(filepath=simple_file_path, use_selection=True)

        print(f"Object exported as {raw_file_path} and {simple_file_path}.")
    except Exception as e:
        print(f"Error during object processing or export: {e}")
else:
    print("No object found to modify.")