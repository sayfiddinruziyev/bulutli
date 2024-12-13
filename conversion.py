def to_hexadecimal(decimal_number):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal_number //= 16
    return hexadecimal

# Misol
decimal_number = 345
hexadecimal_result = to_hexadecimal(decimal_number)
print(f"{decimal_number} (10-lik) => {hexadecimal_result} (16-lik)")