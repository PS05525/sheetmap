#!/usr/bin/python3.6
import cgi
import cgitb
from http import cookies

#日本語を処理するのに必要
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#デバッグ機能を有効にする
cgitb.enable()

print("Content-type: text/html;\n\n")
print("<html><body><TITLE>座席表 更新</TITLE><h1>更新完了</h1>\n")
print("<META http-equiv=Refresh content='10;URL=./index.cgi'>")
print("<br><br><br><A HREF=./index.cgi><B>TOP</B></A>")
print("</body></html>\n")
