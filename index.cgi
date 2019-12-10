#!/usr/bin/python3.6
import init
import cgi
import cgitb
from http import cookies

#日本語を処理するのに必要
#import sys
#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#デバッグ機能を有効にする
cgitb.enable()


#フォーム情報の取り込み
form = cgi.FieldStorage()

if len(form) == 0:
    CC=""
    C=""
else:
    CC=form["name"].value
    event=form["event"].value
    C = cookies.SimpleCookie()
    C["name"] = CC

#サンプル
print("Content-type: text/html;\n\n")
print("<html><body><h1>test cgi</h1>\n")
print("""
<br>
AAA<br>
BBB<br>
<hr>
CCC<br>
テスト表示<br>
<form id="form1" name="form1" method="post" action=index.cgi>
<br>
名前：<input type="text" name=name value="名前">
<input type="submit" value="更新">
<input type="hidden" name="event" value="mod">
<input type="hidden" name="num" value="24">
</form>
""")
print("<hr>入力内容<br>")
#フォームの内容を表示
print(f'名前：<b>',CC,"</b><br>")
print(C)
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="1">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="3">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="5">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="7">
</form>
<center><b>名前</b></center>
9174(2364)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="9">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="11">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="13">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="15">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="17">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="19">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="21">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
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
            <td bgcolor=#FFFFFF valign=top>
<form id="form1" name="form1" method="post" action=form_add.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="23">
</form>
<center><b>　</b></center>
XXXX(xxxx)
</td>
            <td bgcolor=#BAF1FC valign=top>
<form id="form1" name="form1" method="post" action=form_mod.html>
<input type="submit" value="登録">
<input type="hidden" name="event" value="addform">
<input type="hidden" name="num" value="24">
</form>
<center><b>名前</b></center>
XXXX(xxxx)
</td>
          </tr>
        </tbody>
      </table></td>
    </tr>
  </tbody>
</table>
""")
print("</body></html>\n")
