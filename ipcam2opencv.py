import base64
import time
import urllib2

import cv2
import numpy as np
import getch

"""
Examples of objects for image frame aquisition from both IP and
physically connected cameras

Requires:
 - opencv (cv2 bindings)
 - numpy
"""


class ipCamera(object):

    def __init__(self, url, user=None, password=None):
        self.url = url
        auth_encoded = base64.encodestring('%s:%s' % (user, password))[:-1]

        self.req = urllib2.Request(self.url)
        self.req.add_header('Authorization', 'Basic %s' % auth_encoded)

    def get_frame(self):
        response = urllib2.urlopen(self.req)
        img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
        frame = cv2.imdecode(img_array, 1)
        return frame


class Camera(object):

    def __init__(self, camera=0):
        self.cam = cv2.VideoCapture(camera)
        if not self.cam:
            raise Exception("Camera not accessible")

        self.shape = self.get_frame().shape

    def get_frame(self):
        _, frame = self.cam.read()
        return frame


while (True):
    print "\nPress s for a new snapshot\n" \
          "Press i to move up the Foscam\n" \
          "Press k to move down the Foscam\n" \
          "Press l to move left the Foscam\n" \
          "Press j to move right the Foscam\n"
    char = getch.getche()

    if char=='s':
        url = "http://192.168.10.222:1201/snapshot.cgi?user=admin&pwd="
        print '\n'+url
        """
        cam = ipCamera(url)
        frame = cam.get_frame()
        cv2.imshow('image',frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        """
    elif char == 'i':
        url = "http://192.168.10.222:1201/decoder_control.cgi?command=1&user=admin&pwd="
        print '\n'+url
        req = urllib2.Request(url)
        print req
    elif char == 'k':
        url = "http://192.168.10.222:1201/decoder_control.cgi?command=3&user=admin&pwd="
        print '\n'+url
        req = urllib2.Request(url)
        print req
    elif char == 'l':
        url = "http://192.168.10.222:1201/decoder_control.cgi?command=5&user=admin&pwd="
        print '\n'+url
        req = urllib2.Request(url)
        print req
    elif char == 'j':
        url = "http://192.168.10.222:1201/decoder_control.cgi?command=7&user=admin&pwd="
        print '\n'+url
        req = urllib2.Request(url)
        print req
    else:
        print "Bad Usage, try again..\n"


"""
Here a list of more feature from decoder_control.cgi with the Firmware 11.14.2.28 (found
http://www.gadgetvictims.com/2010/10/fi8908w-old-and-new.html) --Lowbayer 21:39, 12 March 2011 (UTC)
Example: http://192.168.10.222:1201/decoder_control.cgi?command=30&user=admin&pwd= = Set the preset 0
Parameters value
0 up
1 Stop up
2 down
3 Stop down
4 left
5 Stop left
6 right
7 Stop right
... Reserved
25 center
26 Vertical patrol
27 Stop vertical patrol
28 Horizon patrol
29 Stop horizon patrol
30 Set preset 0
31 Go preset 0
32 Set preset 1
33 Go preset 1
34 Set preset 2
35 Go preset 2
....
62 Set preset 16
63 Go preset 16
And the list goes further until preset 16
94 IO output high
95 IO output low
"""