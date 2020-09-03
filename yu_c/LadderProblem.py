'''爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；
若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；
只有每步上7阶，最后刚好一阶也不剩。'''

number = 1
switch = 1
while switch:
    if number % 2 == 1 and number % 3 == 2 and number % 5 == 4 and number % 6 == 5 and number % 7 == 0:
        print(number)
        switch = 0
    else:
        print(number)
        number +=1

        

