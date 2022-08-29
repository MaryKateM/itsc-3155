first_last = input("Enter string: ")
if len(first_last) < 2:
    print("Your string is too short!")
else: 
        output = first_last[:2] + first_last[-2:]
        print(output)