def gauss_algorithm_crt(coefficients, moduli):
    n = len(coefficients)
    N = 1  # Product of all moduli
    x = 0

    # Calculate N
    for m in moduli:
        N *= m

    # Apply Gauss' Algorithm
    for i in range(n):
        ai = coefficients[i]
        mi = moduli[i]
        Ni = N // mi
        Ni_inv = pow(Ni, -1, mi)
        x += ai * Ni * Ni_inv

    return x % N

def main():
    # Example usage:
    coefficients = [2, 3, 2]
    moduli = [3, 5, 7]

    result = gauss_algorithm_crt(coefficients, moduli)
    print("Solution:", result)

if __name__ == "__main__":
    main()
