def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()
    
    arr = [540 + t * i for i in range(n)]
    
    idx = 0
    for t in arr:
        cnt = 0
        while cnt < m and idx < len(timetable) and timetable[idx] <= t:
            idx += 1
            cnt += 1
        if cnt < m:
            answer = t
        else:
            answer = timetable[idx - 1] - 1
    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)