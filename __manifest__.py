# Copyright 2020 Tecnativa - Manuel Calero
# Copyright 2022 Quartile
# Copyright 2014-2022 Tecnativa - Pedro M. Baeza
{
    "name": "Sales commissions Extended",
    "version": "16.0.1.0.1",
    "category": "Sales Management",
    "license": "AGPL-3",
    "depends": [
        "commission",
        "sale_commission",
        "sale",
        "account_commission",
    ],
    "data": [
        "data/default_rec_commission05.xml",
        "views/res_partner.xml"
    ],
    "installable": True,
}
