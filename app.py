games = [
{
    "name": "smash bros",
    "price": 59.99,
    "divice": "switch"

},
{
    "name": "persona 5 royal",
    "price": 59.99,
    "divice": "playstation 5"

},
{
    "name": "xenoblade chronicals deffinative addition",
    "price": 59.99,
    "divice": "switch"
}
]
cart = []
cartTotal = 0.0
for index, i in enumerate(games):
    print(index, i["name"])

while 1 ==1:
    gameNum = int(input("What game would you like to purchase (game num)"))
    cart.append({games[gameNum]["name"]})
    cartTotal = cartTotal + float(games[gameNum]["price"])
    if input("do you want to buy more (y/n)") == "n":
        print(cart)
        print(f"your cart total is {cartTotal}")
        break
    