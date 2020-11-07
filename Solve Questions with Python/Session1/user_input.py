print("开始")
# = 赋值. 把等号右边的内容赋值给左边
s = input("这里是input:") # input输入. 让用户输入一些内容. 程序会停在这句话. 阻塞.
# input结束的时候. 会自动的收集到用户输入的内容. 把内容返回给前面的变量
print("结束")

print("用户输入的内容是", s) # print可以一次性打印多个内容

print("大哥", "你的", "表", "不错")

a = input("请输入一个a:") # 获取到的内容都是字符串
b = input("请输入一个b:")
# print(a + b) # 拼接
# 通过类型转换把字符串转换成int

c = int(a) # int: 整数 把字符串转化成int
d = int(b)
print(c + d)

a = int(input("请输入一个a:")) # 获取到的内容都是字符串
b = int(input("请输入一个b:"))
# print(a + b) # 拼接
# 通过类型转换把字符串转换成int
print(a + b)

a = 10
b = 20

print(str(a) + str(b))


PI = 3.1415
radius = 20
area = PI * radius * radius
# area is equal to PI times squares of radius

r = 2
name = "i like to go to school"
weight = 52.1
i_am_smart = False
