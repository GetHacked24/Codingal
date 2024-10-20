import math

def reverse_bits(num):
    num_bits = int(math.log2(num)) + 1
    reversed_num = 0

    for i in range(num_bits):
        reversed_num <<= 1
        reversed_num |= (num >> i) & 1

    return reversed_num

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    reversed_num = reverse_bits(num)
    print("Reversed number:", reversed_num)