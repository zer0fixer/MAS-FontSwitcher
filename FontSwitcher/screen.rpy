#===========================================================================================
# Screen Base
#===========================================================================================

# This screen handles font switching settings.
screen _font_switcher_submod():
    $ tooltip = renpy.get_screen("submods", "screens").scope["tooltip"]

    vbox:
        style_prefix "check"
        box_wrap False
        xfill True
        xmaximum 1000
        null height 10

        hbox:
            text _("{b}Select your favorite font : {/b}")
            # Dropdown-style button to select a font
            textbutton FS_font_switcher[FS_temp_font_]["name"]:
                style "navigation_button"
                action Show("_fs_font_selection")
                yalign 0.9
                hovered tooltip.Action("Click to choose a different font.")

        null height 10

        # Buttons for applying, disabling, previewing, and restarting font changes.
        hbox:
            spacing 10
            
            python:
                # Determine if we are just refreshing sizes or applying a new font
                is_refresh_scenario = (
                    persistent._font_settings_["applied"] and
                    FS_temp_font_ == persistent._font_settings_["id"]
                )

                if is_refresh_scenario:
                    apply_button_text = "Update"
                    apply_message = "To apply the new size and padding values, the game will close."
                    hovered_message = "Don't like the font size and padding? Update the values you have selected!"
                    # The button is sensitive only if the temporary adjustments are different from the applied ones.
                    is_button_sensitive = (persistent._temp_additional_ != persistent.fs_additional_size)
                else:
                    apply_button_text = "Apply"
                    apply_message = "To apply the changes, the game will be closed.\nFont to apply : {0}\nLevel of change : {1}".format(
                        FS_font_switcher[FS_temp_font_]["name"], font_switcher_temp_change.capitalize())
                    hovered_message = "Before applying a font, it is recommended that you preview how it will look and then apply it."
                    # The "Apply" button is always sensitive if it's not a refresh scenario.
                    is_button_sensitive = True

                disable_message = "Font disabled : {}\nThe game will now be closed.".format(persistent._font_settings_["name"])

            textbutton _(apply_button_text):
                style "navigation_button"
                action Show("dialog", message=apply_message, ok_action=Function(FS_apply_style))
                sensitive is_button_sensitive
                hovered tooltip.Action(hovered_message)
            
            textbutton _("Disable"):
                style "navigation_button"
                action Show("dialog", message=disable_message, ok_action=Function(FS_reset_style))
                sensitive persistent._font_settings_["applied"]
                hovered tooltip.Action("Disable your current font.")

            textbutton _("Preview"):
                style "navigation_button"
                action Function(renpy.call_in_new_context, '_fs_preview')
                hovered tooltip.Action("Here is a preview of the font you want to apply.")

            textbutton _("- Size +"):
                style "navigation_button"
                action Show("font_size_settings")
                hovered tooltip.Action("Reduce or increase the default font size.")

            null height 20

            hbox:
                spacing 10

                # Options for font switcher range.
                $ font_switcher_options = [
                    ("Low", "Apply a minimum change (Textbox)."),
                    ("Medium", "Applies balanced changes (Textbox + Buttons)."),
                    ("High", " Applies changes to the entire interface (Except for : Check Button).")
                ]

                for option_label, option_tooltip in font_switcher_options:
                    textbutton _(option_label):
                        action SetField(store, "font_switcher_temp_change", option_label.lower())
                        hovered tooltip.Action(option_tooltip)
                        selected font_switcher_temp_change == option_label.lower()

#===========================================================================================
# Preview
#===========================================================================================
# Label to display font preview.
label _fs_preview:
    hide monika
    python:
        disable_esc()
        mas_MUMURaiseShield()
        font_settings = FS_font_switcher[FS_temp_font_]
        temp_padding = font_settings["padding"]
        size_default = font_settings["size_default"] + persistent._temp_additional_["default"]
        size_button = font_settings["size_button"] + persistent._temp_additional_["options"]
        size_quick = font_settings["size_quick"] + persistent._temp_additional_["quick_menu"]
        size_label = font_settings["size_label"] + persistent._temp_additional_["label"]

        path_default = font_settings["font_default"]
        path_label = font_settings["font_label"]
        path_button = font_settings["font_button"]
        preview_text = "Just click on the textbox or anywhere on the screen to exit the preview.\n1 2 3 4 5 6 7 8 9 0 ! ? ~ _ . , : ;"
        fake_name = "{size=[size_default]}{font=[path_default]}Name{/font}{/size}"

    # Show font preview overlay.
    show screen fake_quick_menu
    show screen fake_overlay
    fake_name "{size=[size_default]}{font=[path_default]}[preview_text]{/font}{/size}"
    show monika
    python:
        enable_esc()
        mas_MUMUDropShield()
    hide screen fake_quick_menu
    hide screen fake_overlay
    return

# Screen to act as a dropdown menu for font selection
screen _fs_font_selection():
    modal True
    zorder 200

    style_prefix "confirm"
    add mas_getTimeFile("gui/overlay/confirm.png")

    frame:
        has vbox
        
        label _("Select a Font!"):
            xalign 0.5

        null height 15

        viewport:
            scrollbars "vertical"
            mousewheel True
            ymaximum 400
            xmaximum 780

            vbox:
                style_prefix "check"
                spacing 10
                xminimum 700
                $ font_keys = sorted(FS_font_switcher.keys(), key=lambda k: FS_font_switcher[k]["name"])
                for key in font_keys:
                    $ font_name = FS_font_switcher[key]["name"]
                    textbutton _(font_name):
                        action [SetField(store, "FS_temp_font_", key), Hide("_fs_font_selection")]
                        xalign 0.0
                        xfill True
                        selected FS_temp_font_ == key

        null height 15
        textbutton _("Close"):
            xalign 0.5
            action Hide("_fs_font_selection")

# Overlay screen for font preview.
screen fake_overlay():
    zorder 50

    vbox:
        style_prefix "check"
        xpos 0.050
        ypos 0.0
        label "{size=[size_label]}{font=[path_label]}Note:{/font}{/size}"
        text "{size=[size_default]}{font=[path_default]}Just Monika.\n\nUse fonts that are legible.\n\nYou can add your own fonts.{/font}{/size}" outlines [(2, "#808080", 0, 0)]

    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 715

        for button_text in ["Talk", "Extra", "Music", "Play"]:
            textbutton _("{size=[size_button]}{font=[path_button]}[button_text]{/font}{/size}") action NullAction()

    vbox:
        style_prefix "talk_choice"
        $ items = [
            "Bookmarks",
            "Hey, {0}...".format(m_name),
            "Repeat conversation",
            "I love you!",
            "I feel...",
            "Goodbye",
            "Nevermind"
        ]

        for _menu in items:
            textbutton _("{size=[size_button]}{font=[path_button]}[_menu]{/font}{/size}") action Return()

screen fake_quick_menu():
    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 0.995

        $ items = [
            "History",
            "Skip",
            "Auto",
            "Save",
            "Load",
            "Settings"
        ]

        for _quick in items:
            textbutton _("{size=[size_quick]}{font=[path_button]}[_quick]{/font}{/size}") action Return()

# Reusable screen for size adjustment controls (+/- buttons)
screen _fs_size_adjuster(key, name, original_size):
    hbox:
        xfill True
        spacing 15
        align (0.5, 0.5)

        # Label for the setting
        text "{0}".format(name):
            text_align 0.0
            xsize 250

        hbox:
            spacing 30
            align (1.0, 0.5)

            # Decrease button
            textbutton _("-"):
                style "navigation_button"
                action Function(FS_adjust_size, key=key, amount=-1, original_size=original_size)

            # Current size display
            if key == "padding":
                text _("Space : {0}".format(persistent._temp_additional_[key] + original_size)):
                    text_align 0.5
                    xsize 150
            else:
                text _("Size : {0}".format(persistent._temp_additional_[key] + original_size)):
                    text_align 0.5
                    xsize 150

            # Increase button
            textbutton _("+"):
                style "navigation_button"
                action Function(FS_adjust_size, key=key, amount=1, original_size=original_size)

screen font_size_settings():
    modal True

    zorder 200

    style_prefix "confirm"
    add mas_getTimeFile("gui/overlay/confirm.png")

    frame:
        vbox:
            style_prefix "check"
            xmaximum 600
            ymaximum 600
            xfill True
            spacing 5
            
            python:
                font_settings = FS_font_switcher[FS_temp_font_]
                keys_to_adjust = ["default", "options", "quick_menu", "label", "padding"]
                    
                name_to_adjust = ["Default", "Options", "Quick Menu", "Navigation", "Padding"]

                original_sizes = [font_settings["size_default"], font_settings["size_button"], font_settings["size_quick"], font_settings["size_label"], font_settings.get("padding", 0)]

                # Check if there are any changes to reset
                has_changes_to_reset = any(persistent._temp_additional_.values())

            label _("Font : {0}".format(font_settings["name"])):
                xalign 0.5

            null height 15

            for key, name, size in zip(keys_to_adjust, name_to_adjust, original_sizes):
                # Use the reusable screen component
                use _fs_size_adjuster(key=key, name=name, original_size=size)
                null height 10

            hbox:
                style_prefix "confirm"
                # This button resets the size adjustments to 0, and is only sensitive if there are changes.
                textbutton _("Reset") action Function(FS_reset_bars) sensitive has_changes_to_reset

            hbox:
                xalign 0.5
                style_prefix "confirm"
                textbutton _("Close") action Hide("font_size_settings")