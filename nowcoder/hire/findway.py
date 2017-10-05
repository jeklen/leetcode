number = int(input())
order = []
while number != 0:
    if number % 2:
        order.append(1)
        number = (number - 1) / 2
    else:
        order.append(2)
        number = (number - 2) / 2
for i in range(len(order)-1, -1, -1):
    print(order[i], end='')