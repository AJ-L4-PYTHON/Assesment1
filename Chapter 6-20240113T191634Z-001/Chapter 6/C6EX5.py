sandwich_orders = [
    'pastrami', 'turkey roast', 'ranch chicken', 'pastrami',
    'meat extravaganza', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we are out of pastrami today. Come back next year")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm cooking your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")