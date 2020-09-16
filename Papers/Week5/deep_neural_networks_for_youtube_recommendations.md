# Deep neural networks for youtube recommendations

## System overview
![](./img/system%20overview.png)  
이전 논문인 [The youtube video recommendation system](https://github.com/seovalue/paper-study/blob/master/Papers/Week3/The_YouTube_Video_Recommendation_System.md) 과 동일하게 기본 구조는 candidate generation-> ranking의 2단계 구조를 따른다.  
* candidate generation: 유저의 활동 정보를 협업 필터링으로 분석해 유튜브 영상 중 해당 유저가 좋아할 것 같은 영상들만 high-precision으로 대략적으로 선별해내는 작업  
* ranking: candidate generation 단계에서 선별한 비디오들과 유저의 정보를 더 자세히 보면서 유저의 선호도 점수를 추정하고 선호도 순으로 추천  

 