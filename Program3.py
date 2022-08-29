from collections import Counter
first_dict = {'a':100,'b':200,'c':300}
sec_dict = {'a':300,'b':200,'d':400}
print(Counter(first_dict) + Counter(sec_dict))