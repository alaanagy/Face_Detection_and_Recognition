# Face_Recognition

![image](https://user-images.githubusercontent.com/49722916/95469794-52876180-0980-11eb-9882-c97274930e77.png)


## Introduction 
First of all, to recognize a face, we must detect the face from image then compare it to all images we have at dataset.
The following figure will explain the process briefly
![FaceRecogBlock](https://user-images.githubusercontent.com/49722916/95477210-62a33f00-0988-11eb-879b-e09d945b30eb.png)

## Let's start !

* You should install opencv library before any thing else, search the internet how to install it.

* You will open spider or jupyter notebook or any other python IDE, then you should change the directory to a file that contains 
all files attached here.

* Run 01_dataset_gathering.py file and enter your id number to gather your dataset and save them in dataset folder.

* Run 02_face_training.py to train your model.

* Run 03_face_recognition.py to recognize your image :) 

**Face detection algorithm is Viola-Jones which is one of the most famous algorithm of face detection, high and accurate detection rates,
and easy to understand and implement.**

**Face Recognition algorithm is Local binary patterns histograms (lBPH) but recognition rate is high in a controlled environment (Fixed lighting).**

## Results

![image](https://user-images.githubusercontent.com/49722916/95478947-7a7bc280-098a-11eb-8ca9-b329264f3119.png)

