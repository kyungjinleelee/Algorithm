import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Algo03_선형구조4_HashMap {


	public static void main(String[] args) {
		
		// HashMap 생성 ( 기본적으로 저장순서 유지 안함 )
		Map<String, String> m = new HashMap<String, String>();
		m.put("A", "AAA");
		m.put("B", "BBB");
		m.put("C", "CCC");
		
		// iterate
		// 1. m.forEach (Consumer)
		m.forEach((key, value) -> System.out.println(key+"="+value));
		System.out.println();
		// 2. key값.forEach(Consumer)
		m.keySet().forEach(key -> System.out.println(key+"="+m.get(key)) );
	}
}
