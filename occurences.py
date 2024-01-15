#Exercitiul 4

from collections import Counter

input_string = input(f"Scrie orice cuvant:")

occurence_counter = Counter(input_string)

for char, count in occurence_counter.items():
    print(f"{char}:{count}")