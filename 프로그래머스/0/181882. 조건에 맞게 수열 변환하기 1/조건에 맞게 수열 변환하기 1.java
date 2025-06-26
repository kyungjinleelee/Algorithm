class Solution {
    public int[] solution(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= 50 && arr[i] % 2 == 0) {
                arr[i] /= 2;
            } else if (arr[i] < 50 && arr[i] % 2 != 0) {
                arr[i] *= 2;
            }
        }
        return arr;
    }
}
// 주의:
// if문을 연속으로 쓰면, 한 원소가 두 번 변할 수 있다.
// 반드시 else if로 써서 if를 한 번만 타도록 해야 한다.