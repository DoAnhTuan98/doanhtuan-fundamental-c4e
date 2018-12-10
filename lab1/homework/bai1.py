from gmail import GMail,Message
import datetime
now = datetime.datetime.now()


html_template = '''

<p>Ch&agrave;o sếp</p>
<p>S&aacute;ng nay em bị ốm</p>
<p>Sếp cho em xin nghỉ nh&eacute; y&ecirc;u sếp nhiều vcl :))</p>

'''
mail = GMail("doanhtuan7198@gmail.com","meoghetca998")
msg = Message("Nghỉ ốm",to="meoghetca98@gmail.com",html= html_template)
if now.hour > 7:
    mail.send(msg)
else:
    print("sếp vẫn đang ngủ không được gửi vào giờ này :))")