# VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION
[논문 링크](https://arxiv.org/abs/1409.1556)  
Author - Karen Simonyan & Andrew Zisserman

* 나름대로 이해한 내용을 작성하였기에 정확하지 않은 내용이 있을 수 있습니다.
## Abstract
They investigate the effect of the convolutional network depth on ints accuracy in the large-scale image recognition setting.
매우 작은 3x3의 필터를 이용하여 depth를 더 깊게 표현함.  
이 방법은 depth에 16-19의 weight을 준 layer를 넣으면서 더욱 significant한 성취를 보였다.

## Introduction
1. 더 나은 정확성을 위한 이전의 시도
- smaller receptive window size and smaller stride of the first convolutional layer.
2. 현재의 시도
- **depth**에 중점을 두었다.
- 매개변수를 수정하고, 모든 레이어에 3x3 filter를 적용하여 더 많은 convolutional layer를 생성하고, increasing depth.
(filter의 개수가 작을수록 슬라이스가 더 많아져서 차원(depth)이 더 깊어진다?)