#这里做一个最简单的计算器，进行两个参数的加减乘除
#我的思路是，将一个计算过程拆分成四部，分别是输入第一个数，选择运算符号，输入第二个数，最后输出结果。

#第一步输入第一个数字
#input()函数输入的内容是字符串
#这里使用了float()函数，是将我输入的数字字符串转化为浮点数以方便用于计算。
#还可以使用int()函数，这个函数是将输入的数字字符串转化为数字，这个函数默认是十进制，所以必须输入整数的数字字符串。否则会报错
x=float(input("请输入第一个数字 "))

#第二步是选择运算符号，这里的运算符号其实就是一个字符串
print("""
请选择运算符号：
"+":相加
"-":相减
"/":相除
"*":相乘
""")
choice=input("请选择运算符号 ")

#第三步输入第三个数字
y=float(input("请输入第二个数字 "))

#最后一步，使用if语句，通过第二步输入的字符串来确认计算方式
#这里使用了round()函数，是为了使输出结果保留两位小数
if choice == "+":
    print(x,"+",y,"=",round(x+y,2))

elif choice =="-":
    print(x,"-",y,"=",round(x-y,2))

elif choice =="/":
    print(x,"/",y,"=",round(x/y,2))

elif choice =="*":
    print(x,"*",y,"=",round(x*y,2))
    
else:
    print("输入错误")