import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Algo03_선형구조1_배열2 {


	public static void main(String[] args) {
		
		// Arrays 클래스
		
		// 1. 리스트 생성  ( Arrays.asList )
		List<String> list = Arrays.asList("A", "B");
		
		// 2. 임의 값으로 채우기 ( fill )
		String [] name = {"A", "B", "C"};
		Arrays.fill(name, "x");
		System.out.println("2. 임의값으로 채우기: " + Arrays.toString(name)); // [x, x, x]
		
		Arrays.fill(name, 0, 2, "a");
		System.out.println("2. 일부분 임의값으로 채우기: " + Arrays.toString(name)); // [a, a, x]
	
		// 3. 배열값 비교 ( equals )
		int [] n = {1, 2, 3};
		int [] n2 = {1, 2, 3};
		System.out.println("3. 배열값 비교: " + Arrays.equals(n, n2)); // true
		
		// 4. 정렬 ( sort )
	//	int [] n3 = { 6, 2, 7, 98, 24};
		Integer [] n3 = { 6, 2, 7, 98, 24};
		Arrays.sort(n3); // 기본은 오름차순 
		Arrays.sort(n3, Comparator.reverseOrder()); // 내림차순
		// Comparator.reverseOrder() 사용하기 위해서는 클래스타입이어야 함. (상단의 int -> Integer 로 변경)
		System.out.println("4. 정렬: " + Arrays.toString(n3)); // [2, 6, 7, 24, 98]
	
		// 5. 특정 값의 위치 검색 ( binarySearch() ) 
		Integer [] n4 = { 6, 2, 7, 98, 24};
		int idx = Arrays.binarySearch(n4, 98);
		System.out.println("5. 특정 값의 위치 검색: " + idx); // 3
		
		// 6. 배열 크기 변경 (원래는 배열 크기 변경 안됨 !! ) ( Arrays.copyOf() )
		int [] n5 = {1, 2, 3};
		n5 = Arrays.copyOf(n5, 5); // 늘어났을 때 빈 값은 기본값(0)으로 채워짐
		System.out.println("6. 배열 크기 변경: " + Arrays.toString(n5)); // [1, 2, 3, 0, 0]

		// 7. 배열에서 자바 스트림 생성
		int [] n6 = {1, 2, 3};
		Arrays.stream(n6)
			  .forEach(System.out::println); // 1 2 3 
	}
}
