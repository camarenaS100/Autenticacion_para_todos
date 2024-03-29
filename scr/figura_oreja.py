import os
import cv2

# Obtiene la ruta de de la carpeta con la imagen para cambiar las escalas de colores
ruta = os.path.join('img', 'Mi_oreja.jpg')
	
image = cv2.imread(ruta)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
_,umbral = cv2.threshold(gray,100,255,cv2.THRESH_BINARY) # Modificar la escala de grieses de la imagen
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contorno,-1,(251,63,52),3) # Reconocimiento de contornos


cv2.imshow('imagen con contornos', image)
cv2.imshow('imagen a escala de grises', canny)
cv2.imshow('imagen en blanco y negro',umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()