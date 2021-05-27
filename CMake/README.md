# CMAKE

### Overview

Simple strategies with CMAKE - Version 3.19.

#### Notes
It is important to note that, cmake only runs with the load command. For instance, the message() command will only print an output when the load command is executed over the CMakefile.txt.

## Summary

* [Creating a CMAKE Tree Architecture](#tree)
* [Generating a Global CMAKE Variable](#globalvar)
* [If statement with Global Variable](#ifglobalvar)
* [Getting an Absolute Path inside a CMAKE](#getabspath)


### <a name="tree"></a>1. Creating a CMAKE Tree Architecture

The following example demonstrates some key ideas of CMake. Make sure that you have CMake installed prior to running this example (go here for instructions).

There are three directories involved. The top level directory has two subdirectories called ./Demo and ./Hello. In the directory ./Hello, a library is built. In the directory ./Demo, an executable is built by linking to the library. A total of three CMakeLists.txt files are created: one for each directory.

The first, top-level directory contains the following CMakeLists.txt file.

```# CMakeLists files in this project can
# refer to the root source directory of the project as ${HELLO_SOURCE_DIR} and
# to the root binary directory of the project as ${HELLO_BINARY_DIR}.
cmake_minimum_required (VERSION 2.8.11)
project (HELLO)

# Recurse into the "Hello" and "Demo" subdirectories. This does not actually
# cause another cmake executable to run. The same process will walk through
# the project's entire directory structure.
add_subdirectory (Hello)
add_subdirectory (Demo)
```

Then for each subdirectory specified, CMakeLists.txt files are created. In the ./Hello directory, the following CMakeLists.txt file is created:

```# Create a library called "Hello" which includes the source file "hello.cxx".
# The extension is already found. Any number of sources could be listed here.
add_library (Hello hello.cxx)

# Make sure the compiler can find include files for our Hello library
# when other libraries or executables link to Hello
target_include_directories (Hello PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
```

Finally, in the ./Demo directory, the third and final CMakeLists.txt file is created:
```
# Add executable called "helloDemo" that is built from the source files
# "demo.cxx" and "demo_b.cxx". The extensions are automatically found.
add_executable (helloDemo demo.cxx demo_b.cxx)

# Link the executable to the Hello library. Since the Hello library has
# public include directories we will use those link directories when building
# helloDemo
target_link_libraries (helloDemo LINK_PUBLIC Hello)
```
#### References
[1. https://cmake.org/examples/](https://cmake.org/examples/)

### <a name="globalvar"></a>2. Generating a Global CMAKE Variable

To define a global variable to be used across different CMAKEs inside a hierarchical tree, just set it in CACHE, as:

```
set(EXPORT_PATH_USED_INTO_SUBDIRS #defining a shared CMAKE var.
        include
        ${CMAKE_CURRENT_SOURCE_DIR}
        CACHE INTERNAL "")
```

Once it has been created, it only will be deleted with the command below. Be notice that only removing the set will not delete the variable from cache.

```
unset(EXPORT_PATH_USED_INTO_SUBDIRS CACHE)
```


### <a name="ifglobalvar"></a>3. If statement with Global Variable

To check if a CACHE (or global variable) exist, junt use:
```
if (DEFINED CACHE{EXPORT_PATH_USED_INTO_SUBDIRS})
    target_include_directories (simple_serial PUBLIC
            $CACHE{EXPORT_PATH_USED_INTO_SUBDIRS})
    message(STATUS "The lib ${PROJECT_NAME} is defined as a static CMAKE subdir located ${DIR_ONE_ABOVE}")
else()
    message(STATUS "The lib ${PROJECT_NAME} is not defined as a static CMAKE subdir")
endif ()
```


### <a name="getabspath"></a>4. Getting an Absolute Path inside a CMAKE

To get the parent path of current CMakeFile, for instance, use:

```
get_filename_component(DIR_ONE_ABOVE ../ ABSOLUTE)
```

or even more...

```
get_filename_component(DIR_TWO_ABOVE ../../ ABSOLUTE)
```
