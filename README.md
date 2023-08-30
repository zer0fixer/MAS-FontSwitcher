<p align="center">
  <img src="https://github.com/Zero-Fixer/MAS-FontSwitcher-EN/assets/142945683/6caa8b59-7e67-4def-a440-7f086255da72">
</p>

<p align="center">
<a href="https://github.com/Zero-Fixer/MAS-FontSwitcher-EN/releases/latest">
  <img alt="Latest release" src="https://img.shields.io/github/v/release/zer0fixer/MAS-Extraplus?style=for-the-badge&logo=appveyor">
</a>
</p>

It is a submod that adds a simple way to add new fonts to Monika After Story so you can give it your personal touch

## Preview of a font
| Before | After |
| ------- | ------- |
| ![Holi](https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/4602cc56-a6d4-4fec-96d3-f7be56c05508) | ![lmao](https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/f1bafe56-62ff-4470-a5ca-ca52b6b1eb52) |

## Fonts
To add and share more fonts, you can use JSON files.
For more convenience, there will be a JSON template so you can edit it.
Click ![Here!](https://github.com/zer0fixer/resource-repository/blob/main/Template.json)

#### Example:
```yaml
{    # ↓ This is the font ID, it has to be unique
    "justmonika": {
        "name": "Monika's handwriting",  # ← Font name, it is recommended to keep it short to avoid screen saturation.
        "font_default": "mod_assets/font/m1_fixed.ttf",  # ← Path of the main font (Game Text, Dialogue).
        "font_label": "mod_assets/font/m1_fixed.ttf",  # ← Path of the label font (General Titles).
        "font_button": "mod_assets/font/m1_fixed.ttf",  # ← Path of the button font (Options).
        "size_default": 27,  # ← Applies the size of the main font.
        "size_button": 27,  # ← Applies the font size of the buttons.
        "padding": 3, # ← This is used to adjust the position and size of the button content. Therefore you will use it in some fonts where it is necessary to modify the padding.
        "description": "How's your day going, player?"  # ← You can add a small description about the font or something else but in moderation.
    }
}
```
