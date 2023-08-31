init -1 python:
    # Apply the selected font style and trigger a game restart.
    def FS_apply_style():

        if is_font_available(FS_font_switcher[FS_temp_font_]["font_default"]) == False:
            FS_get_data = FS_font_switcher["justmonika"]

        persistent._font_settings_ = {
            "id": FS_temp_font_,
            "name": FS_get_data["name"],
            "applied": True
        }

        FS_monika_restart()

    # Reset font style settings to default and trigger a game restart.
    def FS_reset_style():
        persistent._font_settings_ = {
            "id": "justmonika",
            "name": "Inactive",
            "applied": False
        }
        FS_monika_restart()

    # Restart the game by setting a flag and quitting Ren'Py.
    def FS_monika_restart():
        persistent.closed_self = True
        renpy.quit()

    # Load fonts data from JSON files in the designated folder.
    def FS_load_fonts():
        json_folder = os.path.join(renpy.config.basedir, "game", "submods", "FontSwitcher", "json")

        try:
            json_files = [os.path.join(json_folder, filename) for filename in os.listdir(json_folder) if filename.endswith('.json')]
        except OSError:
            return {
                "justmonika": {
                    "name": "Monika",
                    "font_default": "mod_assets/font/m1_fixed.ttf",
                    "font_label": "mod_assets/font/m1_fixed.ttf",
                    "font_button": "mod_assets/font/m1_fixed.ttf",
                    "size_default": 27,
                    "size_button": 27,
                    "quick_size": 14,
                    "padding": 3,
                    "description": "I'm glad to see you here, [player]~"
                }
            }

        fonts_data = {}

        for filepath in json_files:
            with open(filepath) as file:
                json_data = json.load(file)
            fonts_data.update(json_data)

        return fonts_data