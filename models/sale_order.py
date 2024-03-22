from odoo import models


class SaleOrderExtended(models.AbstractModel):
    _inherit = "sale.order"

    def changeClient05(self):
        all_records = self.env["sale.order"].search([])

        if all_records:
            for rec in all_records:
                if rec.partner_id.agent_ids:
                    if rec.invoice_ids:  ##* SI TIENE UNA FACTURA RELACIONADA CAMBIA LOS AGENTES COMISIONADOS DE ESA FACTURA
                        for m in rec.invoice_ids:
                            m.write({"partner_id": m.partner_id.id})
                    rec.write({"partner_id": rec.partner_id.id})
