import frappe

# Remeber to import required modules
from frappe.utils import get_url
from frappe.utils.verified_command import get_signed_params

@frappe.whitelist()
def get_workflow_action_url(action, user, pdanum,current_state):
	apply_action_method = (
		"/api/method/frappe.workflow.doctype.workflow_action.workflow_action.apply_action"
	)

	params = {

		"doctype": 'Work Timesheet', # hard-coded in my case, you can pass it as an argument if you prefer
		"docname": pdanum, # an argument in my case, you can hard-code it if you prefer
		"action": action, # an argument in my case, you can hard-code it if you prefer
		"current_state": current_state, # an argument in my case, you can hard-code it if you prefer
		"user": user # an argument in my case, you can hard-code it if you prefer
	}
    # this will return you an URL to use in the href of the e-mail button
	return get_url(apply_action_method + "?" + get_signed_params(params))


