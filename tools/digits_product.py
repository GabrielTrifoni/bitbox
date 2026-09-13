# tool: digits_product
# description: Returns the product of all digits in a number
# author: @GabrielTrifoni
# example: digits_product "123" -> "6"


def run(*args) -> str:
    number = args[0]
    
    if not number:
        raise ValueError("No number provided.")

    if not number.isdigit():
        raise ValueError("Argument must be a number.")

    product = 1
    for i in number:
        product *= int(i)

    return str(product)
