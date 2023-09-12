import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.SortedMap;
import java.util.Stack;
import java.util.TreeMap;

public class Algo03_선형구조9_PriorityQueue {

	public static void main(String[] args) {
	
		PriorityQueue<Integer> q = new PriorityQueue<>();
		q.add(5);
		q.add(15);
		q.add(6);
		q.add(42);
		q.add(4);
		q.add(1);
				
		System.out.println(q); // [1, 5, 4, 42, 15, 6] 랜덤하게 저장됨
		
		// 삭제될 때 정렬되어 삭제된다.
		for(int i=0; i<5; i++) {
			System.out.println(q.poll());
		}
		
	}
}
