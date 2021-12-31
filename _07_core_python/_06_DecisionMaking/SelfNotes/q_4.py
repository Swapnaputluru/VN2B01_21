'''
Q.4.Accept the marked price from the user and calculate the net amount as (Marked price-discount) to pay according to criteria:
Marked price               Discount
>10000                        20%
>7000 and <= 10000            15%
<=7000                        10%
'''

marked_price = int(input('Enter marked price:'))

if  marked_price > 10000:
    discount = marked_price*0.20
    print("discount is 20% of marked price:", discount, "/net amount is:", marked_price-discount)
elif 7000 < marked_price <= 10000:
    discount = marked_price*0.15
    print("discount is 15% of marked price:", discount, "/net amount is:", marked_price - discount)
else:
    discount = marked_price*0.10
    print("discount is 10% of marked price:", discount, "/net amount is:", marked_price - discount)










