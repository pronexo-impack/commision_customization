# Copyright 2014-2022 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartnerExtended(models.Model):
    _inherit = "res.partner"

    generic_agent = fields.Boolean(default=False, string="Agente Genérico")
