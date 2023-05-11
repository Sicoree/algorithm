def solution(A, B):
    answer = 0
    l = len(A)
    A.sort()
    B.sort()
    
    for idx in range(l):
        answer += A[idx] * B[l - idx - 1]

    return answer