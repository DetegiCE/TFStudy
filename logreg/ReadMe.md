Logistic Regression 이라는걸 배운다.

뭔가 엄청난 회귀모형들이 있다.

* 로지스틱 회귀모형
* 로지스틱 단순회귀모형
* 다항 로지스틱 회귀모형

일단 자료들을 가져오란다.

[링크](http://yann.lecun.com/exdb/mnist)

코드를 진행하면서 보니까 굳이 내가 받아올 필요가 없었다.


## logreg1.py

``
train_x_data shape is  (55000, 784) , train_y_data shape is  (55000, 10)
``

## logreg2.py

logreg2는 별거 없다

그냥 logreg1에서 breakpoint를 찍으면서 숫자를 확인하고, 그 숫자가 얼마인지 데이터들에서 뜯어본다.

1st_digit의 경우, ㅋ이나 3처럼 생겼지만 사실은 7이었고

2nd_digit의 경우, 3이었다.
