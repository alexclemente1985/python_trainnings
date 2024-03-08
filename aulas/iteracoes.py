def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total += 1
    return total

def iteracoes():
    even = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    for n in even:
        print(n)

    x = 0

    while x <= 20:
        print(f"teste de loop while: {x}")
        x += 5

    # range
    list1 = range(10)
    list2 = range(3, 7)
    list3 = range(1, 20, 2)

    print(f"list1: {list1}, list2: {list2}, list3: {list3}")

    for n in list1:
        print("teste for com lista de range: ", pow(2, n))

    for x in range(20):
        if x % 2 == 0:
            print('x: ', x)
        else:
            print("Odd")

    y = [0, 1, 2]
    for item in y:
        print("y: ", item)

    for item in range(len(y)):
        print(f"imprima y[{item}]: ", y[item])

    list_1 = [1, 3, 7, 15, 23, 43, 56, 98]
    print("count(list_1)", count(list_1))

    #Iterações com dicionários
    prices = {
        "box_of_spaghetti": 4,
        "lasagna": 5,
        "hamburger": 2
    }
    quantity = {
        "box_of_spaghetti": 6,
        "lasagna": 10,
        "hamburger": 0
    }

    money_spent = 0

    for i in prices:
        money_spent = money_spent + (prices[i] * quantity[i])

    print("money spent: ", money_spent)


if __name__ == '__main__':
    iteracoes()
