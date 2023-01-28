# Ubuntu環境でのノウハウ

## systemctl コマンド使用できない
```
# genieディレクトリ がある階層(ホームディレクトリ)でコマンド実行
$ cd
$ genie -s
```

## mariadb 起動方法
```
systemctl start mariadb
systemctl status mariadb
sudo mariadb
```

## jupyter notebook起動方法
```
# sandbox/01_practice_or_study/jupyters/配下にjupyter notebook作成モジュール配置
$ cd ~/sandbox/01_practice_or_study/jupyters/
$ jupyter notebook --NotebookApp.use_redirect_file=False
```
