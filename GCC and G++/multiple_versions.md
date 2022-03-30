Install multiple C and C++ compiler versions:


sudo apt -y install gcc-7 g++-7 gcc-8 g++-8 gcc-9 g++-9

Use the update-alternatives tool to create list of multiple GCC and G++ compiler alternatives:

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 7 --slave /usr/bin/g++ g++ /usr/bin/g++-7
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8 --slave /usr/bin/g++ g++ /usr/bin/g++-8
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 9 --slave /usr/bin/g++ g++ /usr/bin/g++-9

Check the available C and C++ compilers list on your Ubuntu 20.04 system and select desired version by entering relevant selection number:
sudo update-alternatives --config gcc

For C++ compiler execute:
sudo update-alternatives --config g++

Each time after switch check your currently selected compiler version:
gcc --version
g++ --version
 
