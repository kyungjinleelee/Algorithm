import java.util.Arrays;

public class Solution {
    public static int[] solution(int[] num_list, int n) {
        int len = num_list.length;
        int[] answer = new int[len];

        // 뒤쪽 부분 복사 (n번째 이후)
        int index = 0;
        for (int i = n; i < len; i++) {
            answer[index++] = num_list[i];
        }

        // 앞쪽 부분 복사 (n번째까지)
        for (int i = 0; i < n; i++) {
            answer[index++] = num_list[i];
        }

        return answer;
    }
}
