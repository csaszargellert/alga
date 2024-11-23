"""class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    decoded_string = ""
    current = root

    for char in s:
        if char == '0':
            current = current.left
        else:
            current = current.right

        if current.left is None and current.right is None:
            decoded_string += current.data
            current = root

    print(decoded_string)