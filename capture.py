from time import sleep
from picamera import PiCamera
from sys import argv

store_dir = "./low-light/"

def init():
  camera = PiCamera()
  camera.resolution = (1024,768)
  return camera

def take_photo(name, camera):
  camera.start_preview()
  sleep(2)
  camera.capture(store_dir + name)

def close(camera):
  camera.close()
