# DatapackModinator
*(Doofenshmirtz voice) Behold, the DatapackModinator!*

A small tool to package Minecraft datapacks and/or resource packs into a single mod file that works on both Fabric and Forge.

Simply place your data and assets folders into the same directory as the python file and the `settings.toml` file, then run the python file.

If you don't happen to have Python installed on your computer, you can head to the [Releases](https://github.com/T0RNATO/datapackmodinator/releases/latest) tab and get the exe that is functionally identical. (Tested only on Windows.)

Note: exe is currently broken, please give me 12 business hours :P

## Settings
This is an example `settings.toml` file. All mod info keys are required and should be changed. Paths are optional in case you want to have the program copy the datapack and/or resource pack from elsewhere.
```toml
[mod_info]
# The internal mod id, used for referencing the mod in code. a-z, 0-9, and _ only.
id = "mymod"
# The name of the mod as it will appear in the mod manager.
display_name = "My Mod"
# The version of the mod. This is used for updating mods and should probably use semver.
version = "1.0.0"
# A list of authors/contributors.
authors = ["My Name"]
# A short description of the mod.
description = "My Mod Description"
# The license of the mod. If unsure, use MIT or The Unlicense.
license = "MIT"
# Forge loader version, because forge can't just support MC version numbers.
# For reference, 40 is 1.18, 43 is 1.19.2, and 47 is 1.20.1
# I will assume it supports versions newer than this as well.
forge_version = 47

# Paths are from the directory from which this is run. These keys are optional.
[paths]
assets = "assets/"
data = "data/"
icon = "icon.png"
```
