# Copyright 2014-2022 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models
from odoo.exceptions import ValidationError

class CommissionMixinExtended(models.AbstractModel):
    _inherit = "commission.mixin"
    #   _name = "commission.mixin.extended"

    def _prepare_agent_vals(self, agent):
        return {"agent_id": agent.id, "commission_id": agent.commission_id.id}

    def _prepare_agent_vals_commission05(self, agent, commission_id):
        return {"agent_id": agent.id, "commission_id": commission_id}

    def _prepare_agents_vals_partner(self, partner, settlement_type=None):
        """Utility method for getting agents creation dictionary of a partner."""
        agents = partner.agent_ids
        comercial_id = self.order_id.user_id.commercial_partner_id
        commission_05id = self.env["commission"].search(
            [("name", "=", "Commission 0.5%"), ("fix_qty", "=", "0.5")], limit=1, order="id desc"
        )
        for ag in partner.agent_ids:
            if ag.generic_agent:
                if comercial_id.agent:
                    return [(0, 0, self._prepare_agent_vals_commission05(comercial_id, commission_05id.id))]
                else:
                    return [(0, 0, self._prepare_agent_vals(agent)) for agent in agents]

        if settlement_type:
            agents = agents.filtered(
                lambda x: not x.commission_id.settlement_type or x.commission_id.settlement_type == settlement_type
            )
            return [(0, 0, self._prepare_agent_vals(agent)) for agent in agents]
