import random

hex_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def gen_hash():
    my_hash = ""
    for i in range(32):
        my_hash += random.choice(hex_list)
    return my_hash

print(gen_hash())
