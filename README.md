# Hidden-Eye
**Hide data into Picture**

Hidden-Eye is library which contain different kinds of Steganography's algorithm in it.

For now , It contains 2 algorithms for hidding data into PNG format.

One is for ASCII and other is for hidding pdf.  

## Hiding ASCII 

For checking , You can use TestEnStrpng.py

![Real_Red_Image](https://github.com/immortal3/Hidden-Eye/blob/master/Tests/Red.png)

![Encode_Image](https://github.com/immortal3/Hidden-Eye/blob/master/ReadMe_Resources/Red_Encoded.png)

Second Image contains 25000 hidden chars in it.
Can you see difference in it ??

## Hiding PDF

For checknig , You can use Hidingpdf.py

Real Photo
![Real_photo](https://github.com/immortal3/Hidden-Eye/blob/master/Tests/big_photo.png)


hidden pdf into this photo
![Encoded_pdf_image](https://github.com/immortal3/Hidden-Eye/blob/master/ReadMe_Resources/encoded_pdf.png)



### Issuses 

Opencv is writting bigger image and reducing one channel when saving encoded png.

In pdf , there is error in retrieving font.
IF someone kwons how to fix it email me or send push request.
