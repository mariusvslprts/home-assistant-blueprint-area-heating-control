# Home Assistant Blueprint: Area Heating Control

Area based heating control blueprint for Home Assistant. 

This blueprint is based on Home Assistants [Area Model](https://www.home-assistant.io/docs/organizing/areas/) and 
discovers devices & sensors based on the provided area.

**Features:**
- 🗓️ Heating sheduler support
- 🌱 Eco + 🛋️ comfort temperature settings (built-in or external entities)
- 🕵️ Entity auto discovery (thermostats + themperature sensors + window sensors) based on area
- ⚙️ Thermostat calibration (requires external temperature sensors)
- 🪟 Window open detection to stop heating while windows are open (requires window sensors)
- 👥 Person detection (uses eco temperature instead of comfort temperature when nobody is at home)
- 🚶 Presence detection (allows to overrides person detection status when a presence sensor provided)
- ♨️ Central heating system status support (disables automation while your central heating system is off)
- ⚔️ Liming protection to prevent your trvs from sticking

> [!IMPORTANT]
> Areas must have at least one `climate` entity assinged in order to get displayed in the area selection.
> Make sure you have assigned your thermostats & window sensors before using this blueprint.

## Installation

To create Automations based on this Blueprint use the following button to import the Blueprint into your Home Assistant instance:

[![my-homeassistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fmariusvslprts%2Fhome-assistant-blueprint-area-heating-control%2Fblob%2Fmain%2Farea-heating-control.yaml)

or follow the official Home Assistant documentation [Importing Blueprints](https://www.home-assistant.io/docs/automation/using_blueprints/#importing-blueprints) and use the following url: 

```
https://github.com/mariusvslprts/home-assistant-blueprint-area-heating-control/blob/main/area-heating-control.yaml
```

## Documentation

Coming soon...


## Support

Feel free to open an Issue or make a Pull Request if you find any bugs or have ideas on how to optimize the the blueprint. 

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/A0A71PVJ28)

