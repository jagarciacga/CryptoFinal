def chinese_remainder_theorem(moduli, remainders):
    # Calculate the product of all moduli
    prod_moduli = 1
    for m in moduli:
        prod_moduli *= m

    result = 0

    # Apply CRT formula
    for mi, ai in zip(moduli, remainders):
        bi = prod_moduli // mi
        bi_inv = pow(bi, -1, mi)
        result += ai * bi * bi_inv

    return result % prod_moduli

def main():
    # Example usage:
    moduli = [5, 17]
    remainders = [3, 14]

    result = chinese_remainder_theorem(moduli, remainders)
    print("Solution:", result)

if __name__ == "__main__":
    main()
