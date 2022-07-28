import cv2
import numpy as np

ressim = cv2.imread("ist.jpg")

#resmin kendim belirlediğim belli bir kısma, [:,:,1] --> 1 olan yer RGB'nin G (yeşil) kısmıyla oynuyoruz.
#Her bir renk (RGB'den biri) 0 ile 255 değerde veya aralıktan bir sayıdadır.
ressim[180:230,380:560,1]=0



cv2.imshow("ali", ressim)











#pencere ciktiğinda biz ekrana müdahale edene kadar pencere ekranda sabir kalması sağlanır.
cv2.waitKey(0)
#pencereyi açıp kapattığımız zaman arkada çalışan opencvyi de sonlandırır.
cv2.destroyAllWindows()