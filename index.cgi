#!/usr/bin/python3.6
import cgi
import cgitb
from http import cookies

#���{�����������̂ɕK�v
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#�f�o�b�O�@�\��L���ɂ���
cgitb.enable()

#�t�H�[�����̎�荞��
form = cgi.FieldStorage()

if len(form) == 0:
    CC=""
    C=""
else:
    CC=form["name"].value
    event=form["event"].value
#    print("Set-Cookie: NAME="+CC)
    C = cookies.SimpleCookie()
    C["name"] = CC

#�T���v��
print("Content-type: text/html;\n\n")
print("<html><body><h1>test cgi</h1>\n")
print("""
<br>
AAA<br>
BBB<br>
<hr>
CCC<br>
�e�X�g�\��<br>
<form id="form1" name="form1" method="post" action=test.py>
<br>
���O�F<input type="text" name=name value="���O">
<input type="submit" value="�X�V">
<input type="hidden" name="event" value="mod">
<input type="hidden" name="num" value="24">
</form>
""")
print("<hr>���͓��e<br>")
#�t�H�[���̓��e��\��
print(f'���O�F<b>',CC,"</b><br>")
print(C)
print("</body></html>\n")