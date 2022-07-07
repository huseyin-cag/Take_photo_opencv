import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #video yakalaması tanımlandı

img_counter = 0

while True:
    key = cv2.waitKey(1)

    ret, frame = cap.read() #video okuması başladı ve frame(pencere) değişkenine atandı 

    frame = cv2.flip(frame,1) #oluşan video yan olduğu için y(1) ekseninde yansıması alındı

    cv2.imshow("Webcam", frame) #frame deki görüntü okundu
    #Eğer pencere açılmadan fotoğraf çekilmesi isteniyorsa yukarıdaki kod silinebilir
    
    if key == ord("q"): #eğer q ya basılırsa frame kapanacak
        break

    elif key == ord("t"):
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1


cap.release() #video durdu
cv2.destroyAllWindows() #pencere kapandı
