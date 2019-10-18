#Modulo calculator:

a = int(input('Enter number A here: '))
b = int(input('Enter number B here: '))
m = int(input('Enter modulo m here: '))

add = a + b     #Addition
sub = a - b     #Subtraction
mul = a * b     #Multiplication
div = a / b     #Division

sumAdd = add%m
print('a + b(mod m) = ', sumAdd)

sumSub = sub%m
print('a - b(mod m) = ', sumSub)

sumMul = mul%m
print('a * b(mod m) = ', sumMul)

sumDiv = div%m
print('a / b(mod m) = ', int(sumDiv))

