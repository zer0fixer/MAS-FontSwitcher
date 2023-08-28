init 1000:
    if (persistent._font_settings_["applied"] and persistent._font_switcher_change == "high"):
        python:
            """
            Change the font and size of the text for the characters that do not use a style:
                Calendar
                Basic Text
                NOU
                Pong
                Search Box
                Render Menu
                (It also affects the styles that use both variables.)
            """
            gui.default_font = font_switcher_custom
            gui.text_size = font_switcher_default_text_size

        #===========================================================================================
        # Music menu
        #===========================================================================================

        ## Music menu button
        style music_menu_button_text:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        style music_menu_button_text_dark:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        #===========================================================================================
        # Notify
        #===========================================================================================

        style notify_text:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        #===========================================================================================
        # NOU
        #===========================================================================================

        style nou_text:     
            font    font_switcher_button_font
            size    font_switcher_default_text_size

        style nou_text_dark:
            font    font_switcher_button_font
            size    font_switcher_default_text_size
            
        #===========================================================================================
        # Island buttons
        #===========================================================================================

        style island_button_text:
            font    font_switcher_button_font
            size    font_switcher_default_text_size

        style island_button_text_dark:
            font    font_switcher_button_font
            size    font_switcher_default_text_size

        #===========================================================================================
        #Game menu
        #===========================================================================================

        ## Title
        style game_menu_label_text:
            font    font_switcher_label_font

        style game_menu_label_text_dark:
            font    font_switcher_label_font

        ## Preference label
        style pref_label_text:
            font    font_switcher_label_font

        style pref_label_text_dark:
            font    font_switcher_label_font

        ## Version text
        style main_menu_version:
            font    font_switcher_custom
            size    font_switcher_menu_font_size

        style main_menu_version_dark:
            font    font_switcher_custom
            size    font_switcher_menu_font_size

        ## Menu text
        style navigation_button_text:
            font    font_switcher_label_font

        style navigation_button_text_dark:
            font    font_switcher_label_font

        ## File text
        style page_label_text:
            font    font_switcher_custom

        style page_label_text_dark:
            font    font_switcher_custom

        style page_button_text:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        style page_button_text_dark:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        ## Slot text
        style slot_time_text:
            font    font_switcher_custom

        style slot_time_text_dark:
            font    font_switcher_custom

        style slot_name_text:
            font    font_switcher_custom

        style slot_name_text_dark:
            font    font_switcher_custom

        ## Radio text
        style radio_button_text:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        style radio_button_text_dark:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        #===========================================================================================
        # History
        #===========================================================================================

        ## Name
        style history_name_text:
            font    font_switcher_custom
            size    font_switcher_default_text_size

        ## Text
        style history_text:
            font    font_switcher_custom
            size    font_switcher_default_text_size