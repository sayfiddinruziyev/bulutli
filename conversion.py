def to_octal(decimal_number):
    octal = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal = str(remainder) + octal
        decimal_number //= 8
    return octal

# Misol
decimal_number = 345
octal_result = to_octal(decimal_number)
print(f"{decimal_number} (10-lik) => {octal_result} (8-lik)")