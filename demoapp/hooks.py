from . import __version__ as app_version

app_name = "demoapp"
app_title = "Demo Management"
app_publisher = "SD"
app_description = "Demo App Management"
app_icon = "octicon octicon-file-directory"
app_color = "yellow"
app_email = "sd@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/demoapp/css/demoapp.css"
# app_include_js = "/assets/demoapp/js/demoapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/demoapp/css/demoapp.css"
# web_include_js = "/assets/demoapp/js/demoapp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "demoapp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "demoapp.install.before_install"
# after_install = "demoapp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "demoapp.uninstall.before_uninstall"
# after_uninstall = "demoapp.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "demoapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"demoapp.tasks.all"
#	],
#	"daily": [
#		"demoapp.tasks.daily"
#	],
#	"hourly": [
#		"demoapp.tasks.hourly"
#	],
#	"weekly": [
#		"demoapp.tasks.weekly"
#	]
#	"monthly": [
#		"demoapp.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "demoapp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "demoapp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "demoapp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["demoapp.utils.before_request"]
# after_request = ["demoapp.utils.after_request"]

# Job Events
# ----------
# before_job = ["demoapp.utils.before_job"]
# after_job = ["demoapp.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"demoapp.auth.validate"
# ]

