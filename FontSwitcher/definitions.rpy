#===========================================================================================
# Variables
#===========================================================================================
## Stores applied font data
define 3 FS_get_key = JS_font_switcher[persistent._font_settings_["id"]]

# Default font settings
default persistent._font_settings_ = {
    "id": "justmonika",
    "name": "Inactive",
    "applied": False
}

# Define font groups for different character sets
define 10 font_switcher_custom = FontGroup().add(
    font_switcher_default_font, 0x0020, 0x00ff  # Custom characters
    ).add(
        "mod_assets/font/SourceHanSansK-Regular.otf", 0xac00, 0xd7a3  # Korean characters
    ).add(
        "mod_assets/font/SourceHanSansSC-Regular.otf", 0x4e00, 0x9faf  # Simplified Chinese characters
    ).add(
        "mod_assets/font/mplus-2p-regular.ttf", 0x3000, 0x4dff  # Japanese + other characters
    ).add(
        "gui/font/Aller_Rg.ttf", 0x0000, 0xffff  # Latin-1 characters
)

# Load font switcher data
define JS_font_switcher = FS_load_fonts()

# Default font switcher change setting
default persistent._font_switcher_change = "medium"

# Default temp font
default 5 FS_temp_font_ = persistent._font_settings_["id"]

# Save the temp font switcher change setting
default 5 font_switcher_temp_change = persistent._font_switcher_change

# Define various font-related variables
define 5 font_switcher_default_font = FS_get_key["font_default"]
define 5 font_switcher_label_font = FS_get_key["font_label"]
define 5 font_switcher_button_font = FS_get_key["font_button"]
define 5 font_switcher_padding = FS_get_key["padding"]

define 5 font_switcher_default_text_size = FS_get_key["size_default"]
# define 5 font_switcher_label_text_size = FS_get_key["size_label"]
define 5 font_switcher_button_text_size = FS_get_key["size_button"]
define font_switcher_quick_size = FS_get_key["quick_size"]


# define font_switcher_label_text_size = 35
define font_switcher_menu_font_size = 16
