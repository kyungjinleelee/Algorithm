import java.util.Comparator;
import java.util.SortedMap;
import java.util.TreeMap;

public class Algo03_선형구조6_TreeMap {


	public static void main(String[] args) {
		
		// TreeMap 생성 ( 기본적으로 key 기준으로 오름차순 정렬됨 )
	//	TreeMap<String, String> m = new TreeMap<>(); // 대소문자 구별 된 오름차순 정렬 {A=AAA, B=BBB, E=EEE, ab=ab, c++=c++c++, d=ddd}
	//	TreeMap<String, String> m = new TreeMap<>(Comparator.reverseOrder()); // 대소문자 구별 된 내림차순 정렬 {d=ddd, c++=c++c++, ab=ab, E=EEE, B=BBB, A=AAA}
	//	SortedMap<String, String> m = new TreeMap<>(Comparator.reverseOrder()); // 위의 코드와 동일 (SortedMap은 해쉬맵의 부모)
		SortedMap<String, String> m = new TreeMap<>(String.CASE_INSENSITIVE_ORDER); // 대소문자 구별하지 않은 오름차순 정렬
		m.put("A", "AAA");
		m.put("ab", "ab");
		m.put("B", "BBB");
		m.put("c++", "c++c++");
		m.put("d", "ddd");
		m.put("E", "EEE");
		
		System.out.println(m);  // {A=AAA, ab=ab, B=BBB, c++=c++c++, d=ddd, E=EEE}
		
			// 아스키 코드 값 ==> A: 65, a: 97
		
		
		
	}
}
