def solution(tickets):
    
    tickets.sort(key = lambda x : (x[0], x[1]))
    
    def DFS(ticket, result):
        if len(ticket) == 0:
            return result
        
        now = result[-1]
        next_idx = -1
        
        for i in range(len(ticket)):
            if ticket[i][0] == now:
                next_idx = i
                break
        
        if next_idx == -1:
            return []
        
        while ticket[next_idx][0] == now:
            nx = DFS(ticket[:next_idx] + ticket[next_idx + 1:], result + [ticket[next_idx][1]])
            
            if nx != []:
                return nx
            next_idx += 1
        
        return []
    
    return DFS(tickets, ["ICN"])