print("Large or Extra Large?")
pizza = input()
if pizza == "Large":
    print("That costs $6")
    large = 6
    print("How many toppings, 1, 2, 3 or 4?")
    toppings = input()
    if toppings == "1":
        subtotal = float(large + 1.00)
        print("Your subtotal is")
        print("$", subtotal)
        tax = float(0.13 * subtotal)
        print("Your tax is")
        print("$", tax)
        fintot = float(tax + subtotal)
        print("Your final cost is")
        print("$", fintot)
    if toppings == "2":
        subtotal = float(large + 1.75)
        print("Your subtotal is")
        print("$", subtotal)
        tax = float(0.13 * subtotal)
        print("Your tax is")
        print("$", tax)
        fintot = float(tax + subtotal)
        print("Your final cost is")
        print("$", fintot)
    if toppings == "3":
        subtotal = float(large + 2.50)
        print("Your subtotal is")
        print("$", subtotal)
        tax = float(0.13 * subtotal)
        print("Your tax is")
        print("$", tax)
        fintot = float(tax + subtotal)
        print("Your final cost is")
        print("$", fintot)



