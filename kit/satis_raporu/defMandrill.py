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
<p><p><p><p><hr>
<small>
<b>Açıklama</b><br>
Bu rapor  tarafından otomatik oluşturulmuştur.<br>
Mobil cihazlar excel dosyasını ön görünümde gösterdiği için formül bulunan hücrelerin içeriğini göstermemektedir.<br>
Mobil cihazınıza uygun bir excel programı ile dosyaları açıp detaylarına bakabilirsiniz. 
</small>
""" %(tarih)

	name = '%s.xlsx' %(tarih)	
	
	title = "hedef/satış raporu # %s" %(tarih)
	mandrill_client = mandrill.Mandrill('NK8GagVptIwrdrnR9iGiig')
	message = {
	 'attachments': [{
	 				  'content' : content,
                      'name': name,
                      'type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                      }],
     'auto_html': None,
     'auto_text': None,
     'from_email': 'root@xxxxxx.com',
     'from_name': 'Kitap Kaynağı Sistem',
     'html': html,
     'inline_css': None,
     'preserve_recipients': None,
     'subject': title,
     'text': '',
     'to': [
     		{'email': 'mail',
             'name': 'name',
             'type': 'to'},
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
<p><p><p><p><hr>
<small>
<b>Açıklama</b><br>
Bu rapor  tarafından otomatik oluşturulmuştur.<br>
Mobil cihazlar excel dosyasını ön görünümde gösterdiği için formül bulunan hücrelerin içeriğini göstermemektedir.<br>
Mobil cihazınıza uygun bir excel programı ile dosyaları açıp detaylarına bakabilirsiniz. 
</small>
""" %(tarih)

	name = '%s.xlsx' %(tarih)	
	
	title = "hedef/satış raporu # %s" %(tarih)
	mandrill_client = mandrill.Mandrill('NK8GagVptIwrdrnR9iGiig')
	message = {
	 'attachments': [{
	 				  'content' : content,
                      'name': name,
                      'type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                      }],
     'auto_html': None,
     'auto_text': None,
     'from_email': 'root@xxxxxx.com',
     'from_name': 'Kitap Kaynağı Sistem',
     'html': html,
     'inline_css': None,
     'preserve_recipients': None,
     'subject': title,
     'text': '',
     'to': [
     		{'email': 'mail',
             'name': 'name',
             'type': 'to'},
             ],
     'view_content_link': None}
	result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool', send_at='2014-01-01 12:12:12')
	print result

	