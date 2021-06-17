# Low-Light-Image-Enhancement-Webapp-
Images captured in outdoor scenes can be highly degraded due to poor lighting conditions. These images can have low dynamic ranges with high noise levels that affect the overall performance of computer vision algorithms. To make computer vision algorithms robust in low-light conditions, use low-light image enhancement to improve the visibility of an image.

- We present a deep learning based method for low-light image enhancement. This
problem is challenging due to the difficulty in handling various factors simultaneously
including brightness, contrast, artifacts and noise.

- To address this task, we propose the
multi-branch low-light enhancement network (MBLLEN). The key idea is to extract rich
features up to different levels, so that we can apply enhancement via multiple subnets
and finally produce the output image via multi-branch fusion. 

- To address this task, we propose the
multi-branch low-light enhancement network (MBLLEN). The key idea is to extract rich
features up to different levels, so that we can apply enhancement via multiple subnets
and finally produce the output image via multi-branch fusion.

![NN-MBLLEN](https://user-images.githubusercontent.com/65397085/122346292-6a2ed500-cf66-11eb-9297-607ecd6ce496.jpg)


## Dataset
We have used LOL Dataset and the Dataset Provided by MBLLEN 

- LOL Dataset : https://drive.google.com/file/d/157bjO1_cFuSd0HWDUuAmcHRJDVyWpOxB/view 
- MBLLEN Dataset : https://drive.google.com/file/d/1U1hyvVktYEoK_3cdcbWNaJ1WDft2mLRl/view 

## Requirements ##

- [x] python 3  
- [x] Tensorflow 1.6.0
- [x] Django  
- [x] Keras 2.2.0
- [x] HTML/CSS
- [x] Opencv-python 3.4.2

## Model 

the proposed MBLLEN consists of three types of modules: the feature
extraction module (FEM), the enhancement module (EM) and the fusion module (FM).

- **FEM** It is a single stream network with 10 convolutional layers, each of which uses
kernels of size 3 × 3, stride of 1 and ReLU nonlinearity, and there is no pooling operation.
The input to the first layer is the low-light color image. The output of each layer is both the
input to the next layer and also the input to the corresponding subnet of EM.

- **EM** It contains multiple sub-nets, whose number equals to the number of layers in FEM.
The input to a sub-net is the output of a certain layer in FEM, and the output is a color image
with the same size of the original low-light image. Each sub-net has a symmetric structure to
first apply convolutions and then deconvolutions. The first convolutional layer uses 8 kernels
of size 3×3, stride 1 and ReLU nonlinearity. Then, there are three convolutional layers and
three deconvolutional layers, using kernel size 5 × 5, stride 1 and ReLU nonlinearity, with
kernel numbers of 16, 16, 16, 16, 8 and 3 respectively. Note that all the sub-nets are trained
simultaneously but individually without sharing any learnt parameters.

- **FM** It accepts the outputs of all EM sub-nets to produce the finally enhanced image.
We concatenate all the outputs from EM in the color channel dimension and use a 1 × 1
convolution kernel to merge them. This equals to the weighted sum with learnable weights.

## Performance on Real Lowlight Images

To obtain better enhancement result, we linearly amplify the output of the network to improve contrast. Please read the code to see other parameter settings. 

![ShubhamMehla](https://user-images.githubusercontent.com/65397085/122344998-fb9d4780-cf64-11eb-8a4e-1e8191be5e47.jpg)


## Performance on MBLLEN Dataset

![mbllen-synthetic-dataset-result](https://user-images.githubusercontent.com/65397085/122345582-a31a7a00-cf65-11eb-9a85-db4bd9c13b8f.jpg)



