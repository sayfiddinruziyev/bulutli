def to_binary(decimal_number):
    binary = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary = str(remainder) + binary
        decimal_number //= 2
    return binary




decimal_number = 45
binary_result = to_binary(decimal_number)
print(f"{decimal_number} (10-lik) => {binary_result} (2-lik)")
