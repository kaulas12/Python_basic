picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
#for 0='' for 1='*'
#for i,char in enumerate(picture):
 # print(i,char)
for i in picture:
  print('\t')
  for j in i:
    if j==0:
      print(' ',end='')
    else:
      print('*',end='')  
   # print(f'{j}',end='') 