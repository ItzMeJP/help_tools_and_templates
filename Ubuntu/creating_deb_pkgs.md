# Building binary deb packages

First create a temporary directory such as:

``` mkdir hello_1.0-1_amd64 ```

This command follows the convention of ``` <name>_<version>-<revision>_<architecture> ``` where version is the version of the binary and revision the number of the current deb pkg. The architecture is the hardware type which the program will be run on.

In the temporary folder, create the the folder hierachy which the program should be placed, such as:

``` cd hello_1.0-1_amd64 ```
``` mkdir -p /usr/local/bin ```

Then put the executable of the program inside of it.

Now create the control file with the definitions of the deb pkg.

``` cd hello_1.0-1_amd64 ```
``` mkdir DEBIAN ```
``` cd DEBIAN ```
``` gedit control ```

Place the follow text block with the pkg information:

``` Package: 6DMimic
Version: 1.0
Architecture: amd64
Maintainer: Joao  <joao@email.pt>
Depends: libfoo1 (>= 1.12.4), libfoo2 (>= 2.14),
Description:  A program that greets you.
 You can add a longer description here. Mind the space at the beginning of this paragraph.
 ```

 You can find the depend list of the executable by:
1. Create a ```debian/control``` inside the ```hello_1.0-1_amd64``` directory (its a LOWCASE debian-control definition).
2. Place a empty control inside of it.
3. Run the command ```dpkg-shlibdeps -O hello_1.0-1_amd64/$path_to_binary```.
4. Just copy the output in "Depends" tag inside ```hello_1.0-1_amd64/DEBIAN/control```.
5. Not necessary, but you can remove ```debian/control```.

**obs:** the ```debian/control``` is only needed so the command of line 3. could work!

If the directory hierarchy include root folders, it could be interesting to set the permission, such as:

```sudo chmod -R a+rwx hello_1.0-1_amd64```

Now build the deb pkg by:

``` dpkg-deb --build --root-owner-group <helloworld_1.0-1_amd64>```

To install run:

```sudo dpkg -i <package>```

To remove run:

```sudo dpkg -r <appname>``` where the appname is the name defined in control package name.

To check if it is properly removed type:
```dpkg -l | grep <appname>```


# Reference

https://www.internalpointers.com/post/build-binary-deb-package-practical-guide
