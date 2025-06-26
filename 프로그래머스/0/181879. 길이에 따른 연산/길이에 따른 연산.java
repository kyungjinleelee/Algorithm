class Solution {
    public int solution(int[] num_list) {
        if (num_list.length >= 11) {
            int sum = 0;
            for (int num : num_list) {  // 길이가 11 이상이면 모든 원소의 합 반환
                sum += num;
            }
            return sum;
        } else {
            int product  = 1;
            for (int num : num_list) { // 10 이하이면 모든 원소의 곱 반환
                product *= num;
            }
            return product ;
        }
    }
}