print('Task 6 - Control Structures in Loops')
zahlen = [10, 1, 9, 8, 7, 9, 4, 5, 4, 8, 4, 3, 9, 7, 6]
print('Given list: {}'.format(zahlen))

cnt_four = 0
idx = 0
for z in zahlen:  
  if z == 4:
    cnt_four += 1
    print('index = {}'.format(idx))
  idx += 1

print('{}'.format(zahlen[0]))
print('Number 4 was found {} times.'.format(cnt_four))