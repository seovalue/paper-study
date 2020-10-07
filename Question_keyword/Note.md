# Feedback Datasets

# Explicit Datasets
현재 프로젝트 목표인 영화 추천 시스템에 대해 생각해보자.

영화 추천 시스템을 만들기 위해서는 어떤 데이터를 사용할 수 있을까?  
먼저, 사용자의 평점 기록 데이터가 있다. 예를 들자면 `Movielens Data`와 같이 `userid, movieid, rating, timestamp` 형태의 데이터가 포함된 파일이 있다.  
유저가 해당 영화에 대해 평점을 매긴 데이터를 바탕으로 영화를 추천할 수 있다.  
이렇게, 평점 기록과 같이 유저가 **자신의 선호도를 직접 표현한 데이터를 Explicit Data**라고 한다. 
영화 리뷰, 차단과 같은 데이터 또한 Explicit Data이다.  
  
Explicit data를 활용하면 강력한 정보를 얻을 수 있다. 유저의 판단에 대한 호불호를 명백히 알 수 있기 때문이다.  
하지만 이러한 데이터를 얻는 것은 힘들다. 현재 얻고 있는 네이버 영화 데이터에서도 마찬가지로 영화를 보고 매기는 유저의 수는 전체 유저에 비해 적고, 또한 다양한 리뷰를 남기지 않는다.  
몇 명의 유저에 대한 리뷰를 확인해본 결과 본인이 **굉장히 흥미있거나** 혹은 **굉장히 극혐이었거나..** 하는 영화들에 대해서만 의견을 남겨 보통 한 유저당 많으면 5개의 리뷰, 적으면 1개정도의 리뷰가 존재한다.  
어쩌면 귀찮음으로 인해 적극적인 Action(리뷰)을 취하지 않는 것일 수도.  
(나 또한 영화 리뷰를 남겨본 적이 한번도 없다. )  

# Implicit Datasets
[Collaborative Filtering For Implicit Feedback Datasets](https://ieeexplore.ieee.org/document/4781121) 논문에 따르면 2010년 이전까지 추천 시스템 분야에서는 주로 Explicit Data를 다루었다.
논문에서는 Implicit 이라는 다른 종류의 데이터를 활용하여 추천시스템을 만드는 방법을 제시하고 있다.  

Implicit Data는 **유저가 간접적으로 선호하는 것과 취향을 나타내는 데이터**를 의미한다. 예를 들자면 검색 기록, 방문 페이지, 마우스 움직임 기록 등이 있다.
이러한 데이터는 유저가 개인정보제공에 동의만 한다면 자동적으로 얻을 수 있기에 수집 난이도가 낮다.
  

### Implicit Dataset의 특징
1. No Negative Feedback   
유저 행동 기반의 관측치는 아이템에 대한 선호를 암시할 수 있지만, 비선호를 나타내는 것은 어렵다. 예를 들자면, 유저가 어떤 영화를 본 기록이 없을 때 그 영화를 싫어해서 보지 않았는지, 혹은 몰랐기 때문에 보지 못했는지에 대해 알 수 없다.
이러한 특징으로 인해 Implicit Data를 모델링할 때에는 수집되지 않은 데이터도 같이 모델링해야한다. 수집되지 않은 데이터에 불호 정보, 부정적인 정보가 담겨있을 가능성이 존재하기 때문이다.  

2. Inherently Noisy  
유저 행동을 추적할 때 정확한 동기와 선호도를 추측하는 것이 어렵다. 이는 위와 반대로 어떤 영화를 봤다고 해서, 유저가 그 영화를 좋아한다고 말하기가 어렵다. 과제로 인해 본 것일 수도 있고, 영화는 맘에 1도 안들지만 나가기엔 돈아까워 끝까지 본 것일 수도 있다.
유튜브의 경우에는 시청시간을 중요한 데이터로 삼는데, 유저가 영상을 틀어놓고 노잼으로 인해 잠들었을 수도 있다.  

3. The numerical value of Implicit feedback indicates confidence  
반복된 행동은 유저의 선호를 반영할 수 있지만, 한 번의 이벤트는 다양한 이유로 발생하기에 implicit feedback의 수치는 preference가 아닌 confidence를 나타낸다. Explicit data의 높은 수치는 곧 높은 선호도를 의미한다. 
하지만 Implicit은 그렇지 않다. 선호도라고 하기 보다는, 한번 보고만 영상보다는 자주, 그리고 오래 본 영상이 유저가 자신의 선호도나 의견을 표현했다는 것에 대한 신뢰도로 해석할 수 있다.  

4. Evaluation of implicit-feedback recommender requires appropriate measures  
평가 척도에 대한 고민이 필요하다. implicit model의 경우 item의 availability나 반복되는 feeback 등을 고려해야 한다. availability란 동시간에 방영되는 두 TV Show의 경우 한쪽만 볼 수 있어서 다른 프로그램을 좋아한다고 해도 Implicit Data가 쌓이지 않는 상황을 말한다. 반복되는 Feedback은 유저가 한 번 이상 프로그램을 봤을 때 한 번 본 경우와 어떻게 다르게 평가할 것인가에 대한 고려이다.  

# Model
implicit feedback에 적용할 수 있는 Latent factor Model이다.  
먼저, 유저 u가 아이템 i에 대한 선호도를 나타내는 binary variable P_ui를 정의한다.  
![](./img/formula1.PNG)  
즉, 유저 u가 아이템 i에 대해 행동을 했으면 1, 아니면 0이다. Implicit Feedback의 경우에 결측치는 선호도에 대해 모르기에 대부분 무시하고 알고리즘이 구현된다.
하지만 preference(P_ui)만으로는 행동을 한 관측치에 대한 설명이 부족하기에 confidence(C_ui, 신뢰도)가 필요하다. 
예를 들어, 아이템에 대한 존재를 몰라 어떠한 행통을 못했을 수도 있고, 선호하진 않지만 다른 이유로 제품을 구매했을 수도 있다.
그 중에서도 반복적인 행동은 (어쩌면) 확실히 선호한다는 것에 대한 증거가 될 수 있다.
그렇기 때문에 r_ui(유저 u의 아이템 i 선호도, P_ui와 개념 같음.)가 커질수록 강한 선호의 지표로 증가함수인 confidence에 대해 정의할 수 있다.  
![](./img/formula2.PNG)  
a(알파)에 따라 r_ui에 대한 변동을 통제한다. confidence는 고정된 수치로 계산하기에 최적화할 파라미터는 아니다. preference와 confidence를 반영해 최적의 USER-ITEM LATENT FACTOR를 찾기 위해, 손실 함수를 다음과 같이 정의한다.  
![](./img/formula3.PNG)  
이는 SGD(경사하강)나 ALT(제곱법)를 통해 최적화할 수 있다. 




