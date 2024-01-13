prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are happy with your toppings: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break