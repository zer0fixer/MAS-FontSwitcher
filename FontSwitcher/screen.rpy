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

        # Display selected font's name.
        label _("Font : {0}").format(persistent._font_settings_["name"]):
            xpos 0.3

        null height 10

        # Sort and display font options in groups of four.
        $ font_keys = sorted(FS_font_switcher.keys(), key=lambda k: FS_font_switcher[k]["name"])

        for i in range(0, len(font_keys), 4):
            hbox:
                spacing 10
                for j in range(i, min(i+4, len(font_keys))):
                    $ key = font_keys[j]
                    $ font_name = FS_font_switcher[key]["name"]

                    # Button to select a font.
                    textbutton _(font_name):
                        action SetField(store, "FS_temp_font_", key)
                        hovered tooltip.Action(FS_font_switcher[key]["description"])
                        selected FS_temp_font_ == key
                        
            null height 10

        null height 10

        # Buttons for applying, disabling, previewing, and restarting font changes.
        hbox:
            spacing 10

            textbutton _("Apply"):
                style "navigation_button"
                action Show(screen="dialog", message="To apply the changes, the game will be closed.\nFont to apply : {0}\nLevel of change : {1}".format(
                    FS_font_switcher[FS_temp_font_]["name"], persistent._font_switcher_change.capitalize()),
                    ok_action=Function(FS_apply_style))
                
            textbutton _("Disable"):
                style "navigation_button"
                action Show(screen="dialog", message="Disabling has been successful.\nThe game will now be closed.",
                            ok_action=Function(FS_reset_style))
                sensitive persistent._font_settings_["applied"]

            textbutton _("Preview"):
                style "navigation_button"
                action Function(renpy.call_in_new_context, '_fs_preview')
                hovered tooltip.Action("Here is a preview of the font you want to apply.")

            null height 20

            hbox:
                spacing 10

                # Options for font switcher range.
                $ font_switcher_options = [
                    ("Low", "Apply a minimum change."),
                    ("Medium", "Applies balanced changes."),
                    ("High", " Applies changes to the entire interface (Except for: Check Button).")
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
        temp_padding = font_settings["padding"]
        size_default = font_settings["size_default"]
        size_button = font_settings["size_button"]
        quick_size = font_settings["quick_size"]
        path_default = font_settings["font_default"]
        path_label = font_settings["font_label"]
        path_button = font_settings["font_button"]
        preview_text = "Just click on the textbox or anywhere on the screen to exit the preview.\n1 2 3 4 5 6 7 8 9 0 ! ? _ . , : ;"
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

# Overlay screen for font preview.
screen fake_overlay():
    zorder 50

    vbox:
        style_prefix "check"
        xpos 0.050
        ypos 0.0
        label "{font=[path_label]}Note:{/font}"
        text "{size=[size_default]}{font=[path_default]}Just Monika\nUse fonts that are legible.{/font}{/size}" outlines [(2, "#808080", 0, 0)]

    vbox:
        style_prefix "hkb"
        xpos 0.05
        yanchor 1.0
        ypos 715

        for button_text in ["Talk", "Extra", "Music", "Play"]:
            textbutton "{size=[size_button]}{font=[path_button]}[button_text]{/font}{/size}":
                padding(temp_padding, temp_padding)
                action NullAction()

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
            textbutton "{size=[size_button]}{font=[path_button]}[_menu]{/font}{/size}":
                padding(temp_padding, temp_padding)
                action Return()

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
            textbutton "{size=[quick_size]}{font=[path_button]}[_quick]{/font}{/size}":
                action Return()

