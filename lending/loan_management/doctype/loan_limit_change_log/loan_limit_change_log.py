# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LoanLimitChangeLog(Document):
	pass


def create_loan_limit_change_log(**kwargs):
	loan_limit_change_log = frappe.new_doc("Loan Limit Change Log")
	loan_limit_change_log.update(kwargs)
	loan_limit_change_log.save(ignore_permissions=True)