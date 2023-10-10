def simple_interest(p, t, r):
    print(f"The principal is {p}")
    print(f"The time period is {t}")
    print(f"The rate of interest is {r}")
    si = (p * t * r) / 100
    print(f"The Simple Interest is {si}")
    return si

p = int(input("Enter the principal amount: "))
t = int(input("Enter the time period: "))
r = int(input("Enter the rate of interest: "))

simple_interest(p, t, r)
