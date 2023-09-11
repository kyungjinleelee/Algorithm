import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

public class Algo03_선형구조3_LinkedList {


	public static void main(String[] args) {
		
		// LinkedList 생성 ( ArrayList 보다 삽입/삭제가 효율적 ) 
		LinkedList<String> list = new LinkedList<>();
		list.add("A1");
		list.add("A2");
		list.add("A3");
		
		list.add(0, "B"); // 0번째 idx에 삽입
		list.addFirst("C");
		list.addLast("D");
		System.out.println(list); // [C, B, A1, A2, A3, D]
		
		// 삭제
		String str = list.removeFirst(); // [B, A1, A2, A3, D]
		str = list.removeLast();		// [B, A1, A2, A3]
		boolean b = list.remove("A1"); //  [B, A2, A3]
		list.removeIf(x->x.startsWith("A")); // [B]
		System.out.println(list);
		
		// iterate는 ArrayList와 동일
		
		
	}
}
