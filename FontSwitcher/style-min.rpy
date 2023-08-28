init 1000:
    if persistent._font_settings_["applied"] and (
            persistent._font_switcher_change == "low" or
            persistent._font_switcher_change == "medium" or
            persistent._font_switcher_change == "high"):
    
        #===========================================================================================
        # Dialogue (Textbox)
        #===========================================================================================

        ## Name
        style say_label:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        style say_label_dark:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        ## Text
        style normal:
            font    font_switcher_custom
            size    font_switcher_default_text_size
            yoffset -5

        ## Quick button
        style quick_button_text:
            font    font_switcher_custom
            size    font_switcher_quick_size

        style quick_button_text_dark:
            font    font_switcher_custom
            size    font_switcher_quick_size
