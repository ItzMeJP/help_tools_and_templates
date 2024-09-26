# Setting Distrobox Podman and Nvidia

### Authors
  - Artur José Cordeiro
  - João Pedro Souza

## Prerequisite

The current setting up was tested with (click on the following link to install each dependency):
- [Distrobox version: 1.4.1](https://distrobox.it/)
- [Podman version 3.4.2](install_podman_ubuntu20.04.md)
- [Nvidia Container Toolkit version 1.16.1](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)


Install the nvidia container toolkit as following:

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```
```bash
sudo apt-get update
```
```bash
sudo apt-get install -y nvidia-container-toolkit
```

Configure it to be compatible with podman.

```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```

```bash
sudo systemctl restart podman
```

## Usage: tensorflow example

Create the box.
```bash
distrobox-create --name tester_tensorflow --nvidia --image tensorflow/tensorflow:nightly-gpu
```

Enter the box.
```bash
distrobox enter tester_tensorflow
```

## Usage: pytorch example

Create the box.
```bash
distrobox-create --name tester_pytorch --nvidia --image pytorch/pytorch:2.4.1-cuda11.8-cudnn9-devel
```

Enter the box.
```bash
distrobox enter tester_pytorch
```


<span style="color: red;">
❗️Only the pytorch devel category images works with CUDA.

❗️Currently, only recent image versions support CUDA within Podman. If your images do not work with CUDA, try using Docker by following this [tutorial](distrobox_docker_nvidia.md).
</span>
