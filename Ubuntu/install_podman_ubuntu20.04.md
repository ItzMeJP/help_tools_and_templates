# Install Podman in Ubuntu 20.04

Podman is a container engine for Linux-based operating systems that provides a way to manage containers without the need for a separate daemon process. It is an open-source tool that is designed to be a drop-in replacement for the Docker daemon, but without requiring root privileges to run.

Podman uses the same container format and image registries as Docker, which means that you can use it to run Docker images and containers as well. Podman supports multiple container runtimes, including the default runc runtime, which is also used by Docker.

Let's take a look at How to install podman on Ubuntu20.04:

##### 1. Update the package index on your system:
```bash
sudo apt update
```

##### 2. Install the Podman dependencies:
```bash
sudo apt install software-properties-common uidmap
```

##### 3. Add the libcontainers repository:
```bash
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_20.04/ /' > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list"
```

##### 4. And run the
```bash
sudo apt-get update
```
---
##### If you get an error like the following one:

```
W: GPG error: http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_20.04 InRelease: The following signatures couldn’t be verified because the public key is not available: NO_PUBKEY 4D64390375060A  
```

This error message indicates that the GPG key for the OpenSUSE Build Service repository at http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_20.04 is missing from your system. GPG (GNU Privacy Guard) is a tool used for secure communication and verifying the authenticity of software packages and repositories.

To resolve this error, you need to import the missing GPG key for the repository. Here are the steps you can follow:

Identify the GPG key ID mentioned in the error message. In this case, it is 4D64390375060A.

Use the apt-key command to import the missing GPG key. Run the following command, replacing 4D64390375060A with the key ID you obtained in the previous step:
```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 4D64390375060A
```
```bash
sudo apt-get update
```
---

##### 5. Install Podman:

sudo apt-get install podman

##### 6.Verify that Podman is installed correctly by running the following command:

```bash
podman version
```

You should see output similar to the following:

```
Version:      3.4.2
API Version:  3.4.2
Go Version:   go1.15.2
Built:        Thu Jan  1 05:30:00 1970
OS/Arch:      linux/amd64
```

**NOTE** Have a look at sources file (/etc/apt/sources.list) and source directory (/etc/apt/sources.list.d)
Here you can see what are the sources you have added. you can comment-out the package if you dont want or if you facing any issue with that package

---

# Reference

[Original](https://rameshponnusamy.medium.com/install-podman-in-ubuntu-20-04-442649400b3f)
