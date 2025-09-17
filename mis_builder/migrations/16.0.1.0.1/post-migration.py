# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(cr, version):
    """Set the value of the analytic_domain field."""
    # Workaround to execute the migration script without errors
    # see https://github.com/odoo/odoo/blob/2a839ef1ed09c36f27ce7536ca3052d9f65ceed9/odoo/modules/migration.py#L252-L256
    env = cr
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE mis_report_instance_period
        SET analytic_domain = CONCAT('[("analytic_distribution_search", "in", [', analytic_account_id::VARCHAR, '])]')
        WHERE analytic_account_id IS NOT NULL
        """,  # noqa: E501
    )
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE mis_report_instance
        SET analytic_domain = CONCAT('[("analytic_distribution_search", "in", [', analytic_account_id::VARCHAR, '])]')
        WHERE analytic_account_id IS NOT NULL
        """,  # noqa: E501
    )
