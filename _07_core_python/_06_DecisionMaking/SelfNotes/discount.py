
sht = int(input('Enter shirt and T-shirt amount:'))
if 0 <= sht <= 100:
    discount = sht*0.05
elif 101 <= sht <= 200:
    discount = sht * 0.10
elif 201 <= sht <= 300:
    discount = sht * 0.15
else:
    discount = sht * 0.22


p = int(input('Enter pant amount:'))
if 0 <= p <= 100:
    dis = p*0.03
elif 101 <= p <= 200:
    dis = p * 0.08
elif 201 <= p <= 300:
    dis = p * 0.12
else:
    dis = p * 0.20


sh = int(input('Enter shorts amount:'))
if 0 <= sh <= 100:
    disc = sh
elif 101 <= sh <= 200:
    disc = sh * 0.05
elif 201 <= sh <= 300:
    disc = sh * 0.10
else:
    disc = sh * 0.18

print("Discount Amount ", discount, dis, disc )
print("Net amount: ", (sht-discount) + (p - dis) + (sh - disc))