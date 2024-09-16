# Obtaining a 3D Object Model Using Go!SCAN 3D

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Steps to Scan an Object Using Go!SCAN 3D](#steps-to-scan-an-object-using-goscan-3d)
4. [Post-Processing the Scan](#post-processing-the-scan)
5. [Exporting the 3D Model](#exporting-the-3d-model)
6. [Post-Processing with Blender (Optional)](#post-processing-with-blender-optional)
7. [Post-Processing with MeshLab (Optional)](#post-processing-with-meshlab-optional)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)
10. [Conclusion](#conclusion)

---

## Introduction

The **Go!SCAN 3D** by Creaform enables users to quickly capture the geometry of real-world objects and convert them into high-quality 3D models. This guide outlines the steps for scanning and refining these models using **VXelements**, with optional post-processing in **Blender** or **MeshLab** to optimize models for various applications like 3D printing and visualization.

---

## Requirements

### Hardware:
- **Go!SCAN 3D** Scanner
- A **computer** meeting the minimum system requirements for 3D modeling
- **Object** to scan

### Software:
- **VXelements** (Creaform’s 3D scanning software)
- **Blender** (optional for post-processing)
- **MeshLab** (optional for post-processing)

---

## Steps to Scan an Object Using Go!SCAN 3D

### Step 1: Setting Up the Hardware
1. **Connect the Go!SCAN 3D** to your computer via USB.
2. Ensure the **power supply** is connected or that the scanner is charged.
3. **Launch VXelements** on your computer.

### Step 2: Preparing for the Scan
1. **Calibrate the Scanner** by following VXelements' prompts.
2. **Prepare the Object**: Place it in a well-lit environment and ensure stability.
3. **Position the Scanner** approximately 30 cm away from the object.

### Step 3: Scanning the Object
1. **Initiate the Scan**: Press the **Start Scan** button in VXelements.
2. **Move the Scanner** around the object smoothly, ensuring all angles are captured.
3. Once complete, press **Stop Scan** to end the process.

For detailed guidance, refer to this [Go!SCAN 3D tutorial](https://www.youtube.com/watch?v=gOcrMLy9jEg).

---

## Post-Processing the Scan

### Step 4: Cleaning and Finalizing the Scan
1. **Clean the Scan**: Remove noise and artifacts using VXelements’ tools.
2. **Generate a 3D Mesh**: Convert the point cloud into a usable 3D mesh and adjust the resolution as needed.

---

## Exporting the 3D Model

### Step 5: Exporting the 3D Model
1. Export the processed 3D model from VXelements in your desired format:
   - **OBJ**
   - **STL**
   - **PLY**
   - **FBX**

---

## Post-Processing with Blender (Optional)

### Step 6: Refining and Simplifying the 3D Model in Blender

**Blender** is a versatile tool that can be used for refining and simplifying the 3D model exported from VXelements. The following script automates model scaling and polygon simplification using the **Decimate Modifier**.

### Blender Python Script
To automate model simplification and scaling, follow these steps in Blender:

1. **Download and Install Blender** from [Blender’s official site](https://www.blender.org/download/).
2. **Run the Script** below in Blender’s text editor:

```python
import bpy
import os
import re

def decimate_object(obj, ratio=0.5):
    """Apply a decimate modifier to simplify the mesh."""
    decimate_modifier = obj.modifiers.get('Decimate')
    if not decimate_modifier:
        decimate_modifier = obj.modifiers.new(name='Decimate', type='DECIMATE')
    decimate_modifier.ratio = ratio
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
    """Remove trailing numbers and dots from the object name."""
    return re.sub(r'[.\d]+$', '', name).strip()

# Delete all existing objects to start fresh
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Define file paths (update this path to your actual file)
input_file_path = '/path/to/your/3d_model.obj'
base_name = os.path.splitext(os.path.basename(input_file_path))[0]

# Define export directories
output_directory = os.path.dirname(input_file_path)
raw_folder = os.path.join(output_directory, "raw")
simple_folder = os.path.join(output_directory, "simple")

# Ensure the raw and simple folders exist
ensure_directory(raw_folder)
ensure_directory(simple_folder)

# Import the 3D object
bpy.ops.import_scene.obj(filepath=input_file_path)

# Ensure the imported object is selected
if bpy.context.selected_objects:
    obj = bpy.context.selected_objects[0]
    bpy.context.view_layer.objects.active = obj

    # Clean the object name
    object_name = clean_object_name(obj.name)

    try:
        # Scale the object down by 1000
        scale_object(obj, scale_factor=1/1000)

        # Export the scaled object
        raw_file_path = os.path.join(raw_folder, f"{object_name}_raw.obj")
        bpy.ops.export_scene.obj(filepath=raw_file_path, use_selection=True)

        # Apply decimation (reduce polygon count)
        decimate_object(obj, ratio=0.85)
        
        # Export the simplified object
        simple_file_path = os.path.join(simple_folder, f"{object_name}_simple.obj")
        bpy.ops.export_scene.obj(filepath=simple_file_path, use_selection=True)

        print(f"Object exported as {raw_file_path} and {simple_file_path}.")
    except Exception as e:
        print(f"Error during processing: {e}")
else:
    print("No object found to modify.")
```

### Script Workflow:
- **Scaling**: The script scales the model down by a factor of 1000, adjusting the object dimension to meters.
- **Decimation**: The model is simplified using a ratio (adjustable in the script).
- **Export**: Both the raw and simplified models are saved in specified folders.

---

## Post-Processing with MeshLab (Optional)

### Step 7: Using MeshLab for Further Refinement

**MeshLab** is an open-source software for advanced mesh processing. It is an excellent alternative or complement to Blender for cleaning and refining your 3D models. 

1. **Install MeshLab** from [here](http://www.meshlab.net/).
2. **Import Your 3D Model** into MeshLab (supports OBJ, STL, or PLY formats).
3. **Refine the Model**:
   - Simplify the mesh by reducing polygon count.
   - Fix holes, fill gaps, and smooth surfaces.
   - Apply filters to enhance the visual quality.
4. **Export the Refined Model**: Once the edits are complete, export the model in your preferred format.

### Why Use MeshLab?
- **Advanced Repair Tools**: MeshLab provides sophisticated features for repairing models.
- **Lightweight and Free**: MeshLab is user-friendly and suitable for tasks like mesh optimization and refinement.
- **Smoothing and Cleaning**: Apply filters to clean up noisy surfaces and enhance smoothness.

**Important Tip**: In MeshLab, use the **Isotropic Explicit Remeshing** filter to standardize the point cloud distance, and align the axes using the **Transform Rotate** command for better alignment.

---

## Best Practices

- **Lighting**: Ensure consistent, even lighting to avoid shadows and reflections.
- **Surface Preparation**: For reflective objects, use a matte spray for better scan quality.
- **Multiple Scans**: For complex objects, take multiple scans and merge them in VXelements.

---

## Troubleshooting

- **Scan Inaccuracies**: Ensure the scanner is within range and properly calibrated. Reflective surfaces may need to be treated.
- **Alignment Problems**: Use markers or manual adjustments to correct alignment issues.
- **Noise**: Use VXelements, Blender, or MeshLab’s cleaning tools to remove noise and artifacts.

---

## Conclusion

By following this guide, you will be able to scan and refine high-quality 3D models using **Go!SCAN 3D**. While **VXelements** is essential for capturing the scan, **Blender** and **MeshLab** offer powerful options for post-processing and refinement. Combining these tools allows you to optimize your models for a variety of applications, from 3D printing to virtual simulations. 

Happy scanning and modeling!