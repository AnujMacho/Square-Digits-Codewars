def square_digits(num):
    a = f"{num}"
    b = []
    l = [b.append(i) or i for i in a]
    l1 = [int(k)*int(k) for k in l]
    print(l1)
    z=""
    for j in l1:
        z += str(j)

    return int(z)
print(square_digits(9119))