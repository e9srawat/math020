"""Math 020"""


def solver(n: int):
    """returns sum of the digits in n!"""
    factn = 1
    for i in range(1, n + 1):
        carry = 0
        prd = 0
        prdl = []
        for j in reversed(range(len(str(factn)))):
            if carry:
                prd = int(str(factn)[j]) * i + int(carry)
            else:
                prd = int(str(factn)[j]) * i
            if j == 0:
                prdl.append(str(prd))
            else:
                prdl.append(str(prd)[-1])
                carry = str(prd)[0:-1]
        factn = "".join(reversed(prdl))
        addr = 0
    for i in factn:
        addr += int(i)

    return addr
