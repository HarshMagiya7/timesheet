# Copyright (c) 2023, Novacept and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class WorkTimesheet(Document):
	pass

@frappe.whitelist()
def demo(a,b):
	c = a+b
	return c
