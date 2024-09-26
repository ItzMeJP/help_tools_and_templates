# Obtaining a 3D Object Model Using Go!SCAN 3D

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
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

## Prerequisites

### Hardware:
- **[Go!SCAN 3D](https://get.creaform3d.com/pt/lp-goscan-3d/?aw_campaign=20.90.1.0-[BRANDED]-Search-Portugal-PT&network=g&aw_device=c&keyword=goscan&creative=685513343732&matchtype=e&gad_source=1&gclid=Cj0KCQjwjNS3BhChARIsAOxBM6pBlGntOx8vFb4IuuO1vy7jgv9KyVQqpsbWVENnLmSAVQwoRIGZIp0aAjH0EALw_wcB)** Scanner
- A **computer** meeting the minimum system requirements for 3D modeling
- **Object** to scan

### Software:
- **[VXelements](https://www.creaform3d.com/en/metrology-solutions/3d-applications-software-platforms)** (Creaform’s 3D scanning software)
- **[Blender 3.0.1](https://www.blender.org/download/)** (optional for post-processing)
- **[MeshLab v2023.12](http://www.meshlab.net/)** (optional for post-processing)

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

**Blender** is a versatile tool that can be used for refining and simplifying the 3D model exported from VXelements. The following script automates model **scaling** and **polygon** simplification using the **Decimate Modifier**.

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

--- 

### Step 7: Using MeshLab for Further Refinement

**MeshLab** offers powerful tools for cleaning, simplifying, and optimizing 3D models. You can automate some of these processes using MeshLab’s scripting capabilities. Below is a script to align the object to its principal axis, scale it, and perform isotropic remeshing.


### How to Use the Script in MeshLab:
1. **Install MeshLab** if you haven’t already: [Download MeshLab](http://www.meshlab.net/).
2. **Open your 3D model** (OBJ, STL, or PLY) in MeshLab.
3. **Load the Script**: Go to `Filters` > `Show current filter script` > `Import Script` and load the above script.
4. **Run the `normalize.mlx` Script**: The script will automatically align the object to its principal axis and scale it down.

5. **Run the `remesh.mlx` Script**: The script will automatically apply isotropic remeshing.


### Script for Aligning and Scalling `normalize.mlx`
```xml
<!DOCTYPE FilterScript>
<FilterScript>
 <filter name="Transform: Align to Principal Axis">
  <Param name="pointsFlag" value="true" type="RichBool" tooltip="If selected, only the vertices of the mesh are used to compute the Principal Axis. Mandatory for point clouds or for non water tight meshes" description="Use vertex"/>
  <Param name="Freeze" value="true" type="RichBool" tooltip="The transformation is explicitly applied, and the vertex coordinates are actually changed" description="Freeze Matrix"/>
  <Param name="allLayers" value="false" type="RichBool" tooltip="If selected the filter will be applied to all visible mesh layers" description="Apply to all visible Layers"/>
 </filter>
 <filter name="Transform: Scale, Normalize">
  <Param name="axisX" value="0.001" type="RichFloat" tooltip="Scaling" description="X Axis"/>
  <Param name="axisY" value="0.001" type="RichFloat" tooltip="Scaling" description="Y Axis"/>
  <Param name="axisZ" value="0.001" type="RichFloat" tooltip="Scaling" description="Z Axis"/>
  <Param name="uniformFlag" value="true" type="RichBool" tooltip="If selected an uniform scaling (the same for all the three axis) is applied (the X axis value is used)" description="Uniform Scaling"/>
  <Param name="scaleCenter" value="0" enum_val0="origin" enum_val1="barycenter" enum_val2="custom point" type="RichEnum" tooltip="Choose a method" enum_cardinality="3" description="Center of scaling:"/>
  <Param name="customCenter" y="0" type="RichPosition" tooltip="This scaling center is used only if the 'custom point' option is chosen." x="0" z="0" description="Custom center"/>
  <Param name="unitFlag" value="true" type="RichBool" tooltip="If selected, the object is scaled to a box whose sides are at most 1 unit length" description="Scale to Unit bbox"/>
  <Param name="Freeze" value="true" type="RichBool" tooltip="The transformation is explicitly applied, and the vertex coordinates are actually changed" description="Freeze Matrix"/>
  <Param name="allLayers" value="true" type="RichBool" tooltip="If selected the filter will be applied to all visible mesh layers" description="Apply to all visible Layers"/>
 </filter>
</FilterScript>
```

### Script for Remeshing `remesh.mlx`
```xml
<!DOCTYPE FilterScript>
<FilterScript>
 <filter name="Remeshing: Isotropic Explicit Remeshing">
  <Param name="Iterations" description="Iterations" tooltip="Number of iterations of the remeshing operations to repeat on the mesh." type="RichInt" value="1"/>
  <Param name="Adaptive" description="Adaptive remeshing" tooltip="Toggles adaptive isotropic remeshing." type="RichBool" value="true"/>
  <Param name="SelectedOnly" description="Remesh only selected faces" tooltip="If checked the remeshing operations will be applied only to the selected faces." type="RichBool" value="false"/>
  <Param max="1.18695" name="TargetLen" description="Target Length" tooltip="Sets the target length for the remeshed mesh edges." min="0" type="RichAbsPerc" value="0.01187"/>
  <Param name="FeatureDeg" description="Crease Angle" tooltip="Minimum angle between faces of the original to consider the shared edge as a feature to be preserved." type="RichFloat" value="30"/>
  <Param name="CheckSurfDist" description="Check Surface Distance" tooltip="If toggled each local operation must deviate from original mesh by [Max. surface distance]" type="RichBool" value="false"/>
  <Param max="1.18695" name="MaxSurfDist" description="Max. Surface Distance" tooltip="Maximal surface deviation allowed for each local operation" min="0" type="RichAbsPerc" value="0.01187"/>
  <Param name="SplitFlag" description="Refine Step" tooltip="If checked the remeshing operations will include a refine step." type="RichBool" value="true"/>
  <Param name="CollapseFlag" description="Collapse Step" tooltip="If checked the remeshing operations will include a collapse step." type="RichBool" value="true"/>
  <Param name="SwapFlag" description="Edge-Swap Step" tooltip="If checked the remeshing operations will include a edge-swap step, aimed at improving the vertex valence of the resulting mesh." type="RichBool" value="true"/>
  <Param name="SmoothFlag" description="Smooth Step" tooltip="If checked the remeshing operations will include a smoothing step, aimed at relaxing the vertex positions in a Laplacian sense." type="RichBool" value="true"/>
  <Param name="ReprojectFlag" description="Reproject Step" tooltip="If checked the remeshing operations will include a step to reproject the mesh vertices on the original surface." type="RichBool" value="true"/>
 </filter>
</FilterScript>
```

### Key Steps in the Scripts:
- **Alignment to Principal Axis**: Ensures the object is properly aligned for easier manipulation.
- **Scaling**: Scales the model uniformly by a factor of 0.001. (Final object in meters)
- **Isotropic Remeshing**: Simplifies and refines the model by adjusting the edge length and smoothing the mesh.


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