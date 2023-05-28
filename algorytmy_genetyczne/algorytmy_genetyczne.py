import random

def encode_binary(x, num_bits):
    """encode a decimal value into a binary string representation"""
    max_value = 2**num_bits - 1  # maximum decimal value that can be represented by num_bits
    scaled_value = int((x / 10) * max_value)  # scale x to fit within the range of num_bits
    binary_string = bin(scaled_value)[2:].zfill(num_bits)  # convert scaled_value to binary string representation
    return binary_string

def decode_binary(binary_string, num_bits):
    """decode a binary string representation into a decimal value"""
    max_value = 2**num_bits - 1  # maximum decimal value that can be represented by num_bits
    scaled_value = int(binary_string, 2)  # convert binary string representation to decimal
    x = (scaled_value / max_value) * 10  # scale the decimal value back to the range [0,10]
    return x

num_bits = 8  # number of bits to represent x
x = 6.5  # decimal value of x

binary_string = encode_binary(x, num_bits)
print(f"Binary string representation of {x} is {binary_string}")

decode_x = decode_binary(binary_string, num_bits)
print(f"Decimal value of {binary_string} is {decode_x}")