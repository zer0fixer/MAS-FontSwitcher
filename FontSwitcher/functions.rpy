init -1 python:
    # Apply the selected font style and trigger a game restart.
    def FS_apply_style():
        FS_get_data = FS_font_switcher[FS_temp_font_]
        persistent._font_switcher_change = font_switcher_temp_change
        persistent._font_settings_ = {
            "id": FS_temp_font_,
            "name": FS_get_data["name"],
            "applied": True
        }
        
        sizes = persistent._temp_additional_
        persistent.fs_additional_size = {
            "default": sizes["default"],
            "options": sizes["options"],
            "quick_menu": sizes["quick_menu"],
            "label": sizes["label"],
            "padding": sizes["padding"]
        }

        FS_monika_restart()

    # Reset font style settings to default and trigger a game restart.
    def FS_reset_style():
        persistent._font_settings_ = {
            "id": "justmonika",
            "name": "Inactive",
            "applied": False
        }

        persistent.fs_additional_size = {
            "default": 0,
            "options": 0,
            "quick_menu": 0,
            "label": 0,
            "padding": 0
        }

        FS_monika_restart()

    # Restart the game by setting a flag and quitting Ren'Py.
    def FS_monika_restart():
        persistent.closed_self = True
        renpy.quit()

    def _normalize_path(path):
        """
        Normalizes a path by replacing backslashes with forward slashes for
        cross-platform compatibility.
        """
        return path.replace("\\", "/")

    def _get_submod_dir(submod_name):
        """
        Gets the directory for a given submod, handling case variations
        for the 'submods' directory.
        """
        game_dir = _normalize_path(renpy.config.basedir)
        submods_dir = os.path.join(game_dir, "game", "submods")
        if not os.path.isdir(submods_dir):
            submods_dir = os.path.join(game_dir, "game", "Submods")

        return _normalize_path(os.path.join(submods_dir, submod_name))

    # Load fonts data from JSON files in the designated folder.
    def FS_load_fonts():
        fontswitcher_abs_path = _get_submod_dir("FontSwitcher")
        json_folder = os.path.join(fontswitcher_abs_path, "json")

        try:
            json_files = [os.path.join(json_folder, filename) for filename in os.listdir(json_folder) if filename.endswith('.json')]
        except OSError:
            return {
                "justmonika": {
                    "name": "Just Monika",
                    "font_default": "mod_assets/font/m1_fixed.ttf",
                    "font_label": "mod_assets/font/m1_fixed.ttf",
                    "font_button": "mod_assets/font/m1_fixed.ttf",
                    "size_default": 27,
                    "size_button": 27,
                    "size_quick": 14,
                    "size_label": 34,
                    "padding": 3
                }
            }

        fonts_data = {}

        for filepath in json_files:
            with open(filepath, 'r') as f:
                json_data = json.load(f)
            fonts_data.update(json_data)

        # Determine the relative path for fonts to handle submods/Submods casing
        game_dir = _normalize_path(renpy.config.gamedir)
        fontswitcher_rel_path = _normalize_path(os.path.relpath(fontswitcher_abs_path, game_dir))

        for font_info in fonts_data.values():
            for key in ["font_default", "font_label", "font_button"]:
                if key in font_info:
                    font_path = font_info[key]
                    if "submods/" not in font_path.lower() and "mod_assets/" not in font_path.lower():
                        # Build the path using os.path.join for consistency
                        full_path = os.path.join(fontswitcher_rel_path, "font", font_path)
                        # Normalize for Ren'Py which uses forward slashes
                        font_info[key] = _normalize_path(full_path)

        return fonts_data

    def FS_reset_bars():
        persistent._temp_additional_["default"] = 0
        persistent._temp_additional_["options"] = 0
        persistent._temp_additional_["quick_menu"] = 0
        persistent._temp_additional_["label"] = 0
        persistent._temp_additional_["padding"] = 0

    def FS_adjust_size(key, amount, original_size):
        current_value = persistent._temp_additional_[key]
        new_value = current_value + amount

        # For padding, allow negative values without a minimum limit.
        if key == "padding":
            persistent._temp_additional_[key] = new_value
        # For font sizes, ensure they don't fall below a minimum readable size.
        else:
            MIN_FONT_SIZE = 8
            if (original_size + new_value) >= MIN_FONT_SIZE:
                persistent._temp_additional_[key] = new_value

init 1 python:
    # Function to verify and reset the configuration
    def check_and_reset_font_settings():
        selected_key = persistent._font_settings_["id"]

        if selected_key not in store.FS_font_switcher:
            persistent._font_settings_ = {
                "id": "justmonika",
                "name": "Inactive",
                "applied": False
            }
            persistent.fs_additional_size = {
                "default": 0,
                "options": 0,
                "quick_menu": 0,
                "label": 0,
                "padding": 0
            }
    
    # Migration function to ensure 'padding' key exists in persistent data
    def _fs_migrate_persistent_data():
        # For users updating, this ensures the 'padding' key is added to existing persistent data
        if "padding" not in persistent.fs_additional_size:
            persistent.fs_additional_size["padding"] = 0
        if "padding" not in persistent._temp_additional_:
            persistent._temp_additional_["padding"] = 0

    _fs_migrate_persistent_data()
    check_and_reset_font_settings()
