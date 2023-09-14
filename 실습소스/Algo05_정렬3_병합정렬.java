import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;


public class Algo05_정렬3_병합정렬 {
	
	

		// 정렬할 메서드
		public static void merge_sort(int [] arr, int left, int right) {
			
			// 갯수가 1인 경우 ==> 더 이상 분할이 불가능하기 때문에 중단 
			if(left == right) return;
			
			int mid = (left+right)/2;
			
			System.out.println(Arrays.toString(Arrays.copyOfRange(arr, left, mid+1))+" " 
			+ Arrays.toString(Arrays.copyOfRange(arr, mid+1, right+1)) );
			merge_sort(arr, left, mid); // 왼쪽 서브 배열  8,2,6,4
			merge_sort(arr, mid+1, right); // 왼쪽 서브 배열  7,3,9,5
			
			// 병합(conquer)
			merge(arr, left, mid, right);
		}
		
		
		// 병합 (conquer)하는 메서드
		// 정렬하면서 병합할 때 필요한 임시 배열
		static int [] sorted = null;
		public static void merge(int [] arr, int left, int mid, int right) {
			
			sorted = new int [arr.length];
			
			// 변수에 저장
			int l = left; // 왼쪽 부분배열의 시작점 
			int r = mid + 1; // 오른쪽 부분배열의 시작점
			int idx = left; // sorted 배열에 저장하기 위한 인덱스 
			
			while(l <= mid && r <= right) {
				// 왼쪽 배열과 오른쪽 배열 비교해서 작은 값을 sorted에 저장시킨다.
				if(arr[l] <= arr[r]) {
					sorted[idx]=arr[l];
					idx++;
					l++;
				}else {
					sorted[idx]=arr[r];
					idx++;
					r++;
				}
			}//end while	
			if(l > mid) { // l > mid 는 왼쪽 배열이 먼저 모두 sorted 배열에 채워진 경우
				// 오른쪽 배열이 남아있는 경우
				while(r <= right) {
					sorted[idx]=arr[r];
					idx++;
					r++;
				}
			}else {   // r > right 는 오른쪽 배열이 먼저 모두 sorted 배열에 채워진 경우
			// 왼쪽 배열이 남아있는 경우
				while(l <= mid ) {  
					sorted[idx]=arr[l];
					idx++;
					l++;
				}
			}
			// 임시배열값을 원본 배열에 복사하기
			 for(int i=left; i <= right; i++) {
				 arr[i]= sorted[i];
			  }
		}// end merge
		
		// 정렬할 데이터 저장 
		static int [] arr = {8,2,6,4,7,3,9,5};
		
		public static void main(String[] args) {
		     
			merge_sort(arr, 0, arr.length-1);
			
			// 정렬된 값 출력
			for(int x: arr) {
				System.out.print(x+" "); // 1 2 3 4 5 6 7 8 9 
			}
			System.out.println(Arrays.toString(sorted));
			
	}// end main
}// end class
