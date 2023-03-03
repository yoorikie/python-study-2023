print("Введите число А = ")
A = int(input())

print("Введите число B = ")
B = int(input())

print("Выберете операцию")
print("+ - сложить A+B")
print("- - вычесть A-B")
print("* - умножить  A*B")
print("/ - поделить A÷B")
print("% - остаток A%B")
print("** - возведение в степень A**B")
D = input()

if D=='+':
  print("Cумма A+B =",A+B)

elif D=='-':
  print("Разность A-B =",A-B)

elif D=='*':
  print("Произведение A*B =",A*B)

elif D=='/':
  print("часное A÷B =",round(A/B,4))

elif D=='%':
  print("остаток A%B =",A%B)

elif D=='**':
  print("степень A**B =",A**B)
  

else:    
  print("Неправильно") 
