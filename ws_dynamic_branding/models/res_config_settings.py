from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ws_brand_name = fields.Char(
        string='Brand name',
        config_parameter='ws_dynamic_branding.brand_name',
        default='Odoo',
    )
    ws_brand_short_name = fields.Char(
        string='Short brand name',
        config_parameter='ws_dynamic_branding.brand_short_name',
        default='Odoo',
    )
    ws_brand_website = fields.Char(
        string='Brand website URL',
        config_parameter='ws_dynamic_branding.brand_website',
        default='https://www.example.com',
    )
    ws_brand_footer_text = fields.Char(
        string='Footer text',
        config_parameter='ws_dynamic_branding.brand_footer_text',
        default='Powered by Odoo',
    )
    ws_brand_login_title = fields.Char(
        string='Login title',
        config_parameter='ws_dynamic_branding.brand_login_title',
        default='Welcome back',
    )
    ws_brand_login_subtitle = fields.Text(
        string='Login description',
        config_parameter='ws_dynamic_branding.brand_login_subtitle',
        default='Log in to continue to your workspace.',
    )
    ws_brand_primary_color = fields.Char(
        string='Primary brand color',
        config_parameter='ws_dynamic_branding.brand_primary_color',
        default='#875A7B',
    )
    ws_brand_logo = fields.Binary(
        string='Brand logo',
        config_parameter='ws_dynamic_branding.brand_logo',
    )
    ws_brand_login_logo = fields.Binary(
        string='Login logo',
        config_parameter='ws_dynamic_branding.brand_login_logo',
    )
    ws_brand_backend_logo = fields.Binary(
        string='Backend logo',
        config_parameter='ws_dynamic_branding.brand_backend_logo',
    )
    ws_brand_favicon = fields.Binary(
        string='Favicon',
        config_parameter='ws_dynamic_branding.brand_favicon',
    )
    ws_enable_backend_branding = fields.Boolean(
        string='Enable backend branding',
        config_parameter='ws_dynamic_branding.enable_backend_branding',
        default=True,
    )
    ws_enable_login_branding = fields.Boolean(
        string='Enable login branding',
        config_parameter='ws_dynamic_branding.enable_login_branding',
        default=True,
    )
    ws_enable_portal_branding = fields.Boolean(
        string='Enable portal branding',
        config_parameter='ws_dynamic_branding.enable_portal_branding',
        default=True,
    )
    ws_enable_email_branding = fields.Boolean(
        string='Enable email branding',
        config_parameter='ws_dynamic_branding.enable_email_branding',
        default=True,
    )

    @api.model
    def _get_branding_value(self, key, default=''):
        return self.env['ir.config_parameter'].sudo().get_param(key, default) or default

    @api.model
    def _get_branding_image(self, key):
        value = self._get_branding_value(key, '')
        if not value:
            return False
        return value

    @api.model
    def get_branding_data(self):
        return {
            'brand_name': self._get_branding_value('ws_dynamic_branding.brand_name', 'Odoo'),
            'brand_short_name': self._get_branding_value('ws_dynamic_branding.brand_short_name', 'Odoo'),
            'brand_website': self._get_branding_value('ws_dynamic_branding.brand_website', 'https://www.example.com'),
            'brand_footer_text': self._get_branding_value('ws_dynamic_branding.brand_footer_text', 'Powered by Odoo'),
            'brand_login_title': self._get_branding_value('ws_dynamic_branding.brand_login_title', 'Welcome back'),
            'brand_login_subtitle': self._get_branding_value('ws_dynamic_branding.brand_login_subtitle', 'Log in to continue to your workspace.'),
            'brand_primary_color': self._get_branding_value('ws_dynamic_branding.brand_primary_color', '#875A7B'),
            'brand_logo': self._get_branding_image('ws_dynamic_branding.brand_logo'),
            'brand_login_logo': self._get_branding_image('ws_dynamic_branding.brand_login_logo'),
            'brand_backend_logo': self._get_branding_image('ws_dynamic_branding.brand_backend_logo'),
            'brand_favicon': self._get_branding_image('ws_dynamic_branding.brand_favicon'),
            'enable_backend_branding': self._get_branding_value('ws_dynamic_branding.enable_backend_branding', 'True') == 'True',
            'enable_login_branding': self._get_branding_value('ws_dynamic_branding.enable_login_branding', 'True') == 'True',
            'enable_portal_branding': self._get_branding_value('ws_dynamic_branding.enable_portal_branding', 'True') == 'True',
            'enable_email_branding': self._get_branding_value('ws_dynamic_branding.enable_email_branding', 'True') == 'True',
        }
