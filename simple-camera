import os
import datetime
from picamera import PiCamera

class RaspyCam:
  
  __tempPath = "/home/pi/dev/temp/bot/"
  
  def __init__(self, resolutionX=1024, resolutionY=768):
    self.camera = PiCamera()
    self.camera.resolution(resolutionX, resolutionY)
  
  def __getCompletePathFilename(self):
    if not os.path.exists(self.__tempPath):
      os.makedirs(self.__tempPath)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    return self.__tempPath + filename
  
  def capture(self):
    filepath = getCompletePathFilename()
    self.camera.capture(filepath)
    return filepath
