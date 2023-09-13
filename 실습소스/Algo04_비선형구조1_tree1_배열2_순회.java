import java.util.Scanner;

/*
 *  	 0
 *     /   \
 *    1     2
 *   / \     \
 *  3   4     5
 *  
 *  입력:
 *  	6
 *  	0  1  2
 *  	1  3  4
 *  	2 -1  5
 *   	3 -1 -1
 *   	4 -1 -1
 *   	5 -1 -1
 */
public class Algo04_비선형구조1_tree1_배열2_순회 {
	
	static int n; // 노드의 개수
	static int [][] tree; // 노드를 저장하기 위한 2차원 배열
	

	public static void main(String[] args) {
	
	Scanner sc = new Scanner(System.in);
	// 노드 갯수를 사용자가 입력
	n = sc.nextInt();
	
	// 2차원 배열 생성
	tree = new int[n][2]; // 2진 트리니까 열의 개수는 2로 지정, [n][0]은 왼쪽 자식, [n][1]은 오른쪽 자식
	
	for(int i = 0; i<n; i++) {
		int x = sc.nextInt(); // 0
		int l_child = sc.nextInt(); // 1
		int r_child = sc.nextInt(); // 2
		tree[x][0] = l_child; // 0은 왼쪽값 
		tree[x][1] = r_child; // 1은 오른쪽값
	}
	
	// 배열 출력
	for(int i = 0; i<tree.length; i++) {
		for(int j = 0; j<tree[i].length; j++) {
			System.out.println(i + "값의 자식:" + tree[i][j]);
		}
	}
	
	//순회 : 재귀함수 이용
	order(0);

	}
	
	 //순회
		private static void order(int x) {
			
			//자식여부 확인
			if(tree[x][0]==-1 && tree[x][1]==-1) {//자식이 없는 경우
				System.out.print(x + " ");
				
			}else {  // 자식이 있는 경우			
//				System.out.print("전위:"+ x + " "); // 0 1 3 4 2 5 
				if(tree[x][0]!=-1) { //왼쪽 자식이 있는 경우
					order(tree[x][0]);
				}
//				System.out.print("중위:"+ x + " "); // 3 1 4 0 2 5 
		        if(tree[x][1]!=-1) { //오른쪽 자식이 있는 겨우
		        	order(tree[x][1]);
				}
		        System.out.print("후위"+ x + " "); // 3 4 1 5 2 0 
			}
			
		}//end order
}
