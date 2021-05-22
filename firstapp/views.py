from django.shortcuts import render
# Create your views here.

from django.core.files.storage import FileSystemStorage
import imageio
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import json
from tensorflow import Graph
from tensorflow.compat.v1 import Session
import numpy as np
import cv2
import base64
from io import BytesIO

img_height , img_width = 400,600

#model = load_model('models/model_rec.h5')
model_graph = Graph()
with model_graph.as_default():
    tf_session = Session()
    with tf_session.as_default():
        model = load_model('models/model_rec.h5')

def Enhance(img, index, flag):
    if index == 0:
      return img

    elif flag == 1:
        h, w, c = img.shape
        with model_graph.as_default():
            with tf_session.as_default():
                test = model.predict(img.reshape(1, h, w, 3))  
        temp = img / 255
        image = temp + ((test[0,:,:,:] * temp)*(1-temp))
        index = index - 1
        flag = 0
        return Enhance(image, index, flag)

    else:
        h, w, c = img.shape
        with model_graph.as_default():
            with tf_session.as_default():
                temp = model.predict(img.reshape(1, h, w, 3))
        image = img + ((temp[0,:,:,:] * img)*(1-img))
        index = index - 1
        return Enhance(image, index, flag)

# def ndarray_to_b64(ndarray):
#     """
#     converts a np ndarray to a b64 string readable by html-img tags 
#     """
#     img = cv2.cvtColor(ndarray, cv2.COLOR_RGB2BGR)
#     _, buffer = cv2.imencode('.png', img)
#     return base64.b64encode(buffer).decode('utf-8')

def to_data_uri(img):
    data = BytesIO()
    img.save(data, "JPEG") # pick your format
    data64 = base64.b64encode(data.getvalue())
    return u'data:img/jpeg;base64,'+data64.decode('utf-8') 


def index(request):
    context = {'a':1}
    return render(request,'index.html',context)


def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileObj = request.FILES['filepath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    #print(filePathName)
    testimage = '.' + filePathName
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)

    index = 8
    # mean = np.mean(x)               #get mean of image to know the degree of darkness
        
    # if (mean < 10):  #specify the number of iterations suitable for the input image
    #     index =7  #12 if extreme low light
    # else:
    #     index = 7   #8 if medium low light
    out = Enhance(x, index, 1)         #apply model to input image
             
    output = (out * 255).astype("uint8")   #convert range of output from [0:1] to [0:255]
    height, width, channel = output.shape
    output_img = Image.fromarray(output, 'RGB')
    # print(output_img)
    # output_img.show()

    output_img = to_data_uri(output_img)
    #output_id = output_img.objects.values_list('id')
    # fileObj_ = request.FILES['filepath']
    # fs_ = FileSystemStorage()
    # filePathName_ = fs_.save(fileObj_.name, fileObj_)
    # filePathName_ = fs_.url(filePathName_)
    #print("output id : ", output_id)
    #output_img.save('my.png')
    #output_img = output.load_img(output, target_size=(height, width))
    context = {'filePathName':filePathName,'output_img': output_img}
    return render(request, 'index.html', context)