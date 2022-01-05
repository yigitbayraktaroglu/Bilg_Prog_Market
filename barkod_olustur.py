from barcode import Code128
from barcode.writer import ImageWriter


def barkod_olustur(number):
    number = str(number)
    my_code = Code128(number, writer=ImageWriter())
    my_code.save(filename=number)
