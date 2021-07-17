#!/bin/sh
# vi: ft=sh

cd $(dirname $0)
tmp="$(mktemp -d)"
handleName=$(echo $HTTP_COOKIE| get_handle_name| uri_decode)

printf "Content-type: text/html\n\n"

cat <<EOF
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>チャットルーム</title>
  </head>
  <body>
    <h1>チャットルーム</h1>
    <p>${handleName}さんとして入室中</p>
    <form action="/cgi-bin/post.cgi" method="POST">
      <input type="text" name="text" id="text" required autofocus>
      <input type="submit" value="書き込む">
    </form>
EOF

tail -n 100 < log           |  # ログから末尾を100行を読み込む
  awk '{print(NR, $0)}'     |  # 行頭に通し番号をつける
  sort -t ' ' -k 1nr        |  # 数の逆順でソート
  cut -d ' ' -f 2-          |  # 通し番号を除去する
  cat > "${tmp}"/last100

cut -d ',' -f 1 < "${tmp}"/last100 |
  uri_decode |
  while read -r l; do
    /usr/bin/printf '<p>[%s]\n' "${l}"
  done > "${tmp}"/name

cut -d ',' -f 2- < "${tmp}"/last100 |
  sed 's/^\(.*\)$/\1<\/p>/' > "${tmp}"/message

paste "${tmp}"/name "${tmp}"/message

cat <<'EOF'
  </body>
</html>
EOF

rm -rf "${tmp}"
