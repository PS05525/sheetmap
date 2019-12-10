#!/usr/bin/python3.6
import init
import cgi
import cgitb
import csv
from http import cookies

#日本語を処理するのに必要
#import sys
#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#デバッグ機能を有効にする
cgitb.enable()


#フォーム情報の取り込み
form = cgi.FieldStorage()

#データファイルを変数に置き換え
with open('/var/www/cgi-bin/seatmap.txt') as f:
   reader = csv.reader(f)
   data = [row for row in reader]

if len(form) == 0:
    CC=""
    C=""
else:
    CC=form["name"].value
    event=form["event"].value
    C = cookies.SimpleCookie()
    C["name"] = CC

#データ判定および必要変数追加
cnt=0
for line in data:
   if len(line[1]) == 0:
      CGI="add.cgi"
      FORM="登録"
      COLOR="#FFFFFF"
      NAME=""
      data[cnt]=data[cnt][0],data[cnt][2],data[cnt][1],CGI,FORM,COLOR,NAME
      cnt=cnt + 1
   else:
      CGI="mod.cgi"
      FORM="更新"
      COLOR="#BAF1FC"
      NAME=line[1]
      data[cnt]=data[cnt][0],data[cnt][2],data[cnt][1],CGI,FORM,COLOR,NAME
      cnt=cnt + 1

#サンプル
print("Content-type: text/html;\n\n")
print("<html><body><TITLE>ITSS座席表</TITLE>\n")
print("""
<table width="200" border="0">
  <tbody>
    <tr>
      <td valign="bottom"><table width="200" border="1">
        <tbody>
          <tr>
            <td colspan=2 bgcolor=#BAF1FC><center><b>杉崎</b></center>03-5828-XXXX(xxxx)</td>
          </tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="1">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
      <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="2">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="3">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="4">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="5">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="6">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="7">
</form>
<center><b>名前</b></center>
9174(2364)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="8">
</form>
<center><b>名前</b></center>
9174(2364)
</td>
          </tr>
        </tbody>
      </table>
      </td>
      <td valign="bottom"><table width="200" border="1">
        <tbody>
          <tr>
            <td colspan=2 bgcolor=#BAF1FC><center><b>星野</b></center>03-5828-XXXX(xxxx)</td>

          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="9">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="10">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="11">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="12">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="13">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="14">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="15">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="16">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
        </tbody>
      </table></td>
      <td valign="bottom"><table width="200" border="1">
        <tbody>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="17">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="18">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="19">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="20">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="21">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="22">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
          <tr>
          <tr>
""")
print("""
            <td bgcolor=#FFFFFF valign=top>
<form id="form1" name="form1" method="post" action=form_add.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="23">
</form>
<center><b>　</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="24">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          <tr>
""")
print("""
          </tr>
        </tbody>
      </table></td>
    </tr>
  </tbody>
</table>
""")
print("</body></html>\n")
