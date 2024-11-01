import time
import datetime as d
from mymodule import add_three_numbers as add
print('Result: ', 7, 15, '.', sep="", end='!\n')
print('second l\ni\nn\ne')
print(5//3)
print()


time.sleep(3)
print('Hello')

print(d.datetime.now().time().hour)

print(add(7, 5, 5))

file = open('text.txt', 'w')

file.write('Hello')
file.write('!!!\n')
file.write('Luk')


file.close()

file = open('text.txt', 'r')
print(file.read())
file.close()
