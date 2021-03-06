import cv2
import numpy as np
import sys
# I cropped out each stereo image into its own file.
# You'll have to download the images to run this for yourself

iframeDir=sys.argv[1]  #../keyframe/
videoName=sys.argv[2]  #video in video.all
numFrame=int(sys.argv[3])  #25
outputDir=sys.argv[4]      #../sift/

for frameId in range(1,numFrame+1):
   jpgFilePath=iframeDir+iframeDir.split("/")[1]+"_"+videoName+'%09d'%frameId+".jpg"

   img = cv2.imread(jpgFilePath)
   if not img is None:
       #print img.shape
       gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
       sift = cv2.xfeatures2d.SIFT_create()
       kp, desc = sift.detectAndCompute(gray, None)
       #print desc.shape
       if not desc is None:
           with open(outputDir+videoName,"a") as f_handle:
               np.savetxt(f_handle,desc,delimiter=';')
