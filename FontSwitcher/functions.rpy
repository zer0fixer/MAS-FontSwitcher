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
            "label": sizes["label"]
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
            "label": 0
        }

        FS_monika_restart()

    # Restart the game by setting a flag and quitting Ren'Py.
    def FS_monika_restart():
        persistent.closed_self = True
        renpy.quit()

    # Load fonts data from JSON files in the designated folder.
    def FS_load_fonts():
        game_dir = os.path.join(renpy.config.basedir, "game")
        submods_dir_name = "submods"
        
        # Check for "Submods" (capitalized) as some users might have it this way.
        if not os.path.isdir(os.path.join(game_dir, submods_dir_name)):
            if os.path.isdir(os.path.join(game_dir, "Submods")):
                submods_dir_name = "Submods"

        json_folder = os.path.join(game_dir, submods_dir_name, "FontSwitcher", "json")

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
            with open(filepath) as file:
                json_data = json.load(file)
            fonts_data.update(json_data)

        return fonts_data

    def FS_reset_bars():
        persistent._temp_additional_["default"] = 0
        persistent._temp_additional_["options"] = 0
        persistent._temp_additional_["quick_menu"] = 0
        persistent._temp_additional_["label"] = 0

    def FS_adjust_size(key, amount, original_size):
        # Define a safe minimum font size to prevent text from becoming unreadable.
        MIN_FONT_SIZE = 8

        current_value = persistent._temp_additional_[key]
        new_value = current_value + amount
        # Ensure the final font size does not fall below the minimum.
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
                "label": 0
            }
    
    check_and_reset_font_settings()