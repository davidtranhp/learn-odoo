from odoo import http


class Main(http.Controller):
    
    @http.route('/academy/academy', auth='public')
    def index(self, **kwargs):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('viindoo_academy.index', {
            'teachers': Teachers.sudo().search([])
            })
