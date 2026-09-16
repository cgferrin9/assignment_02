import sys

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

raw_data = get_raw_sales_data(seed)

clean_data = clean_sales_data(raw_data)
total_revenue = calculate_total_revenue(clean_data)

print_sales_table(clean_data)
print()
print(f"Total Pipeline Revenue: ${total_revenue:,.2f}")