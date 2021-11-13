#Part2. 구현
#문제 1. (1,1) 에서 시작해서 입력받은(L,R,U,D)중에서 받은 대로 1칸씩 이동해서 마지막 인덱스 출력하기
  
n = int(input())
list_a=list(input().split())
  
a = [1,1]

for i in list_a:
  if i == 'R':
    if a[1] + 1 == 0 or a[1] + 1 > n :
      continue
    else:
      a[1] += 1
  elif i == 'U':
    if a[0] - 1 == 0 or a[0] - 1 > n :
      continue
    else:
      a[0] -= 1
  elif i == 'D':
    if a[0] + 1 == 0 or a[0] + 1 > n :
      continue
    else:
      a[0] += 1
  else:
    if a[1] - 1 == 0 or a[1] - 1 > n:
      continue
    else:
      a[1] -= 1

for i in a: 
  print(i,end=" ")