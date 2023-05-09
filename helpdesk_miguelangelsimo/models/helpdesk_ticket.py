from odoo import fields, models

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
        # relation='helpdesk_ticket_tag_rel',
        # column1='ticket_id',
        # column2='tag_id',
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