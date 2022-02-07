marks = {}
for _ in range(int(input())):
    a=input().split()
    marks[a[0]]=list(map(float,a[1:]))
print('%.2f'%(sum(marks[input()])/3))
