import java.util.Arrays;
import java.util.Comparator;
import java.util.SortedMap;
import java.util.Stack;
import java.util.TreeMap;



public class Algo03_선형구조7_Stack2_API이용 {


	public static void main(String[] args) {
	
		Stack<Integer> x = new Stack<>();
		x.push(5);
		x.push(4);
		x.push(3);
		x.push(2);
		x.push(1);
		
		System.out.println(x); // [5, 4, 3, 2, 1]
		// 값을 제거하고 제거된 값을 반환
		int n = x.pop(); // 가장 마지막에 들어간 1이 삭제 
		System.out.println(n + " " + x); // 1 [5, 4, 3, 2] 
		
		System.out.println("top값(스택에서 가장 최상위값)"+ x.peek()); // 2
	}
}
