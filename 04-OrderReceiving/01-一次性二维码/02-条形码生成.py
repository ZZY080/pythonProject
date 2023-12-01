# import  barcode
#
# hr=barcode.get_barcode_class('ean13')
# Hr=hr('123234567890-=')
# qr=Hr.save('123')
# from barcode.writer import  ImageWriter
# hr=barcode.get_barcode_class('code39')
# Hr=hr('123456789876543',writer=ImageWriter())
# qr=Hr.save('1123.png')
import  barcode

bar=barcode.get("ean13",'123456789123450')
bar.save('1.png')