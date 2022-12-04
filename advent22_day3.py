# -*- coding: utf-8 -*-
import string
container_file = open("C:/Users/Nick Anderson/Desktop/input.txt")
container_list = container_file.read().splitlines()
container_file.close()

total_priority = 0
blank_lists = 0
point_list = "0" + string.ascii_lowercase + string.ascii_uppercase

for current in container_list:
    half = int(len(current)/2)
    left = current[0:half]
    right = current[half:len(current)]
    left_set = set(left)
    right_set = set(right)
    letter = left_set.intersection(right_set).pop()
    if letter:
        print(letter," ",point_list.index(letter))
        total_priority = total_priority + point_list.index(letter[0])
            
print(total_priority)

letter = 0
badge_priority = 0
for current in range(0, len(container_list),3):
    first_elf = container_list[current]
    second_elf = container_list[current+1]
    third_elf = container_list[current+2]
    first_set = set(first_elf)
    second_set = set(second_elf)
    third_set = set(third_elf)
    letter = set.intersection(first_set,second_set,third_set).pop()
    badge_priority += point_list.index(letter)
    
print(badge_priority)