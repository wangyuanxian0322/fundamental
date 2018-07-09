import random #导入包

d = 0

while(d == 0):

    play = int(input("请输入（石头0 剪刀1 布2）：")) #这里的int必须加上
    i = random.randint(0,2) # 随机生成 0.1.2 其中一个值，并赋值给i

    if (play == 0 and i == 2) or (play == 1 and i == 0) or (play == 2 and i == 1):
        print("you lose")
    elif (play == 1 and i == 2) or (play == 2 and i == 0) or (play == 0 and i == 1):
        print("you win")
    elif play == i:
        print("draw game")
    elif play == 3:
        print("you exit the game")
        d = 1
    else:
        print('wrong input, please play again')

#print(i) #查看生成的随机值