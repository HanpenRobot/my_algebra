# TIPS
+ pythonでgifをアニメーションを作る際に
```python
# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save("projective_line_plot.gif", writer="imagemagick")
```
のような実装をしている。この"imagemagick"とは何者なのか参考文献[1]に基づいて説明する。

[imagemagick](https://imagemagick.org/)とはGPL準拠のオープンソースソフトウェアである。
imagemagickを使うとgifファイルを連結して保存できる。

[cygwin64 Terminalにパッケージ管理ツールapt-cygを入れるときに参考にしたサイト](https://qiita.com/FSMS/items/68b5956301d987d1be2b)



```bash
apt-cyg install opengl freeglut-devel gcc-g++ make
```

- 参考文献[1] C#で学ぶ偏微分方程式の数値解法 CAEプログラミング入門 平瀬創也 東京電機大学出版局 2009年 第1版1刷発行, pp.162-163 (付録D アニメーションの作り方)

