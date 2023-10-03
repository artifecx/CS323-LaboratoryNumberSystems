def checker_all(n, valid_set):
    return all(c in valid_set for c in n)


def checker_binary(n):
    return checker_all(n, set("01"))


def checker_octal(n):
    return checker_all(n, set("01234567"))


def checker_decimal(n):
    return checker_all(n, set("0123456789"))


def checker_hexadecimal(n):
    return checker_all(n, set("0123456789ABCDEFabcdef"))


def any_to_decimal(n, base):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
           'f': 15}
    result = 0
    power = len(n) - 1
    for c in n:
        result += digits[c] * (base ** power)
        power -= 1
    return result


def decimal_to_any(n, base):
    digits = '0123456789ABCDEF'
    result = ''
    while n:
        result = digits[n % base] + result
        n //= base
    return result


def checker_operation(operation):
    return operation in ['1', '2', '3', '4', 'q']


def main():
    while True:
        print("Available Operations\n"
              "[1] Decimal to Any\n[2] Binary to Any\n[3] Octal to Any\n[4] Hex to Any\n[q] Quit")
        operation = input("Enter your desired operation: ")

        if not checker_operation(operation):
            choice = input("Invalid operation, try again? [1] Yes or [2] No: ")
            if choice != '1': break
            else: continue

        if operation == 'q': return

        while True:
            n = input("Enter n: ")

            # DECIMAL TO ANY
            if operation == '1':
                # check if n is a valid decimal number
                if not checker_decimal(n):
                    choice = input("Invalid decimal number, try again? [1] Yes or [2] No: ")
                    if choice != '1': return
                    else: continue

                base = input("Enter conversion (2 for Binary, 8 for octal, 16 for hex): ")

                # check if input is a valid base
                if base != '2' and base != '8' and base != '16':
                    choice = input("Invalid conversion, try again? [1] Yes or [2] No: ")
                    if choice != '1': break
                    else: continue

                converted = decimal_to_any(int(n), int(base))

                print("RESULT:", end=" ")
                if base == '2':
                    print(f"{n} [Decimal] is {converted} [Binary]\n")
                elif base == '8':
                    print(f"{n} [Decimal] is {converted} [Octal]\n")
                elif base == '16':
                    print(f"{n} [Decimal] is {converted} [Hex]\n")

                choice = input("Would you like to convert another number? [1] Yes or [2] No: ")
                if choice != '1': return
                else: break

            # BINARY TO ANY
            elif operation == '2':
                # check if n is a valid binary number
                if not checker_binary(n):
                    choice = input("Invalid binary number, try again? [1] Yes or [2] No: ")
                    if choice != '1': return
                    else: continue

                base = input("Enter conversion (8 for octal, 10 for decimal, 16 for hex): ")

                # check if input is a valid base
                if base != '8' and base != '10' and base != '16':
                    choice = input("Invalid conversion, try again? [1] Yes or [2] No: ")
                    if choice != '1': break
                    else: continue

                converted = decimal_to_any(any_to_decimal(n, 2), int(base))

                print("RESULT:", end=" ")
                if base == '8':
                    print(f"{n} [Binary] is {converted} [Octal]\n")
                elif base == '10':
                    print(f"{n} [Binary] is {converted} [Decimal]\n")
                elif base == '16':
                    print(f"{n} [Binary] is {converted} [Hex]\n")

                choice = input("Would you like to convert another number? [1] Yes or [2] No: ")
                if choice != '1': return
                else: break

            # OCTAL TO ANY
            elif operation == '3':
                # check if n is a valid octal number
                if not checker_octal(n):
                    choice = input("Invalid octal number, try again? [1] Yes or [2] No: ")
                    if choice != '1': return
                    else: continue

                base = input("Enter conversion (2 for binary, 10 for decimal, 16 for hex): ")

                # check if input is a valid base
                if base != '2' and base != '10' and base != '16':
                    choice = input("Invalid conversion, try again? [1] Yes or [2] No: ")
                    if choice != '1': break
                    else: continue

                converted = decimal_to_any(any_to_decimal(n, 8), int(base))

                print("RESULT:", end=" ")
                if base == '2':
                    print(f"{n} [Octal] is {converted} [Binary]\n")
                elif base == '10':
                    print(f"{n} [Octal] is {converted} [Decimal]\n")
                elif base == '16':
                    print(f"{n} [Octal] is {converted} [Hex]\n")

                choice = input("Would you like to convert another number? [1] Yes or [2] No: ")
                if choice != '1': return
                else: break

            # HEX TO ANY
            elif operation == '4':
                # check if n is a valid hex number
                if not checker_hexadecimal(n):
                    choice = input("Invalid hexadecimal number, try again? [1] Yes or [2] No: ")
                    if choice != '1': return
                    else: continue

                base = input("Enter conversion (2 for binary, 8 for octal, 10 for decimal): ")

                # check if input is a valid base
                if base != '2' and base != '8' and base != '10':
                    choice = input("Invalid conversion, try again? [1] Yes or [2] No: ")
                    if choice != '1': break
                    else: continue

                converted = decimal_to_any(any_to_decimal(n, 16), int(base))

                print("RESULT:", end=" ")
                if base == '2':
                    print(f"{n} [Hexadecimal] is {converted} [Binary]\n")
                elif base == '8':
                    print(f"{n} [Hexadecimal] is {converted} [Octal]\n")
                elif base == '10':
                    print(f"{n} [Hexadecimal] is {converted} [Decimal]\n")

                choice = input("Would you like to convert another number? [1] Yes or [2] No: ")
                if choice != '1': return
                else: break


main()