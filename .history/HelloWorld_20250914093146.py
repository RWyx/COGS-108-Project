import sys

x = input("请输入成绩: ")
y = input("midterm final")
z = x.split()

if x.strip() == "":
    print("空输入，程序结束")
    sys.exit(0)   # 这里就相当于 Java 的 return 0;
2
print("你输入的是:", z)

