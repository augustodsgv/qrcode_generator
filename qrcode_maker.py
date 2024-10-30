import qrcode
import sys
import segno

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing file name and / or url paramenters\nUsage: python3 qrcode_maker.py <file_name.png> <url>')
        exit(1)
    
    # url
    data = sys.argv[2]
    # File to save
    file_name = sys.argv[1]

    qrcode = segno.make_qr(data)
    qrcode.save(file_name, scale=20)
