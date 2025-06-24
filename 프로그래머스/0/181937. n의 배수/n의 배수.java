class Solution {
    public static int solution(int num, int n) {
        if(num % n == 0) {
            return 1;
        } else {
            return 0;
        }
        // return num % n == 0 ? 1 : 0;
    }
}