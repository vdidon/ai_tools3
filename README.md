Info
====
`ai_tool 2018-05-25`

`Author: vdidon <vdidon@live.fr>`

`Copyright: This module has been placed in the public domain.`

`version:0.4.0`
- `support python3`

`version:0.0.6`
`version:0.1.0`
- `add func roc`	
- `add func photo_stiching`
- `add func flv2img`
`version:0.1.1`
- `add func microsoft_demo`
`version:0.1.3`
- `add func luminance`
`version:0.1.4`
- `add func dbop ,opreate the database`
`version:0.1.5`
- `add func util, make the print has time`
`version:0.1.6`
- `add func txt2html, make the txt 2 html table`
`version:0.1.8`
- `modify file microsoft_demo, add zprint into it`
`version:0.1.9`
- `modify roc_yolo`
`version:0.2.1`
- `modify insert_image2db, can insert data into 2 database`
`version:0.2.3`
- `add class2info.py function is get_class_info`
`version:0.2.4`
- `add darkchannel.py to decreate the haze of an image`
`version:0.2.7`
- `add lumi_classfy to luminance.py`
`version:0.3.1`
- `add modify video2img`
`version:0.3.3`
- `add wjdc`
- `add video2gif`
`version:0.3.6`
- `add get_histfeature_from_one_img`


Functions:

- `draw_curve`: draw a curve in a image and return the image 
- `image2text`: translate a image to be text style
- `save2server`: save a image on the local server 
- `image2bw`:  turn a gray image to be a binary weights image

How To Use This Module
======================
.. image:: funny.gif
   :height: 100px
   :width: 100px
   :alt: funny cat picture
   :align: center

1. example code:


.. code:: python

    
    x=np.array([-0.2,0.3,0.4,0.5])
    y=np.array([0.2,0.4,0.1,-0.4])
    norm(x,np.array([0,500]))

    img=draw_curve(x,y)
    img=draw_curve(x,y,title='my title',xlabel='my x label',ylabel='my y lable')
    
    img=cv2.imread('../examples/faces/2007_007763.jpg')
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # img2bw
    img_bw= image2bw(img_gray)


    print img.shape
    image2text(img,(80,40))
    image2text(img,(80,40))



Refresh
========
20180821
