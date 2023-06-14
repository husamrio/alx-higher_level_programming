#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = sum(weight * occurrence for weight, occurrence in my_list)
    frequency = sum(occurrence for weight, occurrence in my_list)
    return total / frequency if frequency > 0 else 0
