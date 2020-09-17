print("--------------------学生成绩评分-------------------------")

temp= input("请输入学生的成绩：")
success = int(temp)
if success >=60 and success <80:
    print("C")
elif success <60:
    print("D")
elif success >=80 and success <90:
    print("B")
elif success >=90 and success <=100:
    print("A")
else:
    print("输入有误，请稍后再试")
