# -*- coding: utf-8 -*-
# Copyright (c) 2019, Maxwell Morais and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import uuid

class Process(Document):
	def autoname(self):
		if not self.get('name'):
			self.name = str(uuid.uuid4())
