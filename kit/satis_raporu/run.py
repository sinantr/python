#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#
# Copyright 2014-04
#

from defSabitler import *
import xlsxwriter
# file attachments için buna ihtiyacımız var. 
import base64 
import defMandrill, defMySql



######################################################################
# Excel’i oluşturuyoruz. 
######################################################################
workbook = xlsxwriter.Workbook('%s%s' %(filenameDirectory,filenameReport))
worksheet = workbook.add_worksheet()

# Cell uzunluğu : (B ile D arasındaki hücrelerin arasındaki genişlik weight = 20) 
worksheet.set_column('A:D', 20)


cell_format_1 = workbook.add_format({
	'bold': 1,
	'bg_color' :'#8CB4E2',
	'align' : 'center',
	'valign' : 'vcenter',
	'font_size' : 16,
	'border' : 1
	})

cell_format_2 = workbook.add_format({
	'bold': 1,
	'bg_color' :'#8CB4E2',
	'align' : 'left',
	'valign' : 'vcenter',
	'font_size' : 16,
	'border' : 1
	})

cell_format_3 = workbook.add_format({
	'bold': 0,
	'align' : 'right',
	'valign' : 'vcenter',
	'font_size' :16,
	'border' : 1,
	'num_format' : '#,##0.00'
	})

cell_format_4 = workbook.add_format({
	'bold': 1,
	'bg_color' :'#8CB4E2',
	'align' : 'center',
	'valign' : 'vcenter',
	'font_size' : 16,
	'border' : 1
	})



# Cell yüksekliği : (10 uncu satırdan başla, height = 150 olsun)
worksheet.set_row(0, 37)
worksheet.set_row(2, 34)
worksheet.set_row(3, 34)
worksheet.set_row(4, 34)
worksheet.set_row(5, 34)
worksheet.set_row(6, 34)
worksheet.set_row(7, 34)
worksheet.set_row(8, 34)
worksheet.set_row(9, 34)
worksheet.set_row(10, 34)
worksheet.set_row(11, 34)
worksheet.set_row(12, 34)
worksheet.set_row(13, 34)
worksheet.set_row(14, 34)
worksheet.set_row(15, 34)

# Create a format to use in the merged range.
merge_format = workbook.add_format({
    'bold': 1,
    'align': 'center',
    'valign': 'vcenter',
    'font_size':24
    })




# Başlık
worksheet.merge_range('A1:D1', u'Kitap Kaynağı Satış Takip Raporu', merge_format)

# A Sütunu
worksheet.write('A3', u'AYLAR', cell_format_4)
worksheet.write('B3', u'HEDEF', cell_format_4)
worksheet.write('C3', u'GERÇEKLEŞEN', cell_format_4)
worksheet.write('D3', u'YÜZDE', cell_format_4)
worksheet.write('A4', u'Ocak', cell_format_2)
worksheet.write('A5', u'Şubat', cell_format_2)
worksheet.write('A6', u'Mart', cell_format_2)
worksheet.write('A7', u'Nisan', cell_format_2)
worksheet.write('A8', u'Mayıs', cell_format_2)
worksheet.write('A9', u'Haziran', cell_format_2)
worksheet.write('A10', u'Temmuz', cell_format_2)
worksheet.write('A11', u'Ağustos', cell_format_2)
worksheet.write('A12', u'Eylül', cell_format_2)
worksheet.write('A13', u'Ekim', cell_format_2)
worksheet.write('A14', u'Kasım', cell_format_2)
worksheet.write('A15', u'Aralık', cell_format_2)
worksheet.write('A16', u'TOPLAM', cell_format_2)
# B Sütunu
worksheet.write('B4', 63379.05, cell_format_3) # Ocak
worksheet.write('B5', 44843.17, cell_format_3) # Şubat
worksheet.write('B6', 82923.77, cell_format_3) # Mart
worksheet.write('B7', 119059.76, cell_format_3) # Nisan
worksheet.write('B8', 45513.57, cell_format_3) # Mayıs
worksheet.write('B9', 50006.03, cell_format_3) # Haziran
worksheet.write('B10', 53824.04, cell_format_3) # Temmuz
worksheet.write('B11', 13878.8, cell_format_3) # Ağustos
worksheet.write('B12', 34737.15, cell_format_3) # Eylül
worksheet.write('B13', 72554.33, cell_format_3) # Ekim
worksheet.write('B14', 66943.89, cell_format_3) # Kasım
worksheet.write('B15', 43338.22, cell_format_3) # Aralık
# Toplama
worksheet.write_formula('B16', '=SUM(B4:B15)', cell_format_3)
# C Sütunu
worksheet.write('C4', defMySql.baglanti(2014,1), cell_format_3) # Ocak
worksheet.write('C5', defMySql.baglanti(2014,2), cell_format_3) # Şubat
worksheet.write('C6', defMySql.baglanti(2014,3), cell_format_3) # Mar
worksheet.write('C7', defMySql.baglanti(2014,4), cell_format_3) # Nisan
worksheet.write('C8', defMySql.baglanti(2014,5), cell_format_3) # Mayıs
worksheet.write('C9', defMySql.baglanti(2014,6), cell_format_3) # Haziran
worksheet.write('C10', defMySql.baglanti(2014,7), cell_format_3) # Temmmuz
worksheet.write('C11', defMySql.baglanti(2014,8), cell_format_3) # Ağustos
worksheet.write('C12', defMySql.baglanti(2014,9), cell_format_3) # Eylül
worksheet.write('C13', defMySql.baglanti(2014,10), cell_format_3) # Ekim
worksheet.write('C14', defMySql.baglanti(2014,11), cell_format_3) # Kasım
worksheet.write('C15', defMySql.baglanti(2014,12), cell_format_3) # Aralık
# Toplama
worksheet.write_formula('C16', '=SUM(C4:C15)', cell_format_3)
# D Sütunu
worksheet.write_formula('D4', '=C4/B4', cell_format_3)
worksheet.write_formula('D5', '=C5/B5', cell_format_3)
worksheet.write_formula('D6', '=C6/B6', cell_format_3)
worksheet.write_formula('D7', '=C7/B7', cell_format_3)
worksheet.write_formula('D8', '=C8/B8', cell_format_3)
worksheet.write_formula('D9', '=C9/B9', cell_format_3)
worksheet.write_formula('D10', '=C10/B10', cell_format_3)
worksheet.write_formula('D11', '=C11/B11', cell_format_3)
worksheet.write_formula('D12', '=C12/B12', cell_format_3)
worksheet.write_formula('D13', '=C13/B13', cell_format_3)
worksheet.write_formula('D14', '=C14/B14', cell_format_3)
worksheet.write_formula('D15', '=C15/B15', cell_format_3)
# Toplama
worksheet.write_formula('D16', '=C16/B16', cell_format_3)

# Insert an image.
worksheet.insert_image('B19', '%slogo.png' %(filenameDirectory))

# Dosyaya yazdık. Şimdi kapatma zamanı. 
workbook.close()

######################################################################
# Execeli Mandrill üzerinden mail atabilmemiz için dosyayı base64’e
# çevirmemiz gerekiyor. http://tr.wikipedia.org/wiki/Base64
######################################################################
base64.encode(open('%s%s' %(filenameDirectory,filenameReport)), open("out.b64", "w"))

# Oluşturduğumuz base64 ü açıp content değerine atıyoruz.
content = open('%sout.b64' %(filenameDirectory)).read()


# Maili gönderiyoruz.
defMandrill.defMandrillUser(content) 
defMandrill.defMandrillRoot(content) 







