import random

r = random.randint(1, 100)
count = 0
while True:
    count+=1
    print("請猜第", count, "次。")
    num = eval(input('請猜數字:'))
    if num == r :
        print('你猜中了！')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
