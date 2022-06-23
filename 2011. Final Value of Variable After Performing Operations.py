# Problem Link https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def final_value_operations(operations):
    x = 0

    for op in operations:
        if '--' in op:
            x -= 1
        else:
            x += 1

    return x

print(final_value_operations(["++X","++X","X++"]))
