이번에는 Linear Regression에 대해서 배운다.

- 선형으로 예측되는 모델을 구현하기 위한 알고리즘이란다.
- 예를 들어 Ch5 에서 봤던 그 그래프들은 모두 y=3x+4에서 기반으로 시작한거다.
- 위와 같은 자료에서 같은 a와 b값을 찾아내는 임무를 수행하는 거란다.

## linreg1.py

```
0 session is performed. cost is  547.8427 , a is  1.2365 , b is  0.557
100 session is performed. cost is  2.4509695 , a is  3.2354178 , b is  0.86772746
200 session is performed. cost is  2.2190819 , a is  3.224005 , b is  1.0195805
300 session is performed. cost is  2.009134 , a is  3.213145 , b is  1.1640717
400 session is performed. cost is  1.8190519 , a is  3.2028117 , b is  1.3015579
(중략)
4500 session is performed. cost is  0.030911379 , a is  3.0264382 , b is  3.6482372
4600 session is performed. cost is  0.02798688 , a is  3.0251565 , b is  3.6652906
4700 session is performed. cost is  0.025339136 , a is  3.023937 , b is  3.6815174
4800 session is performed. cost is  0.022941766 , a is  3.0227764 , b is  3.696957
4900 session is performed. cost is  0.020771228 , a is  3.0216722 , b is  3.7116482
```

## linreg2.py

위에 그린거를 그래프로 표시해준다.

선형 그래프 부분은 점을 잔뜩 찍어주고, sample부분들은 *로 찍어준다.

![linreg2](https://user-images.githubusercontent.com/26007107/61268139-8dc6cf00-a7d5-11e9-8042-6e4e0cde329f.png)


## linreg1.py (추가내용)

learning rate 라는게 있다.

위 linreg1.py에서 보았던 ``tf.train.GradientDescentOptimizer()`` 함수 안에 들어가는 숫자를 말하는데,

값이 커질수록 학습 속도가 빨라진다고 한다.

위의 linreg1.py의 경우, 0.001을 넣은 것이다.

0.01을 넣으면, 

```
0 session is performed. cost is  2878.4697 , a is  7.8649993 , b is  1.0699999
100 session is performed. cost is  inf , a is  1.6676783e+23 , b is  1.2534077e+22
200 session is performed. cost is  nan , a is  nan , b is  nan
300 session is performed. cost is  nan , a is  nan , b is  nan
400 session is performed. cost is  nan , a is  nan , b is  nan
(중략)
4500 session is performed. cost is  nan , a is  nan , b is  nan
4600 session is performed. cost is  nan , a is  nan , b is  nan
4700 session is performed. cost is  nan , a is  nan , b is  nan
4800 session is performed. cost is  nan , a is  nan , b is  nan
4900 session is performed. cost is  nan , a is  nan , b is  nan
```

값을 너무 크게 잡은 나머지 nan이 나온다.


하지만, 값을 너무 작게 넣는다면?

```
0 session is performed. cost is  1014.9256 , a is  0.507365 , b is  0.50057
100 session is performed. cost is  594.3899 , a is  1.1524049 , b is  0.5506957
200 session is performed. cost is  348.56784 , a is  1.6455439 , b is  0.58940417
300 session is performed. cost is  204.87343 , a is  2.0225463 , b is  0.61938274
400 session is performed. cost is  120.877014 , a is  2.3107553 , b is  0.642687
(중략)
4500 session is performed. cost is  2.5912442 , a is  3.2420177 , b is  0.7793366
4600 session is performed. cost is  2.5886683 , a is  3.2418985 , b is  0.78093827
4700 session is performed. cost is  2.5861003 , a is  3.2417793 , b is  0.7825357
4800 session is performed. cost is  2.5835323 , a is  3.24166 , b is  0.7841331
4900 session is performed. cost is  2.5809672 , a is  3.241541 , b is  0.7857305
```

학습이 덜 된다.

이번에는 learning rate 0.00001로 그대로 두고, for문 안에 있는 학습 횟수를 늘려보자.

for문의 range를 15000까지 늘려보니 ``cost is  2.3367393 , a is  3.229841 , b is  0.9415868`` 이다.

나름 가까워졌다.

이번엔 50000까지 해보았다. 

``cost is  1.6504333 , a is  3.1932254 , b is  1.4296687``

나름 가까워졌다.

대체 얼마나 해야 가까워질까 500000까지 해보았다.

``cost is  0.018899113 , a is  3.0206785 , b is  3.72495``
좋다


## linreg1.py (추가내용2)

이번엔 linear_random.txt 파일로 해보았다.

learning_rate 0.001에 학습횟수 5000 : ``cost is  9.329727 , a is  3.1305733 , b is  1.2699698``

진짜 이런걸 보니 정확한 답을 얻기 위해서는 여러번 시도해봐야 한다

아래부터는 여러번 시도해본 결과를 ``(learning_rate, learning_count) : result``로 표시해보았다.

```
(0.001, 5000) : cost is  9.329727 , a is  3.1305733 , b is  1.2699698
(0.002, 5000) : cost is  9.274495 , a is  3.1053298 , b is  1.7887061
(0.003, 5000) : cost is  nan , a is  nan , b is  nan

(0.002, 50000) : cost is  9.169217 , a is  3.0000033 , b is  3.9530783
```

위에 거를 또 그래프로 표시해본다

![linreg3](https://user-images.githubusercontent.com/26007107/61270485-c9b16280-a7dc-11e9-93b0-f901c1ed81b7.png)


왜 빨간 점들이 약해보이는지는 모르겠는데 잘 나온 듯 
