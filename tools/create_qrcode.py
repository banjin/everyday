
import qrcode


def gener_code():
    """
    创建二维码
    """
    data = "https://www.thepythoncode.com"
    # output file name
    filename = "site.png"
    # generate qr code
    img = qrcode.make(data)
    # save img to a file
    img.save(filename)

# 读取二维码

import cv2
# read the QRCODE image
img = cv2.imread("site.png")
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# #####

def read_qrcode():
    import cv2

    # initalize the cam
    cap = cv2.VideoCapture(0)

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()

        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)

        # check if there is a QRCode in the image
        if bbox is not None:
            # display the image with lines
            for i in range(len(bbox)):
                # draw all lines
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)

            if data:
                print("[+] QR Code detected, data:", data)

        # display the result
        cv2.imshow("img", img)
        
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# #########


def read_qrcode_live():
    import cv2

    # initalize the cam
    cap = cv2.VideoCapture(0)

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()

        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)

        # check if there is a QRCode in the image
        if bbox is not None:
            # display the image with lines
            for i in range(len(bbox)):
                # draw all lines
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)

            if data:
                print("[+] QR Code detected, data:", data)

        # display the result
        cv2.imshow("img", img)
        
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    read_qrcode()
