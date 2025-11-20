<p align="center">
  <img src="https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/ecafaae0-acfc-4105-a5a0-2d5c5864e2c5">
</p>

<div align="center">
  <p>
    <a href="https://github.com/zer0fixer/MAS-FontSwitcher/stargazers">
      <img src="https://img.shields.io/github/stars/zer0fixer/MAS-FontSwitcher?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=C9CBFF&labelColor=302D41" alt="stars" />
    </a>&nbsp;&nbsp;
    <a href="https://github.com/zer0fixer/MAS-FontSwitcher/commits/main/">
      <img src="https://img.shields.io/github/last-commit/zer0fixer/MAS-FontSwitcher?style=for-the-badge&logo=github&logoColor=eba0ac&label=Last%20Commit&labelColor=302D41&color=eba0ac" alt="Last Commit" />
    </a>&nbsp;&nbsp;
    <a href="https://github.com/zer0fixer/MAS-FontSwitcher/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/zer0fixer/MAS-FontSwitcher?style=for-the-badge&logo=appveyor&label=Latest%20Release&labelColor=302D41&color=f9e2af" />
    </a>
  </p>
</div>

A submod that adds a simple way to add new fonts to Monika After Story so you can give it your personal touch.

## Features
- Replaces the font in the Monika After Story mod.
- **(New!)** An updated, cleaner UI that moves the font list to a separate window.
- **(New!)** A new 'Size+' menu to adjust font size (min. 8) and padding directly in-game.
- **(New!)** State-aware buttons (Apply, Update, Reset) that dim when no changes are pending.
- **(New!)** Now supports cross-platform (Windows, Mac, Linux).
- It has change levels (Low, Medium, High) in case the user does not want to saturate the interface.
- This submod is compatible with Comfy UI.
- It has a preview so that the user can see the font type before applying the changes.
  
## Preview submod
| Before | After | Comfy UI |
| ------- | ------- | ------- |
| ![Holi](https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/4602cc56-a6d4-4fec-96d3-f7be56c05508) | ![lmao](https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/f21de1f0-ebea-483f-9340-0fadb11b2e50) | ![Holi](https://github.com/zer0fixer/MAS-FontSwitcher/assets/94260040/a2940cb6-49f2-461d-a722-53d3ab9c6a1c) |

## Installation
- Download the latest version of the submod, unzip the zip file and paste it into the `submods` folder.

## How to add new fonts
You can easily add your own fonts:
1. **Place your font file (e.g., MyFont.ttf, MyFont.otf) inside the submods/FontSwitcher/font folder.**
2. **Create a new .json file (e.g., MyFont.json) inside the submods/FontSwitcher/json folder.
You can use this example as a template for your new JSON file.**


#### Example:
```yaml
{    # ↓ This is the font ID, it has to be unique.
    "cupcake": {
        "name": "Natsuki's handwriting",  # ← Font name, it is recommended to keep it short to avoid screen saturation.
        "font_default": "Nat.ttf",  # ← Path of the main font (New method: just the filename!) (Game Text, Dialogue).
        "font_label": "Nat.ttf",  # ← Path of the label font (New method: just the filename!) (General Titles).
        "font_button": "Nat.ttf",  # ← Path of the button font (New method: just the filename!) (Options).
        "size_default": 26,  # ← Applies the size of the main font.
        "size_button": 26,  # ← Applies the font size of the buttons.
        "size_quick": 18,  # ← The size of the quick menu (History, Skip, Auto, Save, Load, Settings).
        "size_label": 32, # ← It is the size of the titles (Preferences, Navigation, Game Menu).
        "padding": 3 # ← This is used to adjust the position and size of the button content. Therefore you will use it in some fonts where it is necessary to modify the padding.
    }
}
```

**Note (Backward Compatibility):**

This new version simplifies paths. You only need the filename (e.g., "Nat.ttf") as long as the font is in the font/ folder.
Don't worry! If you added custom fonts using the old method (e.g., "font_default": "submods/FontSwitcher/font/Comfortaa.ttf"), the submod is fully backward compatible with the old path format, so no changes are necessary.
