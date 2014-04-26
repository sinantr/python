#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb
from defSabitler import *

def baglanti(year, ay):
	# bağlantı
	conn = MySQLdb.connect (host = host,
    	                    user = user,
        	                passwd = passwd,
            	            db = db)
	cursor = conn.cursor ()
	
	# utf-8
	conn.set_character_set('utf8')
	cursor.execute('SET NAMES utf8;')
	cursor.execute('SET CHARACTER SET utf8;')
	cursor.execute('SET character_set_connection=utf8;')
	
	try:
		# sorgu
		cursor.execute ("""
							SELECT 
								SUM(toplam_ucret)
							FROM siparis_teslim 
							WHERE
								siparis_takip='2'
							AND
								YEAR(okdate)='%s'
							AND
								MONTH(okdate)='%s'
						""",(year, ay))
	
		result = cursor.fetchone ()

		if result[0] == None:
			return 0
		else:
			return result[0]
		
		conn.commit()
		
		
	except MySQLdb.Error as e:
		conn.rollback()
		
	
	

	# kapat    
	cursor.close ()
	conn.close ()






