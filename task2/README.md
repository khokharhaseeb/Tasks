# Image processing using Numpy, Open-cv, PILLOW
In this task i have to explore Numpy , Open-cv and Pillow
for image processing, Flipping,Rotation.

# Image Processing 

In this directory i have managed different types of method to do image Processing . 
I have used Open_Cv and Pill and done same task and differnt tasks but 
for most of the image processing in my projects i used open-cv for image processing.
Acording to me the benefit is that cv2 just extract the pixel insted of orientation so its easy for me to
concatenate and to other functions though 
pill also contains functions through which we can handle this like exif class

#starting with
I have done it in jupyter Notebook you just have to open it there and and install requirement file using command pip install -r requirements.txt in your shell.

#numpy functions and flipping
In this directory numpy functions and flipping with Image there are two files.
In numpy.ipynb i have covered different numpy functions from basic to advance.
In numpy-flipping.ipynb file i have done diffenent flippings using numpy both manually and by using numpy funcitons.
 
#screenshots in folder
# Opencv projects  and preprocessing
 In this directory you can find all the task regarding Image processing using Open-cv.

 - Face detection
 - Chanell shifting
 - Bolean image, masking
 - Draw rectangle, Circle, line on image
 - Like chanel shifting(BGR to RGB)
 - Fliping
 - Rotation
 - Color change
 - Resizing
 - Croping

##Working
 This Directory have multiple files each file is a project.
 Name of file is the name of project which makes easy to understand and work.
- In file Bitwise operations i have done three operations including or , and , xor
  which are used as union, intersection and XOR(return True for different inputs and false for same inputs)
- Scond file is aout waitkey we use in open-cv image and video apturing basically to delay processing
- Now three file face detection, face detection with web cam and face detection from video all are using harcascade model given with name h.xml
  All of these have approx. same work.
  first we have to make the Images gray by cv2.cvtCOLOR() and then we will make instance of the model and and then detect the faces.
  like -> face_c = cv2.CascadeClassifier('h.xml') 
    
    It will return us two things first is box having starting position(two points ),height and width of face in it and second is det which will have accuracy of the face.
    we will make copy of the image and using the comming points to crop the image using points.
Now same logic will take place in other files wich are using the model only the difference is that we are using web cam by giving 0 instead of video.
common error is that we forget to write waitkey which gives us error same in releasing video.
- Now for same face detection we use different model is dnn which works on image without converting it to gray scale.
- In first we will extract the blob and pass it as input for detection in dnn function and the face will be detected
-Translation Rotation and other folders by name descibing simple functions are given in them

#PILL 
In pill i we will use mostly the same functions as we used in cv2 
but as there is also a chanel difference between them
We transform, rotate and flip images both in cv2 and pill

 ```bash  
git clone https://github.com/khokharhaseeb/Tasks.git
cd flask_ocr/Opencv
```
 
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Authors

- [@muhammadhaseeb](https://github.com/khokharhaseeb/Tasks.git)



