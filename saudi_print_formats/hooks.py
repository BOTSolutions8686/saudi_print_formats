app_name = "saudi_print_formats"
app_title = "Saudi Print Formats"
app_publisher = "Mazhar Ali"
app_description = "Contain print formats for KSA ERP NExt"
app_email = "engrmazharali95@gmail.com"
app_license = "mit"

# Apps
# ------------------

fixtures = [
     {
        "doctype": "Print Format", 
        "filters": [
            ["name", "in", ["Bot Format J", "Bot Format N","Bot Format S","Bot Format H","Bot Format B","Bot Format B Q","Bot Format HE"]]
        ]
    },    {
        "doctype": "DocType",
        "filters": [
            ["name", "=", "Sales Invoice"]
        ]
    },
    {
        "doctype": "DocType",
        "filters": [["name", "=", "Company"]]
    }
]


# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "saudi_print_formats",
# 		"logo": "/assets/saudi_print_formats/logo.png",
# 		"title": "Saudi Print Formats",
# 		"route": "/saudi_print_formats",
# 		"has_permission": "saudi_print_formats.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/saudi_print_formats/css/saudi_print_formats.css"
# app_include_js = "/assets/saudi_print_formats/js/saudi_print_formats.js"

# include js, css files in header of web template
# web_include_css = "/assets/saudi_print_formats/css/saudi_print_formats.css"
# web_include_js = "/assets/saudi_print_formats/js/saudi_print_formats.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "saudi_print_formats/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "saudi_print_formats/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "saudi_print_formats.utils.jinja_methods",
# 	"filters": "saudi_print_formats.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "saudi_print_formats.install.before_install"
# after_install = "saudi_print_formats.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "saudi_print_formats.uninstall.before_uninstall"
# after_uninstall = "saudi_print_formats.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "saudi_print_formats.utils.before_app_install"
# after_app_install = "saudi_print_formats.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "saudi_print_formats.utils.before_app_uninstall"
# after_app_uninstall = "saudi_print_formats.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "saudi_print_formats.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"saudi_print_formats.tasks.all"
# 	],
# 	"daily": [
# 		"saudi_print_formats.tasks.daily"
# 	],
# 	"hourly": [
# 		"saudi_print_formats.tasks.hourly"
# 	],
# 	"weekly": [
# 		"saudi_print_formats.tasks.weekly"
# 	],
# 	"monthly": [
# 		"saudi_print_formats.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "saudi_print_formats.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "saudi_print_formats.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "saudi_print_formats.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["saudi_print_formats.utils.before_request"]
# after_request = ["saudi_print_formats.utils.after_request"]

# Job Events
# ----------
# before_job = ["saudi_print_formats.utils.before_job"]
# after_job = ["saudi_print_formats.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"saudi_print_formats.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

