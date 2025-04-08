from setuptools import setup, find_packages

setup(
    name="wasper_inventory",
    version="0.0.1",
    description="Inventory Management Solution for Multi-Branch Operations",
    author="Your Company",
    author_email="support@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "frappe>=15.0.0",
        "erpnext>=15.0.0"
    ]
) 