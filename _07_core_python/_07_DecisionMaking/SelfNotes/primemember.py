ring_type = str(input("Enter the ring type:"))
a=['silver', 'gold','platinum','diamond']
if ring_type in a:
    if ring_type == 'silver':
        print("silver ring cost between the 1000 to 10000")
    elif ring_type == 'gold':
        print("gold ring cost between the 20000 to 100000")
    elif ring_type == 'platinum':
        print("platinum ring cost between the 500000 to 1000000")
    else:
        print("diamond ring cost above 100000")
else:
    print("Not in the list of rings")


n = int(input("Enter a number:"))
if n > 1:
    for i in range(2,n//2):
        if(n%i) == 0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is neither prime nor composite")


