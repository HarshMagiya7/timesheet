# Copyright (c) 2023, Novacept and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
class WorkTimesheet(Document):
	def validate(self):
		self.check_date()
		self.calculate_total_hours()

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
				if j != None:
					hours += j
		self.total_working_hours = hours
