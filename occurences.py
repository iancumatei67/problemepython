#Exercitiul 4
#Given an input string, count occurrences of all characters within a string (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).

from collections import Counter

input_string = input(f"Scrie orice cuvant:")

occurence_counter = Counter(input_string)

for char, count in occurence_counter.items():
    print(f"{char}:{count}")
