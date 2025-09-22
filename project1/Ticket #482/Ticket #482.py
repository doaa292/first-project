user_name = input ("Name? ").strip()
payment_method = input("Payment method? (card/cash) :").lower()

if payment_method == "card":
    print(f"{user_name.title()}, processing card securely...")
else:
    print(f"{user_name.title()}, cash accepted-receipt printed")