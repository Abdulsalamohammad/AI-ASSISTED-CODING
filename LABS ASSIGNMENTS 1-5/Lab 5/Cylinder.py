def get_cylinder_price(cylinder_type):
    """Return price per cylinder based on type."""
    prices = {
        "domestic 14.2kg": 905.00,
        "domestic 5kg": 335.50,
        "commercial 19kg": 1886.50,
        "commercial 47.5kg": 4712.00
    }
    return prices.get(cylinder_type.lower(), 0)

def main():
    cylinder_type = input("Enter cylinder type (Domestic 14.2kg / Domestic 5kg / Commercial 19kg / Commercial 47.5kg): ")
    quantity = int(input("Enter number of cylinders booked: "))
    delivery_charges = float(input("Enter delivery charges (10 to 50 Rs): "))

    price_per_cylinder = get_cylinder_price(cylinder_type)
    base_amount = price_per_cylinder * quantity
    subsidy = 0
    if "domestic" in cylinder_type.lower():
        subsidy = float(input("Enter subsidy amount (Applicable only for domestic cylinders): "))

    total_bill = base_amount + subsidy + delivery_charges

    print("\n--- LPG Itemized Bill ---")
    print(f"Cylinder Type      : {cylinder_type}")
    print(f"Number of Cylinders: {quantity}")
    print(f"Base Amount        : Rs. {base_amount:.2f}")
    print(f"Subsidy            : Rs. {subsidy:.2f}")
    print(f"Delivery Charges   : Rs. {delivery_charges:.2f}")
    print(f"Total Bill Amount  : Rs. {total_bill:.2f}")

if __name__ == "__main__":
    main()