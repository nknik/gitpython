# Import QRCode from pyqrcode
# pip install pypng
# pip install pyqrcode
import pyqrcode
# import png
# from pyqrcode import QRCode

def generateqr(s=0):

    s='hii nasaaaaaadssdfhjadfhkabdfhbdhfdsbhbdhjb sjh k'

    url = pyqrcode.create(s)

    url.svg("nik.svg", scale = 8)

    url.png('nk.png', scale = 6)
def extractcode(s):
    import cv2
    img=cv2.imread(s)
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    print(val)
    # from qrtools import QR
    import qrtools
    my_QR = QR(filename = s)
  
    # decodes the QR code and returns True if successful
    my_QR.decode()
  
# prints the data
    print (my_QR.data)
# generateqr()    
extractcode('nk.png')