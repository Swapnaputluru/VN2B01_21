customer_category = str(input("Enter customer category:"))
units = int(input("Enter units:"))
a = ["commercial", "institutional", "domestic"]
if customer_category in a:
    if customer_category == "commercial":
        if units <= 5000:
            print("rate for commercial category which is till 5000 units is rs 1500/-")
        elif 5000 < units <= 10000:
            print("rate for commercial category which is next 5000 units is rs 0.25 per unit:", "total rate for given units:", units * 0.25, "/-")
        elif 10000 < units <= 20000:
            print("rate for commercial category which is next 10000 units is rs 0.23 per unit:", "total rate for given units:", units * 0.23, "/-")
        else:
            print("rate is rs 0.20 per unit:", "total rate for given units:", units * 0.20, "/-")

    if customer_category == "institutional":
        if units <= 5000:
            print("rate is rs 1800/-")
        elif 5001 <= units <= 10000:
            print("rate is rs 0.30 per unit:", "total rate for given units:", units * 0.30, "/-")
        elif 10000 < units <= 20000:
            print("rate is rs 0.28 per unit:", "total rate for given units:", units * 0.28, "/-")
        else:
            print("rate is rs 0.25 per unit:", "total rate for given units:", units * 0.25, "/-")

    if customer_category == "domestic":
        if units <= 100:
            print("rate is rs 75/-")
        elif 100 < units <= 200:
            print("rate is rs 1.25 per unit:", "total rate for given units:", units * 1.25, "/-")
        elif 200 < units <= 400:
            print("rate is rs 2.00 per unit:", "total rate for given units:", units * 2.00, "/-")
        else:
            print("rate is rs 2.5 per unit:", "total rate for given units:", units * 2.5, "/-")

else:
    print("not in the list")