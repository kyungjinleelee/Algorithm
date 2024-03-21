"""
로직
1. 양이 늑대보다 많으면 양의 수를 결과 배열에 저장한다 -> 양이 늑대보다 작거나 같으면 과정 끝냄 
2. edge 배열을 돌면서, 방문된 부모 노드와 방문되지 않은 자식 노드 정보가 있으면, 
 -a. 자식 노드에 방문 처리를 해주고 
 -b. 양 또는 늑대 수를 업데이트 하여 같은 과정을 c. 계속 반복 한다.
⇒ 로직 끝나면 ‘양의 수를 저장한 배열에서의 최댓값’이 모을 수 있는 양의 최댓값이 된다.

체크할 사항
- 양의 수가 늑대의 수보다 많은가?
- 부모 노드를 방문한 적이 있나?
- 자식 노드를 처음 방문한건가?
"""
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
