slog = 'Hello World'
print(slog)

p1 = 8
p2 = 7
p3 = 8
p4 = True
p5 = False
p6 = 'Hello'
p7 = "WH7"
p8 = 8.5

print(p1 + int(p8))

list1 = [1, 3, 5]
list1.append(7)
list2 = [2, 4, 6, 8]

list3 = list1 + list2
print(list3)

list4 = [0, 10]
list2 = list2 + list4
print(list2)
print(list3)
list3 = list1 + list2
print(list3)

hello = "Hello world"

p11 = 1
p12 = 'abc'
p13 = 1.5
p14 = 'a1b2'
p15 = '9'
p16 = '0.5'
p17 = True
p18 = p17
p17 = False
p19 = p13 % p11
print(p11 + int(p13))
p20 = int(p15)

list11 = [1, 2, 3]
list12 = [1, 2, 3, 'apple']
list11.append('banana')
print(list11)
list11.pop()
print(list11)
list11.append(4)
print(list11)
print(list11 + list12)
list13 = list11 + list12
print(list13)
list13.remove('apple')
print(list13)
list11.append(list12)
print(list11)
print(list1)
list5 = [1, 'a', 'bv2']
list1.extend(list5)
print(list1)
list1.insert(0, 77)
print(list1)
print(p20)
print(type(p20))
print(type(p15))
slog1 = hello.split()
print(slog1[0] + slog1[1])

hy = ['hello', 'everybody', '!', 'feeling', 'good', '?']
hy.append('yeah')
hy.insert(1, 'people')
hy1 = ['1', '2', '3']
hy.extend(hy1)
print(hy)

result = f"{hy[0].capitalize()}, {hy[1]}, {hy[2]} {hy[3].capitalize()} {hy[4]} {
    hy[5]} {hy[6].capitalize()}! {', '.join(hy[7:])}"

print(result)

hy.pop()
hy.remove('people')
print(hy)
