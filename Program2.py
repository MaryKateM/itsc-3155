first_int = int(input("First number: "))
second_int = int(input("Second number: "))

i = range(first_int, second_int)
for x in i:
    if x % 7 == 0 and x %5 != 0:
        print(x)
        