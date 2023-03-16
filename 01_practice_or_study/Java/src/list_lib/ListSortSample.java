import java.util.Arrays;
import java.util.Collections;

public class ListSortSample {
    public static void main(String[] args) {

        // 昇順用のリスト
        int[] lists = {10, 50, 30, 20, 200, 120, 35};

        // 降順用のリスト Collectionsクラスを使用する場合はInteger使用する
        // int がプリミティブ型であるのに対し， Integer は整数型を扱うクラスになります。
        // ただの型である int と異なり， Integer には様々な関数が実装されています． そのため，これらの関数を呼び出したい場合は Integer を利用する必要があります．
        Integer[] lists2 = {10, 50, 30, 20, 200, 120, 35};

        ListSortSample m = new ListSortSample();

        // 昇順処理
        int[] s = m.sampleAskArrays(lists);
        // 配列の中身を出力する場合はArrays.toString()を使用
        System.out.println(Arrays.toString(s));

        // 降順処理
        Integer[] s2 = m.sampleDeskArrays(lists2);
        // 配列の中身を出力する場合はArrays.toString()を使用
        System.out.println(Arrays.toString(s2));
    }
    
    // 昇順ソートメソッド
    private int[] sampleAskArrays(int[] ar) {
        Arrays.sort(ar);
        return ar;
    }

    // 降順ソートメソッド
    private Integer[] sampleDeskArrays(Integer[] ar) {
        Arrays.sort(ar, Collections.reverseOrder());
        return ar;
    }
}
