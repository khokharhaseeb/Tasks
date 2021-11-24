# Text Extraction from Id card using Easy OCR in flask
This project contains diferent files
## flas.py for api 
    it has a cam() which will record the video and then save it 
    I have done some special functionality here as i am using web cam but using it on browser and streaming from browser through flask
    her comes the concept of generater as i am using imencode function and yield to use data frame by frame for streaming.

I have used return render_template in it to target the html file in template folder.
its builting  when we will  use it will only target the html file in template folder in the direcotry
and then I am using app(run = debug)

## came.py
In this video we will use two functions
First function will extract the text and at the same iteration image will be passed to other function where face will be detected with harcascade model if face detected thhe i have make a condition in which i am using a list name l just for it igf face detected
then list will be appended other wise it will be empty and till length of list is less than 0 it will continue to detect face if length becomes greater than 0 then it will not enter the function.  

## html 
i have used to html file :
- index.html contains camera and it will be called when we go to browser and recording will be started.
 there will be a button (stop) by which we will stop the recording and extraction will start.

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




## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Authors

- [@muhammadhaseeb](https://www.github.com/octokatherine)



