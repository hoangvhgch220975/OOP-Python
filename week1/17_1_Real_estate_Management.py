owners = ['John','Sara','Jenny','Mike']
prices = [110000, 120000, 305000, 290000]
areas = [1400, 1170, 2024, 1412]

def main():
    running = True
    while running:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_house(owners, prices, areas)
        elif choice == 2:
            edit_price(owners, prices, areas)
        elif choice == 3:
            sell_house(owners, prices, areas)
        elif choice ==4:
            show_house(owners, prices, areas)
        elif choice == 5:
            print('Happy to do bussiness with you')
            running = False
        else: 
            print('Invalid choice. Try again.')

def menu():
    print('1.Add house')
    print('2.Edit price')
    print('3 Sell a house')
    print('Show all house')
    print('5.Exit')

def add_house(owners, price, areas):
    owner = input("Enter the owner's name: ")
    price = int(input("Enter a house's price: "))
    area = int(input('Enter an area: '))

    owners.append(owner)
    prices.append(price)
    areas.append(area)

    print(f'Add house successfully')

def edit_price(owners, prices):
    owner = input("Enter the owner's name: ")
    new_price = int(input("Enter a new price: "))

    for i in range(len(owners)):
        if owners[i] == owner:
            prices[i] = new_price
            print(f'The {owner} house price is edited successfully')
            return
        print(f'The {owner} house is not found')

def sell_house(owners, prices, areas):
    owner = input("Enter owner's name: ")
    for i in range(len(owners)):
        if owners[i] == owner:
            owners.pop(i)
            prices.pop(i)
            areas.pop(i)
            print(f'The {owner} house was sold successfully')
            return
    print(f'The {owner} is not found')


def show_house(owners, prices, areas):
    for i in range(len(owners)):
        print(f'The owner {owners[i]} have a house cost {prices[i]} $ and wide {areas[i]} ')


main()