# Potato Or Not — Foundry VTT 14 community update

Community update of [Potato Or Not](https://github.com/fantasycalendar/FoundryVTT-PotatoOrNot), originally developed by **Wasp** and **Fantasy Computerworks**. The original project and its translators deserve credit for the code and localization files retained here. This update is independently maintained and is not an official release from the original developers.

This release targets Foundry VTT 14 and dnd5e 6.0.6. It changes Foundry's client graphics settings and does not read or modify dnd5e data. Choose one of three presets from the module's settings menu. New users can be prompted when they join.

## Changes (26 October 2026)

- Updated initialization for Foundry 14 and retained the ApplicationV2 dialog.
- Apply only core settings registered by the running Foundry version; skip settings that are absent.
- Avoid repeating unchanged setting writes and record the applied preset only after updates finish.
- Removed bundled third-party image assets from this community package. The selection dialog now uses a text symbol.
- Retained the upstream GNU GPL v3 license and original author attribution.

## Install and publish

The GitHub repository should contain `module.json` at its root. To install manually, copy these files into `{Foundry user data}/Data/modules/potato-or-not/` and enable the module in a world.

The [HackANurse fork](https://github.com/HackANurse/FoundryVTT-PotatoOrNot) builds and publishes its release through `.github/workflows/main.yml`. The release package includes only the module source files listed in `scripts/build-release.py`; original image assets in the fork are excluded. The first release is tagged `v0.6.0-v14.1`. Once published, install it with `https://github.com/HackANurse/FoundryVTT-PotatoOrNot/releases/latest/download/module.json`.

For a manual rebuild, run `POTATO_OR_NOT_REPO=HackANurse/FoundryVTT-PotatoOrNot python3 scripts/build-release.py` from the repository root and upload `dist/module.json` and `dist/module.zip` to a matching GitHub release.

## License and credits

This modified version is distributed under **GNU GPL v3**; see [LICENSE](LICENSE). The source code for this release must remain available under GPL v3 when redistributed. The original code and translations come from [fantasycalendar/FoundryVTT-PotatoOrNot](https://github.com/fantasycalendar/FoundryVTT-PotatoOrNot), which credits Wasp as author and Fantasy Computerworks as the project creator. Changes made on 26 October 2026 are listed above.

This package was checked with local automated tests. A live Foundry VTT 14 / dnd5e 6.0.6 session was not available, so the compatibility declaration should be confirmed in a running world before publishing a release as verified.
