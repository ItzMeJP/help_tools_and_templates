#  Opencv 4.7 "dnn" module with Nvidia GPU, Cuda and CuDnn

1. Install the Dependencies

 ```
sudo apt install build-essential cmake git pkg-config libgtk-3-dev \
libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
gfortran openexr libatlas-base-dev python3-dev python3-numpy \
libtbb2 libtbb-dev libdc1394-22-dev libopenexr-dev \
libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
 ```

2. Create directory to download opencv from source

 ```
mkdir ~/opencv_build && cd ~/opencv_build
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
 ```

3. Change branch to desired version
 ```
cd ~/opencv_build/opencv
git checkout 4.7
cd ~/opencv_build/opencv_contrib
git checkout 4.7
 ```

4. Create build folder
 ```
cd ~/opencv_build/opencv
mkdir -p build && cd build
```

5. Configure Cmake with the desired settings | Change CUDA_ARCH_BIN version to be compatible with your GPU. To check the version go to [NVIDIA](https://developer.nvidia.com/cuda-gpus)
and search your GPU.

 ```
  cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D INSTALL_C_EXAMPLES=OFF \
  -D INSTALL_PYTHON_EXAMPLES=OFF \
  -D OPENCV_GENERATE_PKGCONFIG=ON \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
  -D BUILD_EXAMPLES=ON \
  -D WITH_CUDNN=ON \
  -D OPENCV_DNN_CUDA=ON \
  -D ENABLE_FAST_MATH=1 \
  -D CUDA_FAST_MATH=1 \
  -D CUDA_ARCH_BIN=8.6 \
  -D WITH_CUBLAS=1 ..
 ```

6. Compile Opencv
  ```
make -j8
sudo make install
 ```
