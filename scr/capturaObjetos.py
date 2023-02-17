import cv2
import imutils
import os 

# Espeficicar la ruta completa del directorio
Datos = "/img/Imagenes_orejas"
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture(0)

x1, y1 = 400, 300
x2, y2 = 500, 500

count = 0
while True:
    ret, frame = cap.read()
    if ret == False: break 
    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    objeto = imAux[y1:y2, x1:x2]
    objeto = imutils.resize(objeto, width=40)

    k = cv2.waitKey(1)
    if k == 25:
        break

    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count), objeto)
        print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
        count = count + 1

    cv2.imshow('frame', frame)
    cv2.imshow('objeto', objeto)

cap.release()
cv2.destroyAllWindows()
