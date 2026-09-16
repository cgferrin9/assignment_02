def clean_currency(value) -> float:
    if value is None:
        return 0.0

    str_value = str(value).replace('$', '').replace(',', '').strip()

    try:
        return float(str_value)
    except ValueError:
        return 0.0

def clean_quantity(value) -> int:
    """Convert a raw quantity into an int, using 0 when it cannot be read."""

    if value is None:
        return 0

    try:
        return int(str(value).strip())
    except ValueError:
        return 0


def clean_sales_data(raw_data: list[dict]) -> list[dict]:
    """Clean every raw row and add the revenue it earned."""

    cleaned_data = []

    for row in raw_data:
        cleaned_row = {
            "date": row["date"],
            "item": row["item"],
            "price": clean_currency(row["price"]),
            "qty": clean_quantity(row["qty"])
        }

        cleaned_row["total_revenue"] = cleaned_row["price"] * cleaned_row["qty"]

        cleaned_data.append(cleaned_row)

    return cleaned_data


def calculate_total_revenue(cleaned_data: list[dict]) -> float:
    """Add up the revenue of every cleaned row."""

    total = 0

    for row in cleaned_data:
        total += row["total_revenue"]

    return float(total)


def summarize_by_item(cleaned_data: list[dict]) -> list[dict]:
    totals = {}  

    for row in cleaned_data:
        item = row["item"]
        qty = row["qty"]
        revenue = row["total_revenue"]

        # Create entry if not exist
        if item not in totals:
            totals[item] = {"item": item, "units_sold": 0, "revenue": 0.0}

        # Update totals
        totals[item]["units_sold"] += qty
        totals[item]["revenue"] += revenue

    # Convert to list and sort by revenue descending, then item ascending
    result = sorted(
        totals.values(),
        key=lambda entry: (-entry["revenue"], entry["item"])
    )

    return result


def summarize_by_day(cleaned_data: list[dict]) -> list[dict]:
    totals = {}

    for row in cleaned_data:
        date = row["date"]

        if date not in totals:
            totals[date] = {
                "date": date,
                "units_sold": 0,
                "revenue": 0.0
            }

        totals[date]["units_sold"] += row["qty"]
        totals[date]["revenue"] += row["total_revenue"]

    return sorted(
        totals.values(),
        key=lambda entry: entry["date"]
    )


def find_top_entry(summary: list[dict], field: str = "revenue") -> dict:
    
    if not summary:
        return {}

    top_entry = summary[0]

    for entry in summary:
        if entry[field] > top_entry[field]:
            top_entry = entry

    return top_entry