# FULLY CONVOLUTIONAL NETWORKS FOR SEMANTIC SEGMENTATION
[논문 링크](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Long_Fully_Convolutional_Networks_2015_CVPR_paper.pdf) 
Author: Jonathan Long, Evan Shelhamer, Trevor Darrell

* 공부 중이므로 정확하지 않을 수 있습니다.
## Abstract
end-to-end, pixels-to-pixels로 훈련된 convolutional network가 sematic segmentation에서 state-of-the-art를 능가한다는 것을 보여준다.
임의의 크기의 입력을 받아 효율적인 추론 및 학습을 통해 해당 크기의 출력을 생성하는 fully convolutional network를 구축하는 것.

* space of fully convolutional network를 their application to spatially dense prediction tasks and draw connections to prior models.
* skip architecture that combines semantic information from a deep, coarse layer with appearance info from a shallow, fine layer to produce accurate and detailed segmentation

### Segmentation
segmentation은  주어진 이미지 내 각 위치의 픽셀들을 하나씩 조사하면서, 현재 조사 대상인 픽셀이 어느 특정한 클래스에 해당하는 사물의 일부인 경우, 해당 픽셀의 위치에 그 클래스를 나타내는 값을 표기하는 방식으로 결과물을 예측

## Introduction
1) Feature Extraction 
vggnet(네트워크의 깊이가 좋은 성능에 있어 매우 중요한 요소임을 보여준 모델)을 이용한다. 
16개의 conv레이어로 이루어지며 모든 컨볼루션은 3x3, 모든 풀링은 2x2만으로 이뤄져 있다.  
convolution layer - pooling layer - fully convolution layer  
![feature extraction](./img/feature-extraction.jpeg)

2) Feature-level Classification
기존의 fully connected layer를 거치고 나면 class는 분류를 할 수 있으나 위치정보가 사라진다.  
3차원 데이터에는 공간 정보가 담겨있으나 1차원 벡터로 만들어 값을 넘기기에 공간정보가 사라지게 된다. 
![feature-level-classfication](./img/feature-level-classfication.jpeg) 
따라서, 이 문제를 해결하기 위해 fully connected layer 대신 1x1 conv layer를 추가한다.  
이 1x1 conv 의 결과물이 class의 feature map의 segmentation이 된다.  
즉, 위치정보가 사라지는 것이 아니라 남게 되므로 heatmap을 통해서도 확인할 수 있듯 위치에 해당하는 점수가 높게 나오게 된다.
![heatmap](./img/heatmap.jpeg)

## Summary
dense layer는 미리 정해놓은 사이즈의 행렬만큼 곱하기 때문에 사이즈를 미리 정해두어야한다.

Fully convolutional versions of existing networks predict dense output from arbitrary-sized inputs.

* Fully conv networks
input image가 들어오면, convolutino을 반복하다 convolutional feature map이 나옴. 
일반적인 CNN -> 이 feature map을 1줄로 쭉 편 후, dense layer를 집어넣음.
fully convolutional networks -> 10*10*100의 피쳐맵 (총 만개의 숫자)을 1*1*4096로 바꾼다.
(10*10*100짜리를 4096개 사용)  **1*1*해당 디멘션** 짜리 conv layer로 바꾸는 것.
결국 pixel마다 채널에 클래스 정보가 담겨있는 것.

