# Terminator with Distrobox Setup

## Creating a Shortcut
First, it will be needed to add a shortcut to open a distrobox specific image. Lets example it by a ubuntu_jazzy image using `Ctrl + Alt + R`.

1. Go to Ubuntu Settings
2. Navigate to Keyboard section
3. Click + to add new shortcut
4. Configure as:
   - Name: `Open Distrobox Ubuntu Jazzy`
   - Command: `terminator -p ubuntu_jazzy_profile`.
   (The profile name should be defined in the terminator configuration. See Section 2)
   - Shortcut: Press `Ctrl + Alt + R`

Now the shortcut will open the terminal in distrobox context.

## 2. Configuring the Terminator
Configure Terminator by editing its config file:
```bash
gedit ~/.config/terminator/config
```

Create a profile `default` for host context and a new one for a specific distrobox image context. In the example below, an Ubuntu ROS2 Jazzy context was created. Different background colors were set to differentiate the terminals:

```
[global_config]
  suppress_multiple_term_dialog = True
  always_split_with_profile = True
[keybindings]
[profiles]
  [[default]]
    cursor_color = "#aaaaaa"
    scrollback_infinite = True
    copy_on_selection = True
  [[ubuntu_jazzy_profile]]
    background_color = "#282A36" # Different color to identify
    use_custom_command = True
    custom_command = distrobox-enter ubuntu_jazzy
[layouts]
  [[default]]
    [[[window0]]]
      type = Window
      parent = ""
    [[[child1]]]
      type = Terminal
      parent = window0
[plugins]
```

## Usage
- Open normal terminal: Launch Terminator
- Open distrobox: `Ctrl + Alt + R`
- Split horizontally: `Ctrl + Shift + O`
- Split vertically: `Ctrl + Shift + E`
- Switch terminals: `Alt + Arrows`

The configuration above provides:
- Default profile for host system
- Distrobox profile with custom appearance
- Automatic profile inheritance when splitting terminals
- Infinite scrollback history
- Auto-copy on selection
