from odoo import models, fields, api, _

class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Action'

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Ticket')
    
class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Tag'

    name = fields.Char()
    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tags')

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags')

    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')

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
        compute='_compute_assigned')    
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
    
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to')
    
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
    
    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = self.user_id and True or False
    
    #campo calculado que dentro de un ticket indica los tickets asociados a un usuario
    ticket_qty = fields.Integer(
        string='Ticket Qty',
        compute='_compute_ticket_qty')
    
    @api.depends('user_id')
    def _compute_ticket_qty(self):
        for record in self:
            other_tickets = self.env['helpdesk.ticket'].search([('user_id', '=', record.user_id.id)])
            record.ticket_qty = len(other_tickets)
    
    #crear un campo nombre con etiqueta, hacer boton que cree la etiqueta con nombtre y asocie a ticket
    tag_name = fields.Char(
        string='Tag Name')
    
    def create_tag(self):
        self.ensure_one()
        #opcion 1
        self.write({
            'tag_ids': [(0,0, {'name': self.tag_name})]
        })
        #opcion 2
        #tag = self.env['helpdesk.ticket.tag'].create({
        #    'name': self.tag_name
        #})
        #self.write({
        #    'tag_ids': [(4,tag.id, 0)]
        #})
        #opcion 3
        #tag = self.env['helpdesk.ticket.tag'].create({
        #    'name': self.tag_name,
        #    'ticket_ids': [(6, 0, tag.ids)]
        #})
        #opcion 4
        #tag = self.env['helpdesk.ticket-tag'].create([
        #    'name': self.tag_name,
        #    'ticket_ids': [(6, 0, self.ids)]
        #])
        self.tag_name = False