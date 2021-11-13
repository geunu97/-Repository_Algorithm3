#Part2. 구현
#문제 2. 

#시간문제!!!!!!!!! 
#아주아주 간단한 문제...
#노트에 써놓기 

n = int(input())
  
count = 0
for i in range(n+1):
  for j in range(60):
    for k in range(60):                         #시간 반복문 3개로 표현하기
      if '3' in str(i) + str(j) + str(k):       #str로 모두 붙여서 표현하기
        count += 1

print(count)
  