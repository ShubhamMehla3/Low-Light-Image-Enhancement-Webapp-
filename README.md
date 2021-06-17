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

## Performance on Real Lowlight Images

To obtain better enhancement result, we linearly amplify the output of the network to improve contrast. Please read the code to see other parameter settings. 

![me](https://user-images.githubusercontent.com/65397085/122344040-fc81a980-cf63-11eb-9a7f-d50068d5e2f8.jpg)




