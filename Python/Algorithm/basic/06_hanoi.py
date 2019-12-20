# coding: utf-8

# O(2^n): 2^n - 1이므로
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return
    
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, "->", to_pos)

    hanoi(n - 1, aux_pos, to_pos, from_pos)
    
print("n = 1")
hanoi(1, 1, 3, 2)
print("n = 2")
hanoi(2, 1, 3, 2)
print("n = 3")
hanoi(3, 1, 3, 2)
print()