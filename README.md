# Copy Path Info
Add "**Copy Relative Path**", "**Copy File Name Only**", and "**Copy Git Path**" commands to the Sublime Text right-click context menu of one File Tab.
- **Copy Relative Path**: copy the file path of the currently opened file relative to the folder you have open with the greatest path match. Example: "myrepo/src/XXX.c"
- **Copy File Name Only**: copy the file name only (path is excluded). Example: "XXX.c"
- **Copy Git Path**: copy the relative git path (git repo name is excluded) to the git repo which contains the file. If no git repo, abstract file path will be copied. **Copy Git Path always return Linux like path with '/' as seperator**. Example: "src/XX.c"

Note: the example full path is "/home/thomas/code/myrepo/src/XXX.c" (or Windows like path "D:\home\thomas\code\myrepo\src\XXX.c") and open folder by Sublime Text from "/home/thomas/code", myrepo is git repo name.

# Install to Sublime Text as plugin
1. Download this repo and unzip it
2. Copy the repo folder into Sublime Text directory under: .../Data/Packages/
3. Open one source file in Sublime Text and right click one file tab to select new commands

# Adding Hotkeys
     {"keys": ["ctrl+shift+r"], "command": "copy_relative_path"},
     {"keys": ["ctrl+shift+c"], "command": "copy_git_path"},
     {"keys": ["ctrl+shift+f"], "command": "copy_file_name_only"},
