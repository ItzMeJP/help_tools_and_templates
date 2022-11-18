It is easier to make the changes in Linux and hence I’ll recommend going with the second method.

Ubuntu and most other Linux distributions use systemd these days and hence you can use timedatectl command to change the settings.

What you are doing is to tell your Linux system to use the local time for the hardware clock (RTC). You do that with the set-local-rtc (set local time for RTC) option:

```timedatectl set-local-rtc 1 ```

As you can notice in the command below, the RTC now uses the local time.

```timedatectl ```

Now if you boot into Windows, it takes the hardware clock to be as local time which is actually correct this time. When you boot into Linux, your Linux system knows that the hardware clock is using local time, not UTC. And hence, it doesn’t try to add the off-set this time.

This fixes the time difference issue between Linux and Windows in dual boot.

You see a warning about not using local time for RTC. For desktop setups, it should not cause any issues. At least, I cannot think of one.

I hope I made things clear for you. If you still have questions, please leave a comment below.


# Reference
https://itsfoss.com/wrong-time-dual-boot/
