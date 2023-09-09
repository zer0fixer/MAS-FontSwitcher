#====Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="ZeroFixer",
        name="Font Switcher",
        description="Easily change the font with a simple process. Github repository: {a=https://github.com/zer0fixer/MAS-FontSwitcher}{i}{u}here{/u}{/i}{/a}",
        version="1.0.1",
        settings_pane="_font_switcher_submod"
    )

#====Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Font Switcher",
            user_name="zer0fixer",
            repository_name="MAS-FontSwitcher",
            redirected_files=(
                "README.md"
            )
        )
