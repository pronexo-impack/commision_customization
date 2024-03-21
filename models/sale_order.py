from odoo import models


class SaleOrderExtended(models.AbstractModel):
    _inherit = "sale.order"

    def changeClient05(self):
        all_records = self.env["sale.order"].search([])

        if all_records:
            for rec in all_records:
                if rec.partner_id.agent_ids:
                    rec.write({"partner_id": rec.partner_id.id})
