import sys

from sales_pipeline import (
    get_raw_sales_data,
    clean_sales_data,
    calculate_total_revenue,
    summarize_by_day,
    find_top_entry,
    print_day_table,
)

seed = None
if len(sys.argv) > 1 and sys.argv[1].strip() != "":
    seed = int(sys.argv[1])

print("=== OPERATIONS: Sales by Day ===")
print()

raw_data = get_raw_sales_data(seed)
clean_data = clean_sales_data(raw_data)
day_summary = summarize_by_day(clean_data)

total_revenue = calculate_total_revenue(clean_data)
top_revenue = find_top_entry(day_summary, "revenue")
top_units = find_top_entry(day_summary, "units_sold")

print_day_table(day_summary)
print()
print(f"Total Revenue:          ${total_revenue:,.2f}")
print(f"Busiest day by revenue: {top_revenue['date']} (${top_revenue['revenue']:,.2f})")
print(f"Busiest day by units:   {top_units['date']} ({top_units['units_sold']} units)")