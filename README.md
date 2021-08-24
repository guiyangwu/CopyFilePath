# Copy Path Info
Add "**Copy Relative Path**", "**Copy File Name Only**", and "**Copy Git Path**" commands to the Sublime Text right-click context menu.
- **Copy Relative Path**: copy the file path of the currently opened file relative to the folder you have open with the greatest path match.
- **Copy File Name Only**: copy the file name only (path is excluded)
- **Copy Git Path**: copy the relative git path (git repo name is excluded) to the git repo which contains the file. If no git repo, abstract file path will be copied.

# Install to Sublime Text as plugin
1. Download this repo and unzip it
2. Copy the repo folder into Sublime Text directory under: .../Data/Packages/
3. Open one source file in Sublime Text and right click to select new commands

# Adding a Hotkey
     {"keys": ["ctrl+shift+r"], "command": "copy_relative_path"},
     {"keys": ["ctrl+shift+c"], "command": "copy_git_path"},
     {"keys": ["ctrl+shift+f"], "command": "copy_file_name_only"},
