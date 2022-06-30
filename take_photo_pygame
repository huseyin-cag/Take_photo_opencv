import pygame
import pygame.camera
import time

pygame.camera.init() #kamera modülü başladı
pygame.camera.list_cameras() #Kullanılabilecek kameralar listelendi
cam = pygame.camera.Camera("Chicony USB2.0 Camera",(640,480)) #Kullanılacak kamera ve boyutu ayarlandı
cam.start() #kamera başladı
time.sleep(0.5)

img = cam.get_image() #fotoğraf çekildi

time.sleep(0.5)
pygame.image.save(img,"filename.jpg") #fotoğraf indirildi
