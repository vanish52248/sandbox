import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int d = sc.nextInt();
        int[] numArray = new int[n];
    	for(int i = 0; i < n; i++) {
    		numArray[i] = sc.nextInt();
    	}
        

        int temp = numArray[0];
        for (int i = 1; i < n; i++) {
            int ans = Math.abs(temp - numArray[i]);
            if (ans <= d) {
                System.out.println(numArray[i]);
                return;
            }
            temp = numArray[i];
        }
        System.out.println(-1);
    }
}
