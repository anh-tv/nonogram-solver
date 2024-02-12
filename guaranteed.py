#!/usr/bin/env python3
import sys

def get_guaranteed(length, tomography):
    guaranteed = [True for i in range(length)]
    seperators = [1 for i in range(len(tomography) - 1)]
    max_length = length - sum(tomography)
    current_sum = len(seperators)

    def add_head_tail_seperator(total, seperators):
        colored_sum = sum(tomography)
        for i in range(length - total - colored_sum + 1):
            solution = []
            full_seperators = [i] + seperators + [length - total - colored_sum - i]
            for i in range(len(tomography)):
                solution += [False for j in range(full_seperators[i])] + [True for j in range(tomography[i])]
            solution += [False for j in range(full_seperators[-1])]
            for index, item in enumerate(guaranteed):
                guaranteed[index] = guaranteed[index] & solution[index]

    def process(arr, total, max_value):
        add_head_tail_seperator(total, arr)
        if total < max_value:
            for i in range(len(arr)):
                arr[i] += 1
                process(arr, total + 1, max_value)
                arr[i] -= 1

    process(seperators, len(tomography) - 1, max_length)
    return guaranteed

if __name__ == "__main__":
    args = sys.argv
    length = int(args[1])
    tomography = list(map(int, args[2].split(",")))
    result = get_guaranteed(length, tomography)
    print("".join(map(lambda x: "o" if x else "x", result)))
