import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final String N = sc.next();
        String[] numArray = new String[Integer.parseInt(N)];
    	for(int i = 0; i < numArray.length; i++) {
    		numArray[i] = sc.next();
    	}

        
        List<String> sl = new ArrayList<>();
        for (int i = 0; i < numArray.length; i++) {
            if (Integer.parseInt(numArray[i]) %2 == 0) {
                sl.add(numArray[i]);
            }
        }

        String res = String.join(" ",  sl);
        System.out.println(res);


        sc.close();
    }
}
