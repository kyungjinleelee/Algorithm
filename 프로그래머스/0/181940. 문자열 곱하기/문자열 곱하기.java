class Solution {
    public String solution(String my_string, int k) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < k; i++) {
            sb.append(my_string);
        }
        return sb.toString(); // toString()으로 문자열로 변환하여 반환
    }
}