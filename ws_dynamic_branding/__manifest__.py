{
    'name': 'Dynamic White-Label Branding Manager',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Centralized dynamic branding for Odoo login, backend, portal, and email surfaces',
    'license': 'LGPL-3',
    'author': 'WS',
    'website': 'https://www.example.com',
    'depends': ['base', 'web'],
    'data': [
        'data/res_config_settings.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ws_dynamic_branding/static/src/js/ws_dynamic_branding.js',
            'ws_dynamic_branding/static/src/xml/ws_dynamic_branding.xml',
            'ws_dynamic_branding/static/src/scss/ws_dynamic_branding.scss',
        ],
        'web.assets_frontend': [
            'ws_dynamic_branding/static/src/js/ws_dynamic_branding.js',
            'ws_dynamic_branding/static/src/xml/ws_dynamic_branding.xml',
            'ws_dynamic_branding/static/src/scss/ws_dynamic_branding.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
