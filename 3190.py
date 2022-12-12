from collections import deque
#1453 ~ #1659
#column, row
"""
 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 
 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 
사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L



10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
"""

def moveF (cur):
  di = []
  col, row = 0, 0
  if cur == 1:
    col = 0
    row = 1
  elif cur == 2:
    col = -1
    row = 0
  elif cur == 3:
    col = 0
    row = -1
  elif cur == 4:
    col = 1
    row = 0
  di = [col,row]
  return di

def direction (cur, c):
  next = cur
  # cur = 1,2,3,4 == right, up, left, down
  if cur == 1:
    if c == "L":
      next = 2
    elif c == "D":
      next = 4
  if cur == 2:
    if c == "L":
      next = 3
    elif c == "D":
      next = 1
  if cur == 3:
    if c == "L":
      next = 4
    elif c == "D":
      next = 2
  if cur == 4:
    if c == "L":
      next = 1
    elif c == "D":
      next = 3
  return next



n = int(input())
k = int(input())

apple = []
for i in range(k):
  colx, coly = map(int, input().split())
  apple.append([colx-1, coly-1])

move = []
l = int(input())
total = 0
for s in range(l):
  x, d = map(str, input().split())
  prev = total
  total = int(x)
  divid = int(x) - prev
  move.append([divid,d])

#현재위치 2로 설정

cur = 1
board = [[0]*n for _ in range(n)]
for k in range (k):
  board[apple[k][0]][apple[k][1]] = 1


count = 0
moving = move[0][0]
check = 0

time = 0
pointer = [0,0]
tt = 0
back = deque ()
back.append([0,0])
moveList = moveF(cur)
while True:
  if check < moving or time >= total:
    if time == total:
      cur = direction(cur, move[tt][1])
      moveList = moveF(cur)
    check += 1
    time += 1
    nextPosx = pointer[0]+moveList[0]
    nextPosy = pointer[1]+moveList[1]
    if (nextPosx<0 or nextPosx >= n or nextPosy<0 or nextPosy >=n ):
      break
    else:
      pointer[0] = nextPosx
      pointer[1] = nextPosy
      back.append([nextPosx,nextPosy])
      if (board[nextPosx][nextPosy] == 1):
        board[nextPosx][nextPosy] = 2
      elif (board[nextPosx][nextPosy] == 2):
        break
      else:
        board[nextPosx][nextPosy] = 2
        board[back[0][0]][back[0][1]] = 0
        back.popleft()
        
  else:
    cur = direction(cur, move[tt][1])
    moveList = moveF(cur)
    if (tt+1 < l):
      check = 0
      moving = move[tt+1][0]
      tt += 1

print(time)

