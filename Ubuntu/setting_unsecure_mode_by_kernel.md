## Setting "unsecure mode"


If you want get rid of the message about Insecure Boot you need to enable secure boot. To do this you need turn on validation in module MOK (Machine Owner Key):

```
sudo mokutil --enable-validation
```

You will be asked to enter twice temporary password and than after reboot get a possibility to change validation state.

If validation is enabled than no more message about insecure boot appears. But remember, you will not be able to run any unsigned drivers: nVidia drivers and VirtualBox will not be working.

To disable validation type:

```
sudo mokutil --disable-validation
```

and then reboot.

If you disable validation and have in BIOS Secure Boot switched ON, still you will not be able to boot anything that wasn't signed. Even though your ubuntu has validation disable but "is seen" by BIOS (UEFI) as signed because of shim-signed package. Shim package while your ubuntu is booting checks what is the MOK state and if validation is disabled shows message "Booting in insecure mode".
