# Configurting GeForce 3060+ on Ubuntu20

Before boot, include the nomodeset in kernel parameter. Check [this](kernel_tips.md).

Check if the driver is already installed (normally it is included in the kernel of Ubuntu20). For this, go to Software & Updates > Additional Drivers. Selecte the proprietary, tested nvidia driver 470.

Now, disable the secure mode. One way to do it is described [here](#tag)

Reboot.


Maybe the HDMI will not be loaded by the kernel. The error can be checked by [dmesg or journalctl](kernel_tips.md) commands.

Therefore, add permanently in /etc/defaul/grub the parameter ```pci=realloc```, e.g.

```
GRUB_CMDLINE_LINUX_DEFAULT="pci=realloc"
```

Update the file by:

```
sudo update-grub
```

Reboot the system.

It is possible that Ubuntu gets stuck in the splash purple window sometimes or constantly. This issue is related to the [display server communication protocol](https://linuxconfig.org/how-to-enable-disable-wayland-on-ubuntu-20-04-desktop). Therefor disable Wayland protocol, to force Xorg.
```
sudo atom /etc/gdm3/custom.conf
```

Setting Wayland disable by (removing the comment tag...):
```
WaylandEnable=false
```

Then, reboot the system.

## <a name="tag"></a> Setting "unsecure mode"


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
