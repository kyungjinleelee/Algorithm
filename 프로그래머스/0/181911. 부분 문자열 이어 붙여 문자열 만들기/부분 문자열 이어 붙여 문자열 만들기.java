public class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < my_strings.length; i++) {
            String currentString = my_strings[i];
            int start = parts[i][0];
            int end = parts[i][1];
            
            // 부분 문자열 추출
            String substring = currentString.substring(start, end + 1);
            
            // 결과 문자열에 추가
            result.append(substring);
        }
        
        return result.toString();
    }
}