from odoo import fields, models

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'


    #Secuencia
    sequence = fields.Integer(
        required=True,
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
