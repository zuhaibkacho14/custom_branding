# Dynamic White-Label Branding Manager

Dynamic white-label branding for Odoo 18 login, backend, website, and email surfaces.

## Features

- Centralized branding configuration from the Odoo admin interface.
- Dynamic logo, favicon, brand name, website link, login title, and footer text updates.
- Enabled/disabled per surface configuration.
- Compatible backend and frontend asset hooks.
- No standard Odoo source modification required.

## Module structure

- `ws_dynamic_branding/__init__.py`
- `ws_dynamic_branding/__manifest__.py`
- `ws_dynamic_branding/models/__init__.py`
- `ws_dynamic_branding/models/res_config_settings.py`
- `ws_dynamic_branding/controllers/__init__.py`
- `ws_dynamic_branding/controllers/main.py`
- `ws_dynamic_branding/data/res_config_settings.xml`
- `ws_dynamic_branding/static/src/js/ws_dynamic_branding.js`
- `ws_dynamic_branding/static/src/xml/ws_dynamic_branding.xml`
- `ws_dynamic_branding/static/src/scss/ws_dynamic_branding.scss`

## Installation

1. Place the module in your Odoo addons path.
2. Restart the Odoo server.
3. Update apps and install `Dynamic White-Label Branding Manager`.
4. Open Settings > General Settings > Branding Settings.
5. Configure brand name, logos, colors, and supported surfaces.
6. Save the settings and refresh the browser to view the live branding.

## Notes

This module is designed to work against the standard Odoo 18 configuration architecture and dynamic frontend assets. Actual template selectors and supported branding surfaces may vary with individual Odoo installations, website themes, and custom modules. This is meant as a maintainable, dynamic implementation and should be validated against the live environment before declaring all locations fully production-ready.
