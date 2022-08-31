numItems = int(input("Number of items: "))
list = dict()

for x in range(numItems):
    user_input = input(("Input item and price: "))
    temp = user_input.split(' ')
    list[temp[0]] = int(temp[1])
    sort_dict = sorted(list.items(), key = lambda x:x[1], reverse = False)
    for x in sort_dict:
        print(x[0], x[1])
