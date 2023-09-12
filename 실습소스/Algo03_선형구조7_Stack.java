import java.util.Arrays;
import java.util.Comparator;
import java.util.SortedMap;
import java.util.TreeMap;

class MyStack{
	
	int top; // stack의 가장 최상단
	int size;
	int [] stack;
	
	public MyStack(int size) {
		this.size = size;
		stack = new int[size];
		top = -1;
	}
	
	// 저장: top 증가하고 값 저장하는 메서드
	public void push(int n) {
		++top;
		stack[top] = n;
		System.out.println(stack[top]+ " Push~");
	}
	
	// 삭제: 값 제거하고 top 감소시키는 메서드
	public void pop() {
		if(top>=0)
		System.out.println(stack[top]+ " pop~");
		stack[top--] = 0;
	}
	
	// 현재 top에 있는 값 반환해주는 메서드 
	public int peek() {
		return stack[top];
	}
	
}// end class

public class Algo03_선형구조7_Stack {


	public static void main(String[] args) {
	
		MyStack x = new MyStack(5);
		x.push(5);
		x.push(4);
		x.push(3);
		x.push(2);
		x.push(1);
		
		System.out.println(Arrays.toString(x.stack));
		System.out.println(x.peek());
		
		for(int i = 0; i< x.size; i++) {
			x.pop();
		}
		
	}
}
