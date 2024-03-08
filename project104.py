import cv2


path='/Users/asmamohammed/Desktop/PYTHON/c104-105/solar-system.jpg'

img= cv2.imread("/Users/asmamohammed/Desktop/PYTHON/c104-105/solar-system.jpg")

#text for sun
cv2.putText(img,'sun',(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

#text for mercury
cv2.putText(img,'mercury',(120,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

#text for venus
cv2.putText(img,'venus',(200,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

#text for earth
cv2.putText(img,'earth',(300,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

#text for mars
cv2.putText(img,'mars',(390,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

#text for jupiter
cv2.putText(img,'jupiter',(600,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

#text for saturn
cv2.putText(img,'saturn',(760,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

#text for uranus
cv2.putText(img,'uranus',(970,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

#text for neptune
cv2.putText(img,'neptune',(1100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255.255,255))

cv2.imshow("preview window",img)

cv2.waitKey(0)