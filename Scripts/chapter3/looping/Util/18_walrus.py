remainder = value % modulus
if remainder:
    print(f"Not divisble! The remainder is {remainder}.")

# With assignment expressions, we could rewrite this as:
if remainder := value % modulus:
    print(f"Not divisble! The remainder is {remainder}.")