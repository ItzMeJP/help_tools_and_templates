# Training a Machine Learning Model in a Container with GPU Usage

## Overview

This guide will walk you through the process of setting up and training a machine learning model using Docker containers with GPU support. Leveraging containers ensures a consistent environment for development and deployment, while utilizing GPU acceleration significantly speeds up the training process.

## Prerequisites

- **Docker**: Install Docker from [here](https://docs.docker.com/get-docker/).
- **GPU Access for Docker Containers**: Ensure your system has GPU support configured for Docker. Follow instructions [here](https://github.com/brumocas/Docker/tree/main/GPU).

## Setup

### Step 1: Check Your CUDA, cuDNN, and PyTorch Versions

Execute the following script to check the versions of CUDA, cuDNN, and PyTorch installed in your local machine learning project:

```python
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("cuDNN version:", torch.backends.cudnn.version())
    print("CUDA version:", torch.version.cuda)
else:
    print("CUDA and cuDNN are not available on this system.")
```

### Step 2: Find a Docker Image Matching Your Versions

Go to [Docker Hub](https://hub.docker.com/r/pytorch/pytorch/tags) and find an image tag that matches the versions of CUDA, cuDNN, and PyTorch used in your project.

### Step 3: Pull the Corresponding Docker Image

Pull the Docker image that corresponds to your versions of CUDA, cuDNN, and PyTorch. 

For example:

```bash
docker pull pytorch/pytorch:2.4.0-cuda11.8-cudnn9-runtime
```

### Step 4: Create a Dockerfile

Create a `Dockerfile` to set up the environment for training your model. Here is an example:

```dockerfile
# Use the base PyTorch image with CUDA and cuDNN support
FROM pytorch/pytorch:2.4.0-cuda11.8-cudnn9-runtime

# Install git and other dependencies
RUN apt-get update && \
    apt-get install -y \
    libglib2.0-0 \
    git

# Clone your machine learning project repository
RUN git clone https://github.com/<your_username>/<your_repository>.git /workspace/<your_repository>

# Set the working directory to /workspace/<your_repository>
WORKDIR /workspace/<your_repository>

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
```

### Step 5: Build the Docker Image

Build the Docker image using the `Dockerfile`:

```bash
docker build -t ml-gpu-container .
```

#### Explanation of `docker build -t` Command

- **`docker build`**: Initiates the build process.
- **`-t ml-gpu-container`**: Names the image `ml-gpu-container`. Since no tag is specified, it defaults to `latest`, making the full name `ml-gpu-container:latest`.
- **`.`**: Specifies the current directory as the build context. This means Docker will look for a Dockerfile in the current directory and use the contents of this directory for the build.

### Step 6: Create a Shell Script to Run the Docker Container

Create a shell script to run the Docker container with GPU support:

```sh
#!/bin/bash

function docker_run_com_interface(){
  sudo docker run --gpus all -ti --net=host --ipc=host -e DISPLAY=$DISPLAY -v $2:$3 -v /tmp/.X11-unix:/tmp/.X11-unix -v $XAUTHORITY:/tmp/.XAuthority -e XAUTHORITY=/tmp/.XAuthority --env="QT_X11_NO_MITSHM=1" $1 /bin/bash
}

# Usage: ./run_container.sh <docker_image_name> <host_path> <container_path>
docker_run_com_interface ml-gpu-container $1 $2
```

Make the script executable:

```bash
chmod +x run_container.sh
```

### Step 7: Run the Docker Container with GPU Support

Run the container with GPU support enabled by executing the shell script:

```bash
./run_container.sh <host_path> <container_path>
```

- `ml-gpu-container`: Docker image name.
- `host_path`: Host directory to mount inside the container.
- `container_path`: Container path to mount.

### Example

Check a complete example in the following [DOPE](https://github.com/brumocas/DOPE/tree/main/train/docker) git repository.

### Conclusion

By following this guide, you can set up a Docker container with GPU support and train your machine learning model in a consistent and accelerated environment. This approach ensures that your development environment is reproducible and leverages the power of GPUs to speed up the training process.

For any issues or contributions, feel free to submit a Pull Request or open an issue.

## Acknowledgments

- [PyTorch](https://pytorch.org/)
- [CUDA](https://developer.nvidia.com/cuda-zone)
- [cuDNN](https://developer.nvidia.com/cudnn)
