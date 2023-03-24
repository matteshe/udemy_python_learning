print('Task 9.1 - Functions')

def pow3(number):
  return number**3

print(f'4 pow 3 is {pow3(4)}')
print(f'5 pow 3 is {pow3(5)}')

print('\n')
print('Task 9.2 - Functions')

def countdown(number):
  while number >= 0:
    print(number)
    number -= 1

countdown(10)

print('\n')
print('Task 9.3 - Functions')

def gibMin(a, b):
  if a <= b:
    return a
  else:
    return b

print(f'Minimum von 1 und 2 ist {gibMin(1,2)}.')
print(f'Minimum von 10 und 5 ist {gibMin(10,5)}.')