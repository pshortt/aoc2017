# import os,time

# clear = lambda: os.system('cls')      # or os.system('clear') for Unix

# for i in range(20,0,-1):
    # clear()
    # print(i)
    # time.sleep(1)

ls = [0, 1, 2, 3]
print(ls)

for i,x in enumerate(ls):
    x += 1
    ls[i] = x

print(ls)