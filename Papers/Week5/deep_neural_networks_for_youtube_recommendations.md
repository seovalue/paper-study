# Deep neural networks for youtube recommendations

## System overview
![](./img/system%20overview.png)  
이전 논문인 [The youtube video recommendation system](https://github.com/seovalue/paper-study/blob/master/Papers/Week3/The_YouTube_Video_Recommendation_System.md) 과 동일하게 기본 구조는 candidate generation-> ranking의 2단계 구조를 따른다.  
* candidate generation: 유저의 활동 정보를 협업 필터링으로 분석해 유튜브 영상 중 해당 유저가 좋아할 것 같은 영상들만 high-precision으로 대략적으로 선별해내는 작업  
* ranking: candidate generation 단계에서 선별한 비디오들과 유저의 정보를 더 자세히 보면서 유저의 선호도 점수를 추정하고 선호도 순으로 추천  

### Candidate generation
ranking에 쓰일 후보 비디오 숫자를 수백개의 수준으로 **좁혀서** scalability를 확보합니다.  
특히, 특정 시점에 유저가 시청할 것 같은 하나의 영상을 맞추는 *extreme multiclass classification* 문제로 정의하여 진행합니다.
  
식은 다음과 같습니다.
$$
P(w_t=i|U,C)=\frac{e^{v_i^T u}}{\sum_{j\in V}{e^{v_j^T u}}}
$$  
여기서 $u$는 유저 정보 $U$와 컨텍스트 정보 $C$를 조합하여 만든 유저 임베딩이고, $i$는 비디오 id를, $v_i,v_j$는 비디오 임베딩을 나타냅니다.
여기서의 `embedding`은 단순히 개별 비디오, 사용자와 같은 것들을 $R^n$의 dense vector로의 매핑입니다.  

이 때 deep neural network의 과제는, softmax를 이용하여 동영상을 구분하는데 유용한 사용자의 이력 및 컨텍스트 함수로 사용자 임베딩 $u$를 임베딩하는 것입니다.  

즉 $w_t=i$는 비디오 $i$가 시간 $t$에 시청되었다는 것을 나타내는데, 유저가 비디오를 전부 시청했으면 유저가 positive implicit feedback을 준 것으로 간주합니다.  
즉, 유저 정보와 컨텍스트 정보를 input으로 유저의 watch 여부를 label로 하여 $P(w_t=i|U,C)$가 최대값이 되는 $i$를 알아내는 multi-class classification 문제가 되는 것입니다.  


**Model Training**  
이렇게 **Classification**의 문제로 정의했을 때의 장점은 nagative sampling 테크닉을 활용하여 모델 학습 시에 사용해 학습 속도를 획기적으로 개선할 수 있다는 점입니다.   
수천개의 negative class를 뽑은 뒤, *Large-Scale NMT*(https://www.aclweb.org/anthology/P15-1001/)에서 사용했던 접근법을 모방해 importance weighting으로 보정한다고 되어있습니다. (negative class를 충분히 많이 뽑으면 보정은 안해도 크게 상관이 없다고 합니다.) 

**Model Serving**  
서비스할 때, 유튜브의 비디오 중 top K개만 수십 ms안에 뽑아내야하는 시간 제약으로 인해 정확도보다는 적당한 솔루션을 빨리 뽑아내는 방법을 사용합니다.  
Multiclass classification에서 top K개의 클래스를 뽑아내는 문제는 output vector에서 k-최근접 이웃 알고리즘과 동일한 문제입니다.  
따라서 적당한 output space에 approximate k-nearest neighbor search(http://www.cs.cmu.edu/~agray/approxnn.pdf) 알고리즘을 돌리면 됩니다.
  
**Model Architecture**
![](./img/model%20architecture.png)  
모델의 구조는 위와 같습니다.  
각 유저들은 시청했던 비디오 목록, 검색 키워드, Demographic feature(나이, 성별, 위치, 사용 기기, 로그인 상태) 를 통해서 `fixed-length vector`로 임베딩됩니다.  
시청했던 비디오들은 각 비디오들의 embedding을 평균하여 watch vector가 되고, search token들도 각 ngram 단위로 임베딩된 후 search vector라는 fixed-length vector로 합쳐집니다.  

이 때 search token의 순서를 무시하게 됩니다.  
그 이유는, 유저가 다음에 볼 비디오를 예측할 때 예를 들어 아이들의 덤디덤디 무대를 검색한 뒤 덤디덤디 무대를 시청하였다면 모델은 단순히 마지막 검색어와 대응되는 검색 결과를 외우는 것이 가장 합리적인 방법이 됩니다.  
하지만 매번 새로운 동영상을 사용자에게 추천하기 위해 키워드의 맥락에 따라 추천 리스트가 달라지도록 구현하기 위해 search token들의 순서를 뭉개고 각각 averaging하여 embedding합니다.  

또한 과거의 데이터 위주로 모델이 편향 학습되는 경향을 보정하기 위해, example age라는 feature을 추가해 각 training example이 학습 시점으로부터 얼마나 오래되었는지를 모델에 명시합니다.
이렇게 example age를 넣어 모델을 만들면, 아래와 같이 유저들이 시간이 지남에 따라 특정 비디오를 점점 덜 보게 되는 경향을 보다 잘 예측할 수 있었다고 합니다.

**(Label, input) 생성**