def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p_node, c_node in edges:
            # 부모노드는 방문되고 자식노드는 아니라면, 자식 노드 방문처리 
            if visited[p_node] and not visited[c_node]: 
                visited[c_node] = 1
                
                # 자식 노드가 양인지 늑대인지 확인
                # 양이면 양의 수 1 증가시켜서 dfs 재귀호출
                # 늑대면 늑대 수 1 증가시켜서 dfs 재귀호출
                if info[c_node] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                    
                # 되돌아가기 위해 자식 노드를 미방문 처리
                visited[c_node] = 0
                
    # default            
    # 루트 노드는 방문한 것으로 설정
    # 초기 양 수는 1, 늑대 수 0인 상태에서 dfs 시작
    visited[0] = 1
    dfs(1, 0)
    
    return max(answer)