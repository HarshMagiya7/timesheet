import frappe
@frappe.whitelist()
def summ(a,b):
	c = a + b
	return c
