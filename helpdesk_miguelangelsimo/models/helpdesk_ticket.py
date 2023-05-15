from odoo import api, Command, fields, models, _
from odoo.exceptions import UserError

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'


    #Secuencia
    sequence = fields.Integer(
        default=10,
        help="Secuencia para el orden de las incidencias."
    )

    # Nombre
    name = fields.Char(
        required=True,
        help="Resume en pocas palabras un titulo para la incidencia"
    )

    # Descripción
    description = fields.Text(
        help="Escribe detalladamente la incidencia y como replicarla",
        default="""


        """
    )

    # Fecha
    date = fields.Date()

    # Fecha y hora limite
    date_limit = fields.Datetime(
        string = 'Limit date & Time')
    
    person_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[('is_company', '=', False)],)
    
    # Asignado (Verdadero o Falso)
    assigned = fields.Boolean(
        readonly=True,
    )

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to')
    
    color = fields.Integer('Color Index', default=0)

    amount_time = fields.Float(
        string='Amount of time'
    )

    # Acciones a realizar (html)
    actions_todo = fields.Html()

    # Añadir el campo Estado [Nuevo, asignado, En proceso, pendiente, resuleto, cancelado], que por defecto sea nuevo
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('assigned', 'Assigned'),
            ('in_process', 'In Process'),
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('canceled', 'Canceled'),
        ],
        default="new",
    
    )
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
       
    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()
    
   # def update_description(self):
   #     self.ensure_one() #solo para un registro
   #     self.description = "ok"
    #def update_description(self):
    #   for record in self:
    #   self.description = "ok"

   # def update_all_description(self):
    #    self.ensure_one()
    #    all_tickets = self.env['helpdesk.ticket'].search([])
    #    all_ticket.update_description()

    
    
    assigned = fields.Boolean(
        compute='_compute_assigned', # Hacer que el campo assigned sea calculado,
        search='_search_assigned',# Hacer que se pueda buscar con el atributo search y hacer que se pueda modificar de forma que si lo marco se actualice el usuario con el usuario conectado y si lo desmarco se limpie el campo del usuario.
        inverse='_inverse_assigned',

    )

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)
    
    def _search_assigned(self, operator, value):
        if operator not in ('=', '!=') or not isinstance(value, bool):
            raise UserError( ("Operation not supported"))
        if operator == '=' and value == True:
            operator = '!='
            #value = false
        else:
            operator = '='
            #value = false
        return [('user_id', operator, False)] # false es value pero directamente asignado a false
    
    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user

# hacer un campo calculado que indique, dentro de un ticket, la cantidad de tiquets asociados al mismo ususario.
    tickets_count = fields.Integer(
        compute='_compute_tickets_count',
        string='Tickets count',
    )

    @api.depends('user_id')
    def _compute_assigned(self):
        ticket_obj = self.env['helpdesk.ticket']
        for record in self:
            tickets = ticket_obj.search([('user_id', '=', record.user_id.id)])
            record.tickets_count = len(tickets)

 # crear un campo nombre de etiqueta, y hacer un botón que cree la nueva etiqueta con ese nombre y lo asocie al ticket.
    tag_name = fields.Char()

    def create_tag(self):
        self.ensure_one()
       #self.write({'tag_ids': [(0,0, {'name': self.tag_name})]})#esta es la forma antigua de hacerlo antes de la version 15      
        self.write({'tag_ids': [Command.create({'name': self.tag_name})]}) #esta es la forma de hacerlo a partir de la version 15
    
    def clear_tags(self):
        self.ensure_one()
        #self.write({'tag_ids': [(5,0,0)]})#esta es la forma antigua de hacerlo antes de la version 15 
        tag_ids = self.env['helpdesk.ticket.tag'].search([('name', '=', 'otra')]) #
        self.tag_ids = [Command.clear(),Command.set(tag_ids.ids)] #Esta es la foma actual de borrar y añador una nueva etiqueta llamada "otra"
