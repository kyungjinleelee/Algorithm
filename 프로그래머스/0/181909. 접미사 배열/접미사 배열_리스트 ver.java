import java.util.*;

class Solution {
    public List<String> solution(String my_string) {
        int n = my_string.length();
        List<String> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            answer.add(my_string.substring(i));
        }
        
        Collections.sort(answer);
        return answer;
    }
}
