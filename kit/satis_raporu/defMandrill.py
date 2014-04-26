#!/usr/bin/env python
# -*- coding: utf-8 -*-


import mandrill
from datetime import date

def defMandrillUser(content):
	tarih = date.today()
	tarih = tarih.strftime('%d-%m-%Y')
	html = """%s tarihli hedef/satış raporudur.
<p>
Rapora ekteki excel dosyasından ulaşabilirsiniz.<p>
Saygılarımızla.<br>
www.kitapkaynagi.com
<p><p><p><p><hr>
<small>
<b>Açıklama</b><br>
Bu rapor kitapkaynagi.com tarafından otomatik oluşturulmuştur.<br>
Mobil cihazlar excel dosyasını ön görünümde gösterdiği için formül bulunan hücrelerin içeriğini göstermemektedir.<br>
Mobil cihazınıza uygun bir excel programı ile dosyaları açıp detaylarına bakabilirsiniz. 
</small>
""" %(tarih)

	name = 'kitapkaynagi_%s.xlsx' %(tarih)	
	
	title = "kitapkaynagi.com hedef/satış raporu # %s" %(tarih)
	mandrill_client = mandrill.Mandrill('NK8GagVptIwrdrnR9iGiig')
	message = {
	 'attachments': [{
	 				  'content' : content,
                      'name': name,
                      'type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                      }],
     'auto_html': None,
     'auto_text': None,
     'from_email': 'root@kulturyayinlari.com',
     'from_name': 'Kitap Kaynağı Sistem',
     'html': html,
     'inline_css': None,
     'preserve_recipients': None,
     'subject': title,
     'text': '',
     'to': [
     		{'email': 'cihan.okan@isikyayinlari.com',
             'name': 'Cihan Okan',
             'type': 'to'},
             {'email': 'mahmut.yalcin@isikyayinlari.com',
             'name': 'Mahmut Yalçın',
             'type': 'cc'},
			{'email': 'ali.cetintas@isikyayinlari.com',
             'name': 'Ali Çetintaş',
             'type': 'cc'},
			{'email': 'ozden.demir@isikyayinlari.com',
             'name': 'Özden Demir',
             'type': 'cc'}
             ],
     'view_content_link': None}
	result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool', send_at='2014-01-01 12:12:12')
	print result

def defMandrillRoot(content):
	tarih = date.today()
	tarih = tarih.strftime('%d-%m-%Y')
	html = """%s tarihli hedef/satış raporudur.
<p>
Rapora ekteki excel dosyasından ulaşabilirsiniz.<p>
Saygılarımızla.<br>
www.kitapkaynagi.com
<p><p><p><p><hr>
<small>
<b>Açıklama</b><br>
Bu rapor kitapkaynagi.com tarafından otomatik oluşturulmuştur. 
</small>
""" %(tarih)

	name = 'kitapkaynagi_%s.xlsx' %(tarih)	
	
	title = "kitapkaynagi.com hedef/satış raporu # %s" %(tarih)
	mandrill_client = mandrill.Mandrill('NK8GagVptIwrdrnR9iGiig')
	message = {
	 'attachments': [{
	 				  'content' : content,
                      'name': name,
                      'type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                      }],
     'auto_html': None,
     'auto_text': None,
     'from_email': 'root@kulturyayinlari.com',
     'from_name': 'Kitap Kaynağı Sistem',
     'html': html,
     'inline_css': None,
     'preserve_recipients': None,
     'subject': title,
     'text': '',
     'to': [
     		{'email': 'asinan@kulturyayinlari.com',
             'name': 'Aydın Sinan',
             'type': 'to'},
             {'email': 'umayumay@gmail.com',
             'name': 'Recep Umay',
             'type': 'to'}
             ],
     'view_content_link': None}
	result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool', send_at='2014-01-01 12:12:12')
	print result
	
	