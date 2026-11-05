my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_list = []

for sayi in my_list:
    if sayi not in new_list:
        new_list.append(sayi)
        
print("The original list:")
print(my_list)
print("\nThe list with unique elements only:")
print(new_list)
