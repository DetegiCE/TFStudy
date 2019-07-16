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
