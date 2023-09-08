import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class Algo03_선형구조2_ArrayList3_iterate {


	public static void main(String[] args) {
		
	// ArrayList 반복 출력
		List<String> x = new ArrayList<String>();
		x.add("C");
		x.add("C++");
		x.add("Java");
		x.add("Kotlin");
		x.add("Python");
		x.add("SQL");
		
		// 1. forEach문 ( Consumer ) ** 
		x.forEach(System.out::println);
		System.out.println();
		
		// 2. Iterator 이용 ==> 가장 첫 위치부터 다른위치로
		Iterator<String> ite = x.iterator();
		while(ite.hasNext()) {
			System.out.println(ite.next());
		}
		System.out.println();
		
		// 3. ListIterator ==> 시작 위치를 지정 가능. 역순으로도 접근 가능하다 (previous)
		ListIterator<String> ite2 = x.listIterator(x.size()); // 기본값은 0
	//	ListIterator<String> ite2 = x.listIterator(6); // 주의: idx 값이 아니고 위치값
		while(ite2.hasPrevious()) {
			System.out.println(ite2.previous());
		}
		
		// 4. foreach 문
		for (String s : x) {
			System.out.println(s);
			
		}
		
		// 5. 일반 for문 
		for(int i = 0; i< x.size(); i++) {
			System.out.println(x.get(i));
		}
	}
}
