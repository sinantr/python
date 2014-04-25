#!/usr/bin/env python
# -*- coding: utf-8 -*-


import mandrill
from datetime import date

def defMandrillRoot(html,subject):
	
	tarih = date.today()
	tarih = tarih.strftime('%d-%m-%Y')
	title = "%s %s" %(subject,tarih)
	mandrill_client = mandrill.Mandrill('xxxxxxxxxx')
	message = {
     'auto_html': None,
     'auto_text': None,
     'from_email': 'xxxxxxxxxx',
     'from_name': 'xxxxxxxxxx',
     'html': html,
     'inline_css': None,
     'preserve_recipients': None,
     'subject': title,
     'text': '',
     'to': [
     		{'email': 'xxxxxxxxxx',
             'name': 'xxxxxxxxxx',
             'type': 'to'},
			{'email': 'xxxxxxxxxx',
             'name': 'xxxxxxxxxx',
             'type': 'to'} 
             ],
     'view_content_link': None}
	result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool', send_at='2014-01-01 12:12:12')
	print result


def defMandrillUser(html,subject):
	
	tarih = date.today()
	tarih = tarih.strftime('%d-%m-%Y')
	title = "xxxxxxxxxx DB güncellendi # %s" %(tarih)
	mandrill_client = mandrill.Mandrill('xxxxxxxxxx')
	message = {
     'auto_html': None,
     'auto_text': None,
     'from_email': 'xxxxxxxxxx',
     'from_name': 'xxxxxxxxxx',
     'html': html,
     'inline_css': None,
     'preserve_recipients': None,
     'subject': subject,
     'text': '',
     'to': [
     		{'email': 'xxxxxxxxxx',
             'name': 'xxxxxxxxxx',
             'type': 'to'},
             {'email': 'xxxxxxxxxx',
             'name': 'xxxxxxxxxx',
             'type': 'to'}
             ],
     'view_content_link': None}
	result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool', send_at='2014-01-01 12:12:12')
	print result