# Setting Distrobox with Ubuntu 20.04 and podman

## Intro
Distrobox is a versatile tool that allows users to run any Linux distribution inside their terminal, providing a seamless integration with the host system. It leverages containerization technologies like Podman or Docker to create and manage these environments. 

By using Podman, Distrobox can create containers that are tightly integrated with the host, allowing for the sharing of the user’s HOME directory, external storage, USB devices, graphical applications (X11/Wayland), and audio12. This integration ensures that users can enjoy the flexibility of different Linux distributions while maintaining a cohesive and efficient workflow on their primary system.

## Prerequisite

The current setting up was tested with (click on the following link to install each dependency):
- [Distrobox version: 1.4.1](https://distrobox.it/)
- [Podeman version 3.4.2](install_podman_ubuntu20.04.md)

After the installation, in Ubuntu 20.04, the `distrobox-init` file should be edited.

Access the distrobox bin folder by running:

```bash
cd $(dirname $(which distrobox))/..
```

And comment out the following lines:

 ```text
    apt-get install -y \
        libegl1-mesa \ 
        libgl1-mesa-glx 
```
				

# Usage

1. Create a distrobox called `ubuntu_jazzy` using a `ros:jazzy` image. **The distro is created only once** .
    ```bash
    distrobox-create --name ubuntu_jazzy --image ros:jazzy
    ```
   
2. Check the created distroboxes by:
    ```bash
    distrobox-list
    ```

3. To access a last created distrobox, just run the following command.:

    ```bash
    distrobox-enter ubuntu_jazzy 
    ```
    **NOTE:** To access with sudo privileges, just type:
    
    ```bash
    distrobox-enter ubuntu_jazzy -a "-u 0"
    ```
