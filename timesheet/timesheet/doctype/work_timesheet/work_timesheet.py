# Copyright (c) 2023, Novacept and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
class WorkTimesheet(Document):
	def validate(self):
		self.check_date()
		self.calculate_total_hours()
		self.get_manager()
	def check_date(self):
#		print(self.start_date)
#		print(type(self.start_date))
		if frappe.utils.get_datetime(self.start_date).weekday() != 0:
			frappe.throw('Start date must be a monday')
		start_date = frappe.utils.get_datetime(self.start_date)
		end_date = frappe.utils.add_days(start_date,6)
		self.end_date = frappe.utils.get_date_str(end_date)

	def calculate_total_hours(self):

		hours = 0

		for i in self.timesheet:
			week = [i.mon,i.tue,i.wed, i.thus, i.fri, i.sat, i.sun]
			for j in week:
				if j != None and j < 0:
					frappe.throw('Working hours cannot be negative')
				if j != None:
					hours += j
		self.total_working_hours = hours

	def get_manager(self):
		if self.employee_manager:
			return
		try:
			manager_employee = frappe.db.get_value('Employee',self.employee,'reports_to')
			manager_user = frappe.db.get_value('Employee',manager_employee,'user_id')
			self.employee_manager = manager_user

			manager_name = frappe.db.get_list('User',filters={'name': manager_user},fields=['full_name'],pluck = 'full_name')
			self.manager_name = manager_name[0]
		except:
			frappe.throw(f'Please set Reporting Manager(Reports to) for the Employee: {self.employee}')

	def on_submit(self):
		frappe.msgprint(f'Your timesheet has been sent to {self.manager_name} for approval')
