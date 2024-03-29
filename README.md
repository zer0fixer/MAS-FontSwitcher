<p align="center">
  <img src="https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/ecafaae0-acfc-4105-a5a0-2d5c5864e2c5">
</p>

<p align="center">
<a href="https://github.com/zer0fixer/MAS-FontSwitcher/releases/latest">
  <img alt="Latest release" src="https://img.shields.io/github/v/release/zer0fixer/MAS-FontSwitcher?style=for-the-badge&logo=appveyor">
</a>
</p>

It is a submod that adds a simple way to add new fonts to Monika After Story so you can give it your personal touch.

## Features
- Replaces the font type of the `Monika After Story mod`.
- It has levels of change in case the user does not want to saturate the interface.
- This submod is compatible with `Comfy UI`.
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
