def calculate_data_charges(data_gb, plan_type):
    """Calculate data charges based on plan type and usage."""
    if plan_type.lower() == "pre-paid":
        rate = 10  # Rs. per GB for pre-paid
    else:
        rate = 8   # Rs. per GB for post-paid
    return data_gb * rate

def calculate_value_added_charges(services):
    """Calculate charges for value-added services."""
    service_rates = {
        "caller tune": 30,
        "ott subscription": 100,
        "international roaming": 200
    }
    total = 0
    for service in services:
        total += service_rates.get(service.lower(), 0)
    return total

def calculate_tax(amount):
    """Calculate tax (18% GST)."""
    return amount * 0.18

def main():
    data_gb = float(input("Enter data consumed (in GB): "))
    plan_type = input("Enter plan type (pre-paid or post-paid): ")
    services_input = input("Enter additional services used (comma separated, e.g. caller tune, ott subscription): ")
    services = [s.strip() for s in services_input.split(",") if s.strip()]

    dc = calculate_data_charges(data_gb, plan_type)
    vc = calculate_value_added_charges(services)
    subtotal = dc + vc
    tax = calculate_tax(subtotal)
    total = subtotal + tax

    print("\n--- Itemized Bill ---")
    print(f"Plan Type: {plan_type}")
    print(f"Data Usage: {data_gb} GB")
    print(f"Data Charges (DC): Rs. {dc:.2f}")
    print(f"Value-added Services: {', '.join(services) if services else 'None'}")
    print(f"Value-added Charges (VC): Rs. {vc:.2f}")
    print(f"Tax (18% GST): Rs. {tax:.2f}")
    print(f"Total Bill Amount: Rs. {total:.2f}")

if __name__ == "__main__":
    main()