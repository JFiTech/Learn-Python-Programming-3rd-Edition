n = 39
remainders = []

while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
remainders.reverse() # if we don't reverse it,
                    # we'd get 59 (in binary) as a result

print(remainders)