import sys

from sales_pipeline import (
    get_raw_sales_data,
    clean_sales_data,
    summarize_by_item,
    find_top_entry,
    print_item_table,
)

seed = None
if len(sys.argv) > 1 and sys.argv[1].strip() != "":
    seed = int(sys.argv[1])

print("=== MARKETING: Revenue by Item ===")
print()

raw_data = get_raw_sales_data(seed)

clean_data = clean_sales_data(raw_data)
summary = summarize_by_item(clean_data)
top_revenue = find_top_entry(summary, "revenue")
top_units = find_top_entry(summary, "units_sold")

print_item_table(summary)
print()
print(f"Top seller by revenue: {top_revenue['item']} (${top_revenue['revenue']:,.2f})")
print(f"Top seller by units:   {top_units['item']} ({top_units['units_sold']} units)")