"""
This script retrieves, cleans, and analyzes raw sales data to 
calculate total revenue and display detailed daily sales information.
"""

import sys

# Initialize seed to None; if provided as a command-line argument, use it 
# to allow reproducible data generation or fetching.
seed = None
if len(sys.argv) > 1 and sys.argv[1].strip() != "":
    seed = int(sys.argv[1])

from sales_pipeline import (
    get_raw_sales_data,
    clean_sales_data,
    calculate_total_revenue,
    print_sales_table,
)

print("=== FINANCE: Daily Sales Detail ===")
print()

# Step 1: Retrieve raw sales data, potentially using the optional seed.
raw_data = get_raw_sales_data(seed)

# Step 2: Clean and preprocess the raw sales data for accurate analysis.
clean_data = clean_sales_data(raw_data)

# Step 3: Calculate the total revenue from the cleaned sales data.
total_revenue = calculate_total_revenue(clean_data)

# Step 4: Print a detailed table of daily sales to provide insight into sales performance.
print_sales_table(clean_data)
print()

# Step 5: Show the total revenue generated across all sales entries.
print(f"Total Pipeline Revenue: ${total_revenue:,.2f}")