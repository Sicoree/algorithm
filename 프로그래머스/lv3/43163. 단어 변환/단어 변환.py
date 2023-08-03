from collections import deque

def solution(begin, target, words):
    if target not in words:
        answer = 0
    else:
        q = deque()
        q.append([begin, 0])
        visited = [0 for i in range(len(words))]
        while q:
            word, cnt = q.popleft()
            if word == target:
                answer = cnt
                break
            for i in range(len(words)):
                wcnt = 0
                if not visited[i]:
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            wcnt += 1
                    if wcnt == 1:
                        q.append([words[i], cnt + 1])
                        visited[i] = 1
    return answer