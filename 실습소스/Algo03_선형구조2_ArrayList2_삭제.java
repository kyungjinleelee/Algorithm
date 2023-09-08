import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Algo03_선형구조2_ArrayList2_삭제 {


	public static void main(String[] args) {
		
		// ArrayList 삭제
		List<String> x = new ArrayList<String>();
		x.add("C");
		x.add("C++");
		x.add("Java");
		x.add("Kotlin");
		x.add("Python");
		x.add("SQL");
		
		String str = x.remove(5); // idx로 삭제 
		
		System.out.println(str);		// SQL
		
		boolean b = x.remove("Kotlin"); // value 이용
		System.out.println(b);	// true
		
		x.removeIf(s -> s.startsWith("C")); // C로 시작하는 값들 삭제
		System.out.println(x);	// [Java, Python]
		
		// 삭제할 값을 List에 저장하고 이 List값을 이용해서 삭제
		List<String> x2 = new ArrayList<String>();
		x2.add("Java");
		
		x.removeAll(x2); // x 에서 x2값을 삭제해라!
		System.out.println(x);	// [Python]

	}
}
