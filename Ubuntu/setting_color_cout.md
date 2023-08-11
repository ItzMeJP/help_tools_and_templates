

You need to output ANSI color codes. Note that not all terminals support this; if color sequences are not supported, garbage will show up.

Example:

 cout << "\033[1;31mbold red text\033[0m\n";

Here, \033 is the ESC character, ASCII 27. It is followed by [, then zero or more numbers separated by ;, and finally the letter m. The numbers describe the color and format to switch to from that point onwards.

The codes for foreground and background colours are:

         foreground background
black        30         40
red          31         41
green        32         42
yellow       33         43
blue         34         44
magenta      35         45
cyan         36         46
white        37         47

Additionally, you can use these:

reset             0  (everything back to normal)
bold/bright       1  (often a brighter shade of the same color)
underline         4
inverse           7  (swap foreground and background colors)
bold/bright off  21
underline off    24
inverse off      27

See the table on Wikipedia for other, less widely supported codes.

To determine whether your terminal supports colour sequences, read the value of the TERM environment variable. It should specify the particular terminal type used (e.g. vt100, gnome-terminal, xterm, screen, ...). Then look that up in the terminfo database; check the colors capability.
