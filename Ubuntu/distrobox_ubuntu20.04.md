# Setting Distrobox with Ubuntu 20.04 and Podman

## Intro
Distrobox is a versatile tool that allows users to run any Linux distribution inside their terminal, providing a seamless integration with the host system. It leverages containerization technologies like Podman or Docker to create and manage these environments. 

By using Podman, Distrobox can create containers that are tightly integrated with the host, allowing for the sharing of the user’s HOME directory, external storage, USB devices, graphical applications (X11/Wayland), and audio12. This integration ensures that users can enjoy the flexibility of different Linux distributions while maintaining a cohesive and efficient workflow on their primary system.



## Prerequisite

<span style="color: red;">
❗️ The specific versions of the tools mentioned in this guide are required only for Ubuntu 20.04. This is because the latest versions of both Distrobox and Podman do not support this OS version. If you are using a more recent version of Ubuntu, you can use the latest versions of these tools without any issues.
</span>

The current setting up was tested with (click on the following link to install each dependency):
- [Distrobox version: 1.4.1](https://distrobox.it/)
- [Podman version 3.4.2](install_podman_ubuntu20.04.md)


Set the podman as main container manager by (useful in case you have Docker installed):

```bash
export DBX_CONTAINER_MANAGER=podman
```

**NOTE:** include this command in `.bashrc` to guarantee the podman as main container manager:

```bash
echo 'export DBX_CONTAINER_MANAGER=podman' >> ~/.bashrc
```

```bash
source ~/.bashrc
```

> ➤ **NOTE**:
> It is possible to create a configuration file to distrobox, thus avoiding editing env variables.
> Configuration files can be placed in the following paths, from the least important to the most important:
>
>    - /usr/share/distrobox/distrobox.conf
>    - /usr/etc/distrobox/distrobox.conf
>    - /etc/distrobox/distrobox.conf
>    - ${HOME}/.config/distrobox/distrobox.conf
>    - ${HOME}/.distroboxrc
> 
> Example configuration file:
> 
>```text
>container_always_pull="1"
>container_generate_entry=0
>container_manager="docker"
>container_image_default="registry.opensuse.org/opensuse/toolbox:latest"
>container_name_default="test-name-1"
>container_user_custom_home="$HOME/.local/share/container-home-test"
>container_init_hook="~/.local/distrobox/a_custom_default_init_hook.sh"
>container_pre_init_hook="~/a_custom_default_pre_init_hook.sh"
>container_manager_additional_flags="--env-file /path/to/file --custom-flag"
>container_additional_volumes="/example:/example1 /example2:/example3:ro"
>non_interactive="1"
>skip_workdir="0"
>PATH="$PATH:/path/to/custom/podman"

# Usage

1. Create a distrobox called `ubuntu_jazzy` using a `ros:jazzy` image. 

   **The distrobox is created only once.** 
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
   
   > **NOTE:** If you encounter issues with password setup during access, try using sudo privileges by typing:
   >
   >    ```bash
   >    distrobox-enter ubuntu_jazzy -a "-u 0"
   >    ```
   >

4. You could monitor the distrobox image startup by typing in another terminal the following:
   ```bash
   podman logs -f ubuntu_jazzy
   ```

   >  ➤ **NOTE**:
   >If a error occur while entering into the distrobox regarding the `mesalib` dependencies, do the following:
   >
   >Access the distrobox bin folder by running:
   >
   >```bash
   >cd $(dirname $(which distrobox))/.
   >```
   >
   >And comment out the following lines into  `distrobox-init` file:
   >
   > ```text
   >    apt-get install -y \
   >        libegl1-mesa \ 
   >        libgl1-mesa-glx 
   > ```
   > 
   
5. To exit the distrobox, just type `exit`  inside the distrobox terminal.
