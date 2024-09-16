# Enabling GPU Access for Docker Containers

This guide explains how to give Docker containers access to GPUs, which is essential for tasks involving machine learning, data processing, or any GPU-accelerated computation.

## Prerequisites

1. **NVIDIA GPU:** Ensure that you have an NVIDIA GPU installed on your machine.
2. **NVIDIA Driver:** Install the appropriate NVIDIA driver for your GPU.
3. **Docker:** Make sure Docker is installed on your system.
4. **NVIDIA Docker Toolkit (nvidia-docker):** This toolkit allows Docker to use NVIDIA GPUs.

## Step-by-Step Instructions

### 1. Install the NVIDIA Driver

Ensure that the NVIDIA driver is installed and properly configured on your system. You can download the driver from the [NVIDIA website](https://www.nvidia.com/Download/index.aspx). Follow the installation instructions specific to your operating system.

To check if the driver is installed correctly, run:

```bash
nvidia-smi
```

This command should display information about your GPU.

### 2. Install Docker

If Docker is not installed, follow the installation guide for your operating system from the [official Docker documentation](https://docs.docker.com/get-docker/).

To check if the docker is installed correctly, run:

```bash
docker --version
```

### 3. Install the NVIDIA Container Toolkit

The NVIDIA Container Toolkit allows Docker to utilize GPU resources. Install it by following these steps or the [official NVIDIA Container Toolkit documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html):

#### For Ubuntu:

1. **Configure the production repository::**

    ```bash
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    ```

    

2. **Update the package list and Install the NVIDIA Container Toolkit packages:**

    ```bash
    sudo apt-get update
    sudo apt-get install -y nvidia-container-toolkit
    ```

3. **Configure the container runtime by using the nvidia-ctk command:**

    ```bash
    sudo nvidia-ctk runtime configure --runtime=docker
    ```

4. **Restart the Docker daemon:**

    ```bash
    sudo systemctl restart docker
    ```

#### For Other Linux Distributions:

Refer to the [NVIDIA documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) for instructions specific to your distribution.

### 4. Verify the Installation

Check if Docker can detect your GPU by running a test container. Use the following command to run a container with GPU access:

```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

This command runs a CUDA-based image and should output details about your GPU, similar to running `nvidia-smi` directly on your host.

### 5. Running Docker Containers with GPU Access

To run a Docker container with GPU access, use the `--gpus` flag followed by the desired configuration. For example:

- **To use all available GPUs:**

    ```bash
    docker run --gpus all <image-name>
    ```

- **To use a specific number of GPUs:**

    ```bash
    docker run --gpus 2 <image-name>
    ```

- **To use specific GPUs:**

    ```bash
    docker run --gpus '"device=0,1"' <image-name>
    ```

Replace `<image-name>` with the name of the Docker image you want to run.

### 6. Troubleshooting

- **Check Docker Logs:** If the container fails to start or GPU resources are not available, check Docker logs for error messages.

    ```bash
    docker logs <container-id>
    ```

- **Verify NVIDIA Driver and Toolkit:** Ensure that the NVIDIA driver and container toolkit are correctly installed and compatible with each other.

- **Consult NVIDIA Documentation:** For advanced configurations or issues, refer to the [NVIDIA documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/).


### 7. Forums

Check the following forums and discussions if you encounter issues or need further assistance:

- **[Bobcares](https://bobcares.com/blog/docker-failed-to-initialize-nvml-unknown-error/):** This discussion helped me especially after applying method 1. It addresses common errors like "failed to initialize NVML" and provides troubleshooting steps.
- **[Stack Overflow](https://stackoverflow.com/questions/76812471/docker-compose-with-gpu-access):** A valuable resource for questions related to Docker Compose and GPU access. You can find solutions and discussions on similar issues faced by others.

These forums can be a great starting point for finding solutions or engaging with the community for more support.

## Conclusion

With the NVIDIA Docker Toolkit installed and configured, you can now leverage GPU resources within your Docker containers for accelerated computing tasks. If you encounter any issues or need further assistance, consult the official documentation or seek support from the Docker and NVIDIA communities.