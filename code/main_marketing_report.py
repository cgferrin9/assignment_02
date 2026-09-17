"""
This script processes sales data to summarize revenue and units sold by item,
then identifies and displays the top-selling items based on revenue and units.
"""

import sys

from sales_pipeline import (
    get_raw_sales_data,
    clean_sales_data,
    summarize_by_item,
    find_top_entry,
    print_item_table,
)

# Optionally use a command-line argument as a seed for reproducible data processing
seed = None
if len(sys.argv) > 1 and sys.argv[1].strip() != "":
    seed = int(sys.argv[1])

print("=== MARKETING: Revenue by Item ===")
print()

# Step 1: Load raw sales data, optionally using the seed to control randomness
raw_data = get_raw_sales_data(seed)

# Step 2: Clean and prepare the raw data for aggregation
clean_data = clean_sales_data(raw_data)

# Step 3: Aggregate sales data by item, computing summary statistics like revenue and units sold
summary = summarize_by_item(clean_data)

# Step 4: Find the item with the highest revenue and the highest units sold
top_revenue = find_top_entry(summary, "revenue")
top_units = find_top_entry(summary, "units_sold")

# Step 5: Display a detailed table for all items and print the top sellers
print_item_table(summary)
print()
print(f"Top seller by revenue: {top_revenue['item']} (${top_revenue['revenue']:,.2f})")
print(f"Top seller by units:   {top_units['item']} ({top_units['units_sold']} units)")