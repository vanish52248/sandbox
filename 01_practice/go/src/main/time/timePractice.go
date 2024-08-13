package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// 現在時刻
	now := time.Now()
	p("★ now: ", now)

	// 時刻を指定して作成
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p("★ then: ", then)

	// 以下作成した日時より一部だけ取得する場合に使用
	p("then-year:", then.Year())               //　年
	p("then-month: ", then.Month())            // 月
	p("then-day: ", then.Day())                // 日
	p("then-weekday: ", then.Weekday())        // 曜日
	p("then-hour: ", then.Hour())              // 時
	p("then-minute: ", then.Minute())          // 分
	p("then-second: ", then.Second())          // 秒
	p("then-nanoseconds: ", then.Nanosecond()) // ナノ秒
	p("then-location: ", then.Location())      // 時間基準

	// 以下のメソッドは2つの時刻を比べて、1つ目が2つ目より前か、後か、それとも同時刻かをそれぞれテストする。
	p("nowよりthenのほうが前か: ", then.Before(now))
	p("nowよりthenのほうが後か: ", then.After(now))
	p("nowとthenが同時刻か: ", then.Equal(now))

	// メソッド Sub は2つの時刻の間隔を表す経過時間 Duration を返す。
	diff := now.Sub(then)
	p("★ duration: ", diff)

	// 以下差分を取得した時間より経過時間を取得する場合に使用
	p("duration-hours: ", diff.Hours())             // 経過した時間
	p("duration-minutes: ", diff.Minutes())         // 経過した分
	p("duration-seconds: ", diff.Seconds())         // 経過した秒
	p("duration-nanoseconds: ", diff.Nanoseconds()) // 経過したナノ秒

	// Add を使って指定した期間だけ時刻を進めることもできる。- を使えば、時刻を戻すこともできる。
	p(now.Add(diff))
	p(then.Add(-diff))
}
