class Solution {
    public int[] solution(int n, int k) {
        // 1. k의 배수 개수 세기
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                cnt++;
            }
        }
        
        // 2. 결과 배열 생성
        int[] answer = new int[cnt];
        int idx = 0;
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                answer[idx++] = i;
            }
        }
        return answer;
    }
}
