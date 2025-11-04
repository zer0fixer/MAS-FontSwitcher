<p align="center">
  <img src="https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/ecafaae0-acfc-4105-a5a0-2d5c5864e2c5">
</p>

<div align="center">
  <p>
    <a href="https://github.com/zer0fixer/MAS-FontSwitcher/stargazers">
      <img src="https://img.shields.io/github/stars/zer0fixer/MAS-FontSwitcher?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=C9CBFF&labelColor=302D41" alt="stars" />
    </a>&nbsp;&nbsp;
    <a href="https://github.com/zer0fixer/MAS-FontSwitcher/commits/main/">
      <img src="https://img.shields.io/github/last-commit/zer0fixer/MAS-Extraplus?style=for-the-badge&logo=github&logoColor=eba0ac&label=Last%20Commit&labelColor=302D41&color=eba0ac" alt="Last Commit" />
    </a>&nbsp;&nbsp;
    <a href="https://github.com/zer0fixer/MAS-FontSwitcher/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/zer0fixer/MAS-Extraplus?style=for-the-badge&logo=appveyor&label=Latest%20Release&labelColor=302D41&color=f9e2af" />
    </a>
  </p>
</div>

It is a submod that adds a simple way to add new fonts to Monika After Story so you can give it your personal touch.

## Features
- Replaces the font in the Monika After Story mod.
- (New!) An updated, cleaner UI that moves the font list to a separate window.
- (New!) A new 'Size+' menu to adjust font size (min. 8) and padding directly in-game.
- (New!) State-aware buttons (Apply, Update, Reset) that dim when no changes are pending.
- (New!) Now supports cross-platform (Windows, Mac, Linux).
- It has change levels (Low, Medium, High) in case the user does not want to saturate the interface.
- This submod is compatible with Comfy UI.
- It has a preview so that the user can see the font type before applying the changes.
  
## Preview submod
| Before | After | Comfy UI |
| ------- | ------- | ------- |
| ![Holi](https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/4602cc56-a6d4-4fec-96d3-f7be56c05508) | ![lmao](https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/f21de1f0-ebea-483f-9340-0fadb11b2e50) | ![Holi](https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/a2940cb6-49f2-461d-a722-53d3ab9c6a1c) |

## Installation
- Download the latest version of the submod, unzip the zip file and paste it into the `submods` folder.

## Fonts
To add and share more fonts, you can use JSON files.
For more convenience, there will be a JSON template so you can edit it.
Click ![Here!](https://github.com/zer0fixer/resource-repository/blob/main/Template.json)

#### Example:
```yaml
{    # ↓ This is the font ID, it has to be unique.
    "justmonika": {
        "name": "Monika's handwriting",  # ← Font name, it is recommended to keep it short to avoid screen saturation.
        "font_default": "mod_assets/font/m1_fixed.ttf",  # ← Path of the main font (Game Text, Dialogue).
        "font_label": "mod_assets/font/m1_fixed.ttf",  # ← Path of the label font (General Titles).
        "font_button": "mod_assets/font/m1_fixed.ttf",  # ← Path of the button font (Options).
        "size_default": 28,  # ← Applies the size of the main font.
        "size_button": 28,  # ← Applies the font size of the buttons.
        "size_quick": 20,  # ← The size of the quick menu (History, Skip, Auto, Save, Load, Settings).
        "size_label": 34, # ← It is the size of the titles (Preferences, Navigation, Game Menu).
        "padding": 3 # ← This is used to adjust the position and size of the button content. Therefore you will use it in some fonts where it is necessary to modify the padding.
    }
}
```
**Note: It is possible to place and define the path to a font outside the folder of this submod, but it is not recommended unless it is a Monika After Story font. It is recommended to be inside the font folder in "submods/FontSwitcher/font" and the JSON is mandatory to be in "submods/FontSwitcher/json".**
