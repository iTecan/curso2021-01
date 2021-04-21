from odoo import models, api, fields, _

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    name = fields.Char(
        string='Name',
        required=True)
    description = fields.Text(
        string='Description',
        translate= True)
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
    
    
    #Cambiar estado a asignado, visible solo con estado=nuevo
    def asignar(self):
        self.ensure_one()
        self.write({
            'state': 'asignado',
            'assigned': True})
    
    def proceso(self):
        self.ensure_one()
        self.state = 'proceso'

    def pendiente(self):
        self.ensure_one()
        self.state = 'pendiente'

    def resuelto(self):
        self.ensure_one()
        self.state = 'resuelto'

    def cancelado(self):
        self.ensure_one()
        self.state = 'cancelado'