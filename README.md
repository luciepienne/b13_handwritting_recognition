# HANDWRITTING RECOGNITION


***

## Table of Contents
1. [Overview](#overview)
2. [How to Run](#how-to-run)
    1. [Create the model](#create-the-model)
    2. [Test the model](#test-the-model)
3. [Different interesting points](#different-interesting-points)
4. [Usage](#usage)

***
## Project structure
```
project/
│
├── functions/    # Python scripts for each function used in notebook
│
├── data/
│   ├── drawing/    # tests draws to make some recognition
│   └── webcams/    # tests pictures to make some recognition
├── functions/
│
├── models/
|
├── notebooks/
├── website/
│
├── .gitignore
└── README.md

```

## Overview
La Poste can use AI to better read handwritting, let's help them to improve their performance.

The MNIST dataset is a collection of handwritten digits. It consists of 70,000 images, each of size 28x28 pixels. The dataset is directly compatible with the original MNIST dataset.


## How to Run
- run with Jupiter Notebook
- Ensure you have pip install :
numpy 
pandas
keras.models 
keras.layers
keras.optimizers
keras.preprocessing.image
tensorflow.keras.models
matplotlib
cv2
os
sys

### Create the model

After testing VGG16 it appears that the most performing model is CNN

1. MNIST NUMBER DATASET
Run the file : notebooks/number_recognition_model.ipynb
=> you will download MNIST number dataset and generate a model in models repository named 'number_recon_model.keras'

2. MNIST FASHION DATASET
Run the file : notebooks/fashion_recognition_model.ipynb
=> you will download MNIST fashion dataset and generate a model in models repository named 'fashion_recon_model.keras'

### Test the model 

You will test the model prediction and see if it can recognize your numbers.
The real difficulty is to make sure the image is well configured before the prediction to be able to realize the 97% of accuracy. 
The time has run out to make the relevant changes to predict with a good accuracy.

1. webcam and drawing Test
You can launch in your browser the website and create many pictures of numbers drawing or taking a picture of numbers.

2. Dataset test
Test your predictions : notebooks/number_recognition_predict.ijynb
=> you will try the prediction of your model with some pictures downloaded previously

## Different interesting points
- The part to predict fashion is not ready

## Usage

internal usage only. for training only


