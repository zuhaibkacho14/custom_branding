from odoo import http
from odoo.http import request


class BrandingController(http.Controller):

    @http.route('/ws_dynamic_branding/branding_data', type='json', auth='public', methods=['GET'], csrf=False, sitemap=False)
    def branding_data(self):
        return request.env['res.config.settings'].sudo().get_branding_data()
