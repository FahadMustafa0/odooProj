# -*- coding: utf-8 -*-
# from odoo import http


# class Openacado(http.Controller):
#     @http.route('/openacado/openacado/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacado/openacado/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacado.listing', {
#             'root': '/openacado/openacado',
#             'objects': http.request.env['openacado.openacado'].search([]),
#         })

#     @http.route('/openacado/openacado/objects/<model("openacado.openacado"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacado.object', {
#             'object': obj
#         })
