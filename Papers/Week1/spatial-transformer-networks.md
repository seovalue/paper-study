# SPATIAL TRANSFORMER NETWORKS
[논문 링크](http://papers.nips.cc/paper/5854-spatial-transformer-networks.pdf)  
Author: Max Jaderberg, Karen Simonyan, Andrew Zisserman, Koray Kavukcuoglu

* 나름대로 이해한 내용을 작성하였기에 정확하지 않은 내용이 있을 수 있습니다.
## Abstract
이 논문은, CNN의 한계인 the lack of ability to be spatially invariant를 개선하는 모델을 제시한다.   
(공간적으로 불변)  
*Spatial Transformer*라고 불리는 이 모델은, 데이터의 공간 조작을 명시적으로 허용하기에 변환, 크기조정, 회전과 같은 뒤틀림에 대한 불변성을 학습하여 여러 클래스에서 최신 성능을 얻을 수 있음을 보여준다.

## Introduction
이미지에 대해 추론할 수 있는 시스템의 바람직한 특성은 텍스쳐와 모양에 대해서 pose와 part를 분리하는 것.
local max-pooling layer의 도입은 spatially invariant한 것에 대해 개선을 도왔지만, 이는 depth가 깊거나 중간의 feature map에서만 적절하였다.  
why? 공간적 배열의 변화를 처리할 때 이미 정의된 pooling machanism으로 제한적이었기 때문.
이 논문에서 소개될 *Spatial Transformer*는, 개별 데이터 샘플에 따라 spatial transformation이 조절되며 이 작업에 대해 적절한 동작이 훈련 중 학습된다.
각 입력 샘플에 대해 적절한 변환을 생성하여 이미지를 능동적으로, 공간적으로 변환할 수 있는 dynamic mechanism.
이를 통해 spatial transformer를 포함하는 네트워크는 가장 관련이 높은 이미지 영역을 선택할 수 있을 뿐만 아니라 해당 영역을 표준 예상 표즈로 변환하여 후속 계층에서의 추론을 단순화 할 수 있다.
