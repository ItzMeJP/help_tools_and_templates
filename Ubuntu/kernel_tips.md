# Kernel Tips

Kernel configurations are useful when a new computer is configured or new driver installed.

It is possible to configure once per boot or definitively:

* **Once**: just in grub go to Ubuntu option and press "e". Set the parameters and press ctrl-x. These configuration will be applied in the current boot.
* **Definitively**: edit the /etc/default/grub file. Then, ``` sudo update-grub``` and restart.

# Some usefull parameters:

* **nomodeset**:

  The newest kernels have moved the video mode setting into the kernel. So all the programming of the hardware specific clock rates and registers on the video card happen in the kernel rather than in the X driver when the X server starts.. This makes it possible to have high resolution nice looking splash (boot) screens and flicker free transitions from boot splash to login screen. Unfortunately, on some cards this doesn't work properly and you end up with a black screen. Adding the nomodeset parameter instructs the kernel to not load video drivers and use BIOS modes instead until X is loaded.

* **quiet splash**:

  The splash (which eventually ends up in your /boot/grub/grub.cfg ) causes the splash screen to be shown.

  At the same time you want the boot process to be quiet, as otherwise all kinds of messages would disrupt that splash screen.

  Although specified in GRUB these are kernel parameters influencing the loading of the kernel or its modules, not something that changes GRUB behaviour. The significant part from GRUB_CMDLINE_LINUX_DEFAULT is CMDLINE_LINUX

* **acpi, noapic and nolapic**:

    In general, such boot parameters are not needed unless there is a problem with your BIOS and how it handles these standards, or it just might be old enough where these standards were not fully implemented properly.

    ACPI (Advanced Configuration and Power Interface) is a standard for handling power management. Older systems may not support ACPI full, so sometimes it helps to give the kernel a hint to not use it. "acpi=off"

    APIC (Advanced Programmable Interrupt Controller) is a kind of feature found on newer systems. The "local" version is called "LAPIC". What this controller can do is be set up to generate and handle interrupts, a signal the hardware uses to pass messages. Again, some implementations of APIC can have problems on older system, and so it is useful to disable it. "noapic" and "nolapic".

    Sometimes the APIC is working, but it slows things down by getting in the middle of messages being passed around. This can mess with audio and video processing, for example. Folks might disable it for that reason as well.

For more parameters descriptions, check [this](https://www.kernel.org/doc/html/v4.14/admin-guide/kernel-parameters.html).

## Helping debug kernel problems
The [dmesg](https://man7.org/linux/man-pages/man1/dmesg.1.html) command allows to get the log text from the kernel boot.

The

The example bellow will retrieve the current boot(-b-0) log. The integer number just the define which boot tentative the log is related, i.e., the pneultimate will be -b-1 :

```sudo journalctl -b-0 >journal.txt ```
