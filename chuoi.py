# Chuoi

name = ''
address = ''
phone = ''
result = f'Student: {name}\nAddress:{address}\nPhone:{phone}'
print(result)
print(name, address, phone)


name = 'Dung'
address = 'Hanoi'
phone = '08074459410'
result = f'Student: {name}\nAddress:{address}\nPhone:{phone}'

print(result)


variable = 'string'
a = f'This is a {variable}'
print(a)


variable = 'three'
b = f'1:{{one}}, 2:{{two}}, 3:{variable}'
print(b)

#can giua
r = '{:^10}'.format('Dung')
print(r)

r = '{:*^10}'.format('Dung')
print(r)


#can le phai
r = '{:*>10}'.format('Dung') 
print(r)

#canle trai
r ='{:*<10}'.format('Dung')
print(r)


r = '{:*^50}'.format('Dung')
print(r)

r = 'Nguyen {:*^30} Trung Dung'.format('Hoang')
print(r)


row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Dung', 'Hanoi')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Purin', 'Japan')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)