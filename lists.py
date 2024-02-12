#Exercitiul 2

#Given a list of integers. Remove duplicates from the list and create a tuple. Find the minimum and maximum number.

list = [2, 3, 4, 5, 6, 7, 2, 10, 6, 4, 5, 30, 12, 3, 13]
print(f"Lista initiala {list}")

no_duplicate_list = set(list)
print(f"Lista fara dubluri este {no_duplicate_list}")

my_tuple = tuple(no_duplicate_list)
print(f"Tuplul este {my_tuple}")

print(f"Numarul minim este {min(my_tuple)}")
print(f"Numarul maxim este {max(my_tuple)}")




