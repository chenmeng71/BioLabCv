# BioLabCv
Explore the use of Computer Vision in Biology lab work.

Starting from a picture taken in bio lab, and let's see if we can use computer vision to help counting the number of e-coli colonies.
<div align="left">
    <img src="/labImage.JPG" width="400px"</img> 
</div>
<br/>

Crop a smaller segment to simplify.
<div align="left">
    <img src="/ecoliCrop.JPG" width="300px"</img> 
</div>
<br/>

Screenshot from running colonyCount.py, where 372 colonies are counted from the cropped image. First display image shows the result of the processing where the contour of each colony is found and the total number of contours is counted. The second and third display images show the intermediate steps of finding the colonies in the input image, and the distance transformation where each pixel is replaced with the value of its distance to the nearest background pixel.
<div align="left">
    <img src="/ScreenshotColonyCount.png" width="1000px"</img> 
</div>
<br/>

These python packages are needed to run the program. Use "pip" to install.
* opencv-python
* matplotlib
* numpy
* imutils

