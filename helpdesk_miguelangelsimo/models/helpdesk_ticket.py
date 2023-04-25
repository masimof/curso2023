from odoo import fields, models

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'


    # Nombre
    name = fields.Char(
        required=True,
        help="Resume en pocas palabras un titulo para la incidencia"
    )

    # Descripción
    description = fields.Text(
        help="Escribe detalaldamente la incidencia y como replicarla",
        default="""


        """
    )

    # Fecha
    date = fields.Date()

    # Fecha y hora limite
    date_limit = fields.Datetime(
        string = 'Limit date & Time')
    
    # Asignado (Verdadero o Falso)
    assigned = fields.Boolean()

    # Acciones a realizar (html)
    actions_todo = fields.Html()
