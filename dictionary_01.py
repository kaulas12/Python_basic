n=int(input())
student_marks ={}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float,line))
    student_marks[name] = scores
query_name= input()
list1=student_marks[f'{query_name}']
length=len(list1)
avg=sum(list1)/length
print(f'{avg:.2f}'.format(avg))
