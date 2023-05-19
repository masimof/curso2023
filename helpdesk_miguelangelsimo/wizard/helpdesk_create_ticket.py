from odoo import models, api, fields, _


# - Crear un asistente para crear tickets desde la etiqueta
#   - que coja por contexto el active_id para que el ticket creado tenga asociada la etiqueta desde la que se lanza el asistente
#   - crear el boton en el formulario de la etiqueta
#   - después de crear el ticket redirigir al formulario con el ticket creado
class helpdeskCreateTicket(models.TransientModel):
    _name = 'helpdesk.create.ticket'
    _description = 'Create Ticket'

    tag_id = fields.Many2one(
        'helpdesk.ticket.tag', 
         string='Tag', 
         required=True,
         default=lambda self: self.env.context.get('active_id')
         )
    name = fields.Char(string='Subject', required=True)
    description = fields.Text(string='Description', required=True)

    def create_ticket(self):
        ticket = self.env['helpdesk.ticket'].create({
            'name': self.name,
            'description': self.description,
            'tag_ids': [(4,self.tag_id.id)],
        })
        return {
            'name': _('Ticket'),
            'view_mode': 'form',
            'res_model': 'helpdesk.ticket',
            'res_id': ticket.id,
            'type': 'ir.actions.act_window',
        }