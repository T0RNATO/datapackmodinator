import tomllib
import json
import os
from zipfile import ZipFile

with open("settings.toml", "rb") as f:
    settings = tomllib.load(f)

def format(text, *codes):
    out = ""
    for code in codes:
        out += f"\033[{code}m"
    return out + text + "\033[0m"

def add_folder_to_zip(zipf, folder_path, arcname):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.join(arcname, os.path.relpath(file_path, folder_path)))
            count += 1
    return count

expected_keys = ["id", "version", "display_name", "description", "authors", "license", "forge_version"]

info = settings["mod_info"]
paths = settings["paths"]

missing_keys = [key for key in info.keys() if key not in expected_keys]

if len(missing_keys) > 0:
    print(format(f"Missing keys in settings: {', '.join(missing_keys)}", 91))
    input("Press enter to exit...")

with ZipFile("mod.jar", "w") as z:
    icon = "icon" in paths and os.path.isfile(paths["icon"])

    # Fabric
    z.writestr("fabric.mod.json", json.dumps({
        "schemaVersion": 1,
        "id": info["id"],
        "version": info["version"],
        "name": info["display_name"],
        "description": info["description"],
        "authors": info["authors"],
        "license": info["license"],
        **({"icon": "icon.png"} if icon else {}),
    }))

    # Forge
    z.writestr("META-INF/mods.toml", f"""
        modLoader="lowcodefml"
        loaderVersion="[{info['forge_version']},)"
        
        license="{info['license']}"
        
        [[mods]]
        modId="{info['id']}"
        version="{info['version']}"
        displayName="{info['display_name']}"
        authors="{', '.join(info['authors'])}"
        description="{info['description']}"
        {'logoFile="icon.png"' if icon else ''}
    """)

    try:
        z.write(paths["icon"], "icon.png")
        print("Added icon")
    except KeyError:
        pass
    except FileNotFoundError:
        print(format("Icon not found at provided path.", 93))

    try:
        print(f"Added {add_folder_to_zip(z, paths['data'], 'data')} datapack files")
    except KeyError:
        pass
    except FileNotFoundError:
        print(format("Datapack files not found at provided path.", 93))

    try:
        print(f"Added {add_folder_to_zip(z, paths['assets'], 'assets')} resource pack files")
    except KeyError:
        pass
    except FileNotFoundError:
        print(format("Resource pack files not found at provided path.", 93))

    print(format("Done! Mod created at mod.jar", 92))

z.close()
input("Press enter to exit...")

