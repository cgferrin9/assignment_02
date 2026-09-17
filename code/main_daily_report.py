"""
This script processes sales data through a pipeline of functions, 
then summarizes and displays sales statistics by day and overall revenue.
"""

import sys

from sales_pipeline import (
    get_raw_sales_data,
    clean_sales_data,
    calculate_total_revenue,
    summarize_by_day,
    find_top_entry,
    print_day_table,
)

# Set random seed if provided from command-line arguments for reproducibility
seed = None
if len(sys.argv) > 1 and sys.argv[1].strip() != "":
    seed = int(sys.argv[1])

print("=== OPERATIONS: Sales by Day ===")
print()

# Step 1: Acquire raw sales data, optionally using a fixed seed for consistent results
raw_data = get_raw_sales_data(seed)

# Step 2: Clean and normalize the raw data for analysis
clean_data = clean_sales_data(raw_data)

# Step 3: Aggregate cleaned data to summarize sales by each day
day_summary = summarize_by_day(clean_data)

# Step 4: Calculate overall total revenue from the cleaned dataset
total_revenue = calculate_total_revenue(clean_data)

# Step 5: Identify the day with highest revenue and highest units sold
top_revenue = find_top_entry(day_summary, "revenue")
top_units = find_top_entry(day_summary, "units_sold")

# Step 6: Print the summarized sales table and final statistics
print_day_table(day_summary)
print()
print(f"Total Revenue:          ${total_revenue:,.2f}")
print(f"Busiest day by revenue: {top_revenue['date']} (${top_revenue['revenue']:,.2f})")
print(f"Busiest day by units:   {top_units['date']} ({top_units['units_sold']} units)")