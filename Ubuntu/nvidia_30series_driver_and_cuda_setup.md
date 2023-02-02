# Nvidia driver, CUDA and cuDNN setup for nvidia 30 series gpu's
##### author: artur.j.cordeiro@inesctec.pt


This setup can change according motherboard manufacturers. It explaines how to install nvidia drivers, CUDA and cuDNN for Ubuntu 20.04. Follow the guide in order, because the next step will not work without the previous one.

### Disabling Secure Boot

1. Go to bios.
2. Advanced mode.
3. Boot.
4. Secure boot- Disable **OR** OS Type- Other OS and clear secure boot keys.
5. Reboot computer.

### Install Nvidia driver

1. [Verify which nvdia driver is compatible with your GPU](https://www.nvidia.com/download/index.aspx).
2. sudo apt update.
3. sudo apt upgrade.
4. Install the desired nvidia driver (version 1):
```
Go to software & updates
Select Additional Drivers
Choose a version to install and click on Apply
```
5. Install the desired nvidia driver (version 2):
```
apt search nvidia-driver
sudo apt install nvidia-driver-x
```
6. sudo reboot.
#### Extra:
```
Find out information about GPU: sudo lshw -C display
Verify installation: nvidia-smi
```

### Install CUDA

1. [Verify CUDA compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/index.html).
2. [Download CUDA toolkit](https://developer.nvidia.com/cuda-toolkit).
3. Install only the CUDA toolkit.
4. Change CUDA path in bash:
```
nano ~/.bashrc
export PATH=$PATH:/usr/local/cuda-x/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-x/lib64
export CUDADIR=/usr/local/cuda-x
source ~/.bashrc
```

### Install cuDNN

1. [Verify compatibility and download cuDNN](https://developer.nvidia.com/cudnn).
2. [Unzip and copy the files into the CUDA toolkit directory](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html):
```
tar -xvf cudnn-linux-x86_64-8.x.x.x_cudaX.Y-archive.tar.xz
sudo cp cudnn-*-archive/include/cudnn*.h /usr/local/cuda/include
sudo cp -P cudnn-*-archive/lib/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```
3. sudo reboot.
