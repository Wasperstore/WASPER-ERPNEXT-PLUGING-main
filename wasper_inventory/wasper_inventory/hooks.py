app_name = "wasper_inventory"
app_title = "Wasper Inventory"
app_publisher = "Your Company"
app_description = "Inventory Management Solution for Multi-Branch Operations"
app_email = "support@yourcompany.com"
app_license = "MIT"

# Fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["module", "in", ["Wasper Inventory"]]]
    },
    {
        "doctype": "Property Setter",
        "filters": [["module", "in", ["Wasper Inventory"]]]
    },
    {
        "doctype": "Report",
        "filters": [["module", "in", ["Wasper Inventory"]]]
    }
]

# App Includes
app_include_js = ["wasper_inventory.bundle.js"]
app_include_css = ["wasper_inventory.bundle.css"]

# Website Context
website_context = {
    "favicon": "/assets/wasper_inventory/images/favicon.ico",
    "splash_image": "/assets/wasper_inventory/images/splash.png"
}

# DocType Classes
doc_events = {
    "Sales Invoice": {
        "on_submit": "wasper_inventory.wasper_inventory.doc_events.sales_invoice.on_submit",
        "on_cancel": "wasper_inventory.wasper_inventory.doc_events.sales_invoice.on_cancel"
    },
    "Purchase Invoice": {
        "on_submit": "wasper_inventory.wasper_inventory.doc_events.purchase_invoice.on_submit",
        "on_cancel": "wasper_inventory.wasper_inventory.doc_events.purchase_invoice.on_cancel"
    },
    "Stock Entry": {
        "on_submit": "wasper_inventory.wasper_inventory.doc_events.stock_entry.on_submit",
        "on_cancel": "wasper_inventory.wasper_inventory.doc_events.stock_entry.on_cancel"
    }
}

# Scheduled Tasks
scheduler_events = {
    "daily": [
        "wasper_inventory.wasper_inventory.utils.send_low_stock_notifications",
        "wasper_inventory.wasper_inventory.utils.send_daily_sales_report"
    ],
    "weekly": [
        "wasper_inventory.wasper_inventory.utils.send_weekly_inventory_report"
    ],
    "monthly": [
        "wasper_inventory.wasper_inventory.utils.send_monthly_performance_report"
    ]
}

# Permissions
permissions = [
    {
        "role": "System Manager",
        "doctype": "Branch",
        "permlevel": 0,
        "rights": ["read", "write", "create", "delete", "report", "export", "import", "print"]
    },
    {
        "role": "Branch Manager",
        "doctype": "Branch",
        "permlevel": 0,
        "rights": ["read", "write", "create", "report", "print"]
    }
] 