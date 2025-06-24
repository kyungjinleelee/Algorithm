class Solution {
    public int solution(int n) {
        int sum = 0;
        
        if(n % 2 != 0) { // n이 홀수일 경우
            for (int i = 1; i <= n; i += 2) {
                sum += i;
            }
        } else { // n이 짝수일 경우
            for (int i = 2; i <= n; i += 2) {
                sum += i * i;
            }
        }
        return sum;
    }
}