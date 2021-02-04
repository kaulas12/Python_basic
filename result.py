n=int(input())
record=[]
count=[]
result=[]
for i in range (n):
  name= input()
  score=float(input())
  stu=[name,score]
  record.append(stu)
#print(record)
for rows in record:
  for index,marks in enumerate(rows):
    if index==1:
      if marks not in count:
        count.append(marks)
count.remove(min(count))      
sec_mini=min(count)
length=len(record)
for i in range(length):
  if record[i][1]==sec_mini:
    #print(record[i][0])
    result.append(record[i][0])
result.sort()
for i in result:
  print(i)