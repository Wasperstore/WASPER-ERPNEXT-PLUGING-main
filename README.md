# Wasper Inventory

A comprehensive inventory management solution built on Frappe Framework.

## Features

- Multi-branch inventory management
- Point of Sale (POS) system
- Stock management and tracking
- Automated email notifications
- Comprehensive reporting
- Branch performance analytics

## Installation

1. Install Frappe Framework:
```bash
bench init frappe-bench
cd frappe-bench
```

2. Create a new site:
```bash
bench new-site wasper.local
```

3. Install Wasper Inventory:
```bash
bench get-app wasper_inventory https://github.com/Wasperstore/WASPER-ERPNEXT-PLUGING.git
bench --site wasper.local install-app wasper_inventory
```

## Configuration

1. Set up branches:
   - Go to: Branch > New
   - Enter branch details
   - Assign branch manager

2. Configure POS:
   - Go to: POS Profile > New
   - Set up payment methods
   - Configure users

3. Set up email notifications:
   - Configure email server
   - Set up notification schedules

## Usage

### POS System

1. Access POS:
   - Go to: POS
   - Select branch and POS profile
   - Start selling

2. Process sales:
   - Add items to cart
   - Select payment method
   - Complete transaction

### Inventory Management

1. Stock management:
   - Track stock levels
   - Set reorder points
   - Manage warehouses

2. Stock transfers:
   - Create stock entries
   - Transfer between branches
   - Update stock levels

### Reports

1. Sales reports:
   - Branch-wise sales
   - Item-wise sales
   - POS summary

2. Stock reports:
   - Stock balance
   - Stock movement
   - Low stock alerts

## Development

### Setup Development Environment

1. Clone the repository:
```bash
git clone https://github.com/Wasperstore/WASPER-ERPNEXT-PLUGING.git
```

2. Install dependencies:
```bash
cd WASPER-ERPNEXT-PLUGING
pip install -e .
yarn install
```

3. Build assets:
```bash
bench build --app wasper_inventory
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Support

For support, email support@wasper.com 
