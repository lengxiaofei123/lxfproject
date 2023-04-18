# python基础算法
# ..................................................................................................................
# 练习一、计算随机数1到1000的各位数之和，如12和为3
# def qiuhe():
#     while True:
#         a = int(input("请输入1~1000的数值："))
#         if a == 0:
#             break
#         b = a % 10
#         c = a // 10
#         d = c % 10
#         e = a // 100
#         total = b + d + e
#         print("结果是"+str(total),"请输入0退出")
# ..................................................................................................................
# 练习二、多个输入值计算结果
# def duozhi():
#     a, b, d = eval(input("请输入三个值："))
#     print(a + b - d)
# ..................................................................................................................
# 练习三、剪刀石头布
import random
from inputimeout import inputimeout, TimeoutOccurred

print("......欢迎来到剪刀石头布小游戏......")


# 如何实现超时退出，利用inputtimeout模块和try来修饰,此包需要pip安装
# def input_value():
#     while True:
#         try:
#             # 设置超时时间为十秒
#             yourchoose = str(inputimeout(prompt="请输入剪刀或者石头或者布：", timeout=10))
#             if yourchoose == "退出":
#                 break
#             systemchoose = random.randint(1, 3)
#             if systemchoose == 1:
#                 value = '剪刀'
#             elif systemchoose == 2:
#                 value = "石头"
#             else:
#                 value = "布"
#             try:
#                 if (yourchoose == "剪刀" and value == "布") or (yourchoose == "石头" and value == "剪刀") or (
#                         yourchoose == "布" and value == "石头"):
#                     print("系统选择是%s，你赢啦" % value)
#                 elif (yourchoose == "剪刀" and value == "石头") or (yourchoose == "石头" and value == "布") or (
#                         yourchoose == "布" and value == "剪刀"):
#                     print("系统选择是%s，你输啦" % value)
#                 elif (yourchoose == "剪刀" and value == "剪刀") or (yourchoose == "石头" and value == "石头") or (
#                         yourchoose == "布" and value == "布"):
#                     print("系统选择是%s，你们平手!" % value)
#                 else:
#                     print("输入有误，请重新输入剪刀石头布")
#             except Exception:
#                 print("输入有误，请重新输入")
#             print("...输入退出即可退出！...")
#         except TimeoutOccurred:
#             print("输入超时退出！")
#             # 超时退出循环
#             break
#
#
# input_value()
# ..................................................................................................................
