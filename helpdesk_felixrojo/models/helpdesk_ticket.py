from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    name = fields.Char(
        string='Name',
        required=True)
    description = fields.Text(
        string='Description')
    date = fields.Date(
        string='Date')

    #Estado, por defecto nuevo
    state = fields.Selection(
        [('nuevo', 'Nuevo'),
         ('asignado', 'Asignado'),
         ('proceso', 'En Proceso'),
         ('pendiente', 'Pendiente'),
         ('resuelto', 'Resuelto'),
         ('cancelado', 'Cancelado')],
        string='State',
        default='nuevo')
    
    #Tiempo en horas
    time = fields.Float(
        string='Time')
    
    #Asignado
    assigned = fields.Boolean(
        string='Assigned',
        readonly='True')
    
    #Fecha limite
    date_limit = fields.Date(
        string='Date Limit')

    # Accion correctiva html
    action_corrective = fields.Html(
        string='Corrective Action',
        help='Describe corrective actions to do')
    
    # Accion preventiva html
    action_preventive = fields.Html(
        string='Preventive Action',
        help='Describe preventive actions to do')
    
    