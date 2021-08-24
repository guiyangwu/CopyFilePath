# Copy File Path
Adds a "Copy Relative Path", "Copy Git Path" and "Copy File Name Only" commands to 
the Sublime Text right-click context menu, which copies the file path of the currently
opened file relative to the folder you have open with the greatest path match.

# Sublime Text plugin

## Adding a Hotkey
     {"keys": ["ctrl+shift+r"], "command": "copy_relative_path"},
     {"keys": ["ctrl+shift+c"], "command": "copy_git_path"},
     {"keys": ["ctrl+shift+f"], "command": "copy_file_name_only"},
