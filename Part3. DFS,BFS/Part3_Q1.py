#Part3. DFS,BFS
#문제 1. N*M 크기의 0,1로 구성된 얼음틀이 있을 때 연속된 0은 1개로 계산한다면 0의 갯수는 총 몇개인지 구하기 

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))


#DFS로 특정한 노드를 방문한 뒤에 연결된 모드 노드들도 방문
def DFS(x,y):
    #주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        #상,하,좌,우 위치 모두 재귀적 호출 (중요!!!)
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if DFS(i,j) == True:
            result += 1

print(result)

#Point
#모든 좌표에서 시작
#하나의 좌표점 전달(시작점) -> 재귀함수 시작(시작점에서 0이라면 상하좌우 재귀로 구현)