import time

i = 1800
print("Press enter to start 30 min break! Or type minutes to continue.")
iv = input()
if iv:
    i = int(iv)
while i > 0:
    print(i)
    i -= 1
    time.sleep(1)
print("Back to work!")
