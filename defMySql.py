#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb

def baglanti(barkod, fiyati, stok):
	# bağlantı
	conn = MySQLdb.connect (host = "xxxxxxxxxx",
    	                    user = "xxxxxxxxxx",
        	                passwd = "xxxxxxxxxx",
            	            db = "xxxxxxxxxx")
	cursor = conn.cursor ()
	
	# utf-8
	conn.set_character_set('utf8')
	cursor.execute('SET NAMES utf8;')
	cursor.execute('SET CHARACTER SET utf8;')
	cursor.execute('SET character_set_connection=utf8;')
	
	try:
		# sorgu
		cursor.execute ("""
							UPDATE urun_copy
							SET fiyati='%s', stok='%s'
   							WHERE barkod='%s'
						""",(fiyati, stok, barkod))
	
		conn.commit()
	except MySQLdb.Error as e:
		conn.rollback()
		
	
	
	
	#return join(yazdir)

	# kapat    
	cursor.close ()
	conn.close ()






