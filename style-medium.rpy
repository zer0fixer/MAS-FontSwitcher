init 1000:
    if persistent._font_settings_["applied"] and (
            persistent._font_switcher_change == "medium" or
            persistent._font_switcher_change == "high"):

        #===========================================================================================
        # Talk menu
        #===========================================================================================

        style talk_choice_button:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style talk_choice_button_dark:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style talk_choice_button_text:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        style talk_choice_button_text_dark:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        #===========================================================================================
        # Menu dialogue
        #===========================================================================================

        style choice_button:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style choice_button_dark:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style mas_dlg_menu_button_text:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        style mas_dlg_menu_button_text_dark:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        #===========================================================================================
        # Scrollable menu
        #===========================================================================================

        style scrollable_menu_button:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style scrollable_menu_button_dark:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style scrollable_menu_button_text:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        style scrollable_menu_button_text_dark:
            font    font_switcher_button_font
            size    font_switcher_button_text_size



        #===========================================================================================
        # Two-pane scrollable menu
        #===========================================================================================
        
        style twopane_scrollable_menu_button:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style twopane_scrollable_menu_button_dark:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style twopane_scrollable_menu_button_text:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        style twopane_scrollable_menu_button_text_dark:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        #===========================================================================================
        # Hkb menu
        #===========================================================================================

        style hkb_button:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style hkb_button_dark:
            top_padding    font_switcher_padding
            bottom_padding font_switcher_padding

        style hkb_button_text:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        style hkb_button_text_dark:
            font    font_switcher_button_font
            size    font_switcher_button_text_size

        #===========================================================================================
        # Extras menu
        #===========================================================================================

        style mas_adjustable_button_text:
            font    font_switcher_custom
            size    font_switcher_button_text_size

        style mas_adjustable_button_text_dark:
            font    font_switcher_custom
            size    font_switcher_button_text_size

        #===========================================================================================
        # Input
        #===========================================================================================

        style input_prompt:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        style input:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        #===========================================================================================
        # Frames
        #===========================================================================================
        
        style confirm_prompt_text:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        style confirm_prompt_text_dark:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        style confirm_button_text:
            font    font_switcher_custom
            size    font_switcher_default_text_size

