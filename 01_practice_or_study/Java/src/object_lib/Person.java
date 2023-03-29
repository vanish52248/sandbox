// clone()による複製をサポートしていることを外部に対して表明する為にjava.lang.Cloneableインタフェースを実装する必要がある。
public class Person implements Cloneable{
    private String name;
    private int age;

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String toString() {
        /*
         * Object毎に必ず持っているtoString()メソッドをオーバーライドすることで
         * System.out.println(p)などインスタンスのみを表示するときに、return の情報が返される
         * なので新規クラスごとにtoString()メソッドをオーバーライドしてよい
         * オーバーライド前 -> Person@6ff3c5b5
         * オーバーライド後 -> 名前：null; 年齢:0;
         */
        return "名前：" + this.name + "; 年齢:" + this.age + ";";
    }

    public boolean equals(Object o) {
        /*
         * Object毎に必ず持っているequals()メソッドをオーバーライドすることで
         * 等価判定アルゴリズムを作成できる
         * なので新規クラスごとにequals()メソッドのオーバーライドは必須
         */

        // ①自分自身が引数として渡されてきた場合、無条件でtrueを返す
        if (o == this) return true;
        // ②nullが引数として渡されてきた場合、無条件でfaliseを返す
        if (o == null) return false;
        // ③比較し、型が異なるならばfalseを返す
        // 　型が同じ場合は④に備えて比較できるように適切にキャストする
        if (!(o instanceof Person)) return false;
        Person p = (Person) o;
        // ④2つのインスタンスが持つしかるべきフィールド動詞を比較して等価か判定してtrue/falseを返す
        // 先頭と末尾の空白を取り除いた名前が正しければ投下とみなす
        if (!this.name.trim().equals(p.name.trim())) {
            return false;
        }
        return true;
    }

    public Person clone() {
        /*
         * Object毎に必ず持っているclone()メソッドをオーバーライドすることで
         * インスタンスの複製をすることができる
         * なので新規クラスごとにclone()メソッドをオーバーライドしてよい
         */
        Person result = new Person();
        result.name = this.name;
        result.age = this.age;
        return result;
    }
}
