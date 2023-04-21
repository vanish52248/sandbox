package com.example;

// AssertThat比較に必要なインポート
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;


// Testに必要な事前・事後・本処理・無視処理に必要なインポート
import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import org.junit.Ignore;

public class ScoreTest {
    @Before
    public void setUp() {
        /*
         * @Beforeアノテーションがついているメソッドは、各テストを実行するより前に毎回実行される
         * 何か共通系の処理などを行うために利用する
         */
        
        System.out.println("setUp!!!!!!!!!!!!!!!!!!!!");
    }

    @After
    public void termDown() {
        /*
         * @Afterアノテーションがついているメソッドは、各テストが実施された後に毎回実行される
         * Beforeで外部リソースを割り当てて、Afterで解放するといった方法で利用する
         */
        
        System.out.println("tearDown!!!!!!!!!!!!!!!!!!!!");
    }

    @Test
    @Ignore
    public void ignoreScore() {
        /*
         * @IgnoreアノテーションがついているメソッドはTestアノテーションがついていてもSkipされる
         * 何かしらの都合により、一時的にテストしたくない場合などに利用する
         */
        System.out.println("ignoreCase!!!!!!!!!!!!!!!!!!!!");
    }

    @Test
    public void cScore() {
        /*
         * 正常系試験
         */
        Score s = new Score();
        // 期待値
        String expected = "C";
        // 実際値
        String actual = s.judgeGrade(69);
        // 比較(期待値と実際値の比較結果がtrueであることを確かめる)
		assertThat(expected, is(actual));
    }

    @Test
    public void bScore() {
        /*
         * 正常系試験
         */
        Score s = new Score();
        // 期待値
        String expected = "B";
        // 実際値
        String actual = s.judgeGrade(79);
        // 比較(期待値と実際値の比較結果がtrueであることを確かめる)
		assertThat(expected, is(actual));
    }

    @Test
    public void aScore() {
        /*
         * 正常系試験
         */
        Score s = new Score();
        // 期待値 => C
        String expected = "C";
        // 実際値 => A
        String actual = s.judgeGrade(79);
        // 比較(期待値と実際値の比較結果がfalseであることを確かめる)
		assertThat(expected, is(not(actual)));
    }

    @Test
    public void nullScore() {
        /*
         * 正常系試験
         */
        Score s = new Score();
        // 実際値
        String actual = s.judgeGrade(91);
        // 比較(実際値とnullの比較結果がtrueであることを確かめる)
        assertThat(actual, nullValue());
    }

    @Test
    public void raiseScore1() {
        /*
         * 異常系試験
         */
        Score s = new Score();
        try {
            s.judgeGrade(-1);
        } catch (IllegalArgumentException e) {
            // 異常系メッセージの確認
            assertThat(e.getMessage(), is("score は 0点以上にするべきです。:" + -1));
        }
    }

    @Test
    public void raiseScore2() {
        /*
         * 異常系試験
         */
        Score s = new Score();
        try {
            s.judgeGrade(101);
        } catch (IllegalArgumentException e) {
            // 異常系メッセージの確認
            assertThat(e.getMessage(), is("score は 100点以下にするべきです。:" + 101));
        }
    }




}
