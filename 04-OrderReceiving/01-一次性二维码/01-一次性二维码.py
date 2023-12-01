# import barcode
# from barcode.writer import ImageWriter
# EAN = barcode.get_barcode_class('ean13')
# my_ean = EAN('5901234123457', writer=ImageWriter)
# fullname = my_ean.save('ean13_barcode.png')

# from io import BytesIO
# fp = BytesIO()
# my_ean.write(fp)
#
#
# with open("EAN.txt", "wb") as f:
#    my_ean.write(f)  # Pillow (ImageWriter) produces RAW format here
#
# from barcode import generate
# name = generate('EAN13', '5901234123457', output='barcode_svg')

#
# fp = BytesIO()
# generate('EAN13', '5901234123457', writer=ImageWriter, output=fp)

# import barcode
# from barcode.writer import ImageWriter
#
#
# bar=barcode.get('ean13','123456789102',writer=ImageWriter)
# filename=bar.save('ean13')
# print(filename)
import barcode
from barcode.writer import ImageWriter
EAN = barcode.get_barcode_class('ean13')
my_ean = EAN('5901234123457', writer=ImageWriter)
fullname = my_ean.save('ean13_barcode')
