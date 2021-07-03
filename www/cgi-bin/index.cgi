#!/bin/sh
# vi: ft=sh

cd $(dirname $0)

printf "Content-type: text/html\n\n"

cat <<'EOF'
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>チャットルーム</title>
  </head>
  <body>
    <h1>チャットルーム</h1>
    <form action="/cgi-bin/post.cgi" method="POST">
      <input type="text" name="text" id="text" required autofocus>
      <input type="submit" value="書き込む">
    </form>
EOF

tail -n 100 < log           |  # ログから末尾を100行を読み込む
  awk '{print(NR, $0)}'     |  # 行頭に通し番号をつける
  sort -t ' ' -k 1nr        |  # 数の逆順でソート
  cut -d ' ' -f 2-          |  # 通し番号を除去する
  sed 's/^\(.*\)$/<p>\1<p>/'   # pタグをつける

cat <<'EOF'
  </body>
</html>
EOF
