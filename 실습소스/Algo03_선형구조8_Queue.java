import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.SortedMap;
import java.util.Stack;
import java.util.TreeMap;

public class Algo03_선형구조8_Queue {

	/*
	 * 	Queue
	 *  - FIFO ( First In First Out)
	 *  
	 *  - enqueue
	 *    dequeue
	 *  
	 *  삽입(저장) 관련 메서드 
	 *  가. add(값): 저장시 문제가 발생되면 예외가 발생
	 *  	offer(걊): 저장시 문제가 발생되면 false 리턴
	 *  
	 *  삭제 관련 메서드
	 *  가. remove(): 값이 없으면 예외가 발생됨 
	 *  	poll(): 값이 없으면 null 리턴
	 *  
	 *  *peek(): 가장 앞에 있는 front값 반환 
	 */

	public static void main(String[] args) {
	
		
		Queue<String> q = new LinkedList<>();
		q.add("A");
		q.add("B");
		q.add("C");
		q.add("D");
		q.add("E");

		System.out.println(q); // [A, B, C, D, E]
		System.out.println("peek: " + q.peek()); // peek: A (가장 처음에 있는 값 (front값))
		
		String str = q.remove();
		System.out.println(str + " " + q); // A [B, C, D, E]
		
		str = q.poll();
		System.out.println(str + " " + q); // B [C, D, E]
	}
}
