#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib, sys, os, time
from datetime import datetime
from defMandrill import defMandrillRoot

def ftpBaglanti(filename):
	host = 'xxxxxxx'
	user = 'xxxxxxx'
	passw = 'xxxxxxx'
			
	try:
		ftp = ftplib.FTP(host, user, passw)
		print '*** FTP sunucuya bağlandı'
	except:
		sonuc = 'FTP error'
		print sonuc
		defMandrillRoot(sonuc,sonuc)	
		sys.exit()

	try: 
		#print ftp.retrlines('LIST')
		
		# ftp sunucudaki dosyanın tarihi
		datetimeftp = ftp.sendcmd('MDTM ' + filename) 
		# makinedeki dosyanın tarihi		
		datetimepc = os.path.getmtime('/home/python/xxxxxxx/fiyat_guncel/' + filename)
		
		modifiedTimeFtp = datetime.strptime(datetimeftp[4:], "%Y%m%d%H%M%S").strftime("%d %b %Y %H:%M:%S")
		modifiedTimePc = datetime.fromtimestamp(datetimepc).strftime("%d %b %Y %H:%M:%S")
		
		if modifiedTimeFtp > modifiedTimePc:
			#print modifiedTimeFtp
			#print modifiedTimePc
			#print "FTP deki dosya yenidir"
			# Sunucudaki dosyayı download ediyoruz
			localfile = open('/home/python/xxxxxxxxxx/fiyat_guncel/' + filename, 'wb')
			ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
			localfile.close()
						
			
		else:
			#print modifiedTimeFtp
			#print modifiedTimePc
			#print "Makinedeki deki dosya yenidir"
			sys.exit()
		print '*** Dosya bulundu : "%s"' % filename
	except:
		print '*** İşlem durdu. Dizindeki dosya tarihi büyük "%s"' % filename
		ftp.quit()
		sys.exit()
	else:
		print '*** Dosya indirildi : "%s"' % filename 
	ftp.quit()