from odoo import http


class Main(http.Controller):

    @http.route('/academy/academy', auth='public', website=True)
    def index(self, **kwargs):
        Teachers = http.request.env['academy.teachers']
        
        return http.request.render(
            'viindoo_academy.index',
            {
                'teachers': Teachers.search([])
                }
            )

    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher3(self, teacher):
        return http.request.render('viindoo_academy.biography', {
            'person': teacher
        })
