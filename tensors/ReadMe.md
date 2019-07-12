This part is Chapter 6 in book

It mainly talks about tensor(array) linear calculations in tensorflow

## tensors1.py

~~~python
[[2 4]
 [4 6]]
[[0 0]
 [0 0]]
~~~

## tensors2.py

* *multiply* : 진짜 그 위치의 원소끼리 곱함
* *matmul* : 진짜 행렬 곱셈

~~~python
[[ 1  4]
 [ 9 16]]
[[ 7 10]
 [15 22]]
~~~

## tensors4.py

입력데이터 data는 python의 list 자료구조이다.
```
data = [[1],[2],[3],[4]]
```
이 자료형이 tensor로 입력되었다가
```
a = tf.placeholder(dtype=tf.float32, shape=[None,1])
```
다시 변수로 취했는데
```
a_out = sess.run(a,feed_dict={a:data})
```
numpy.ndarray 형으로 변환되었다.

* *tf.placeholder* : 연산시 반드시 feed_dict={}의 중괄호 내부에 입력되는 변수를 지정
* *shape=[None,1]* : None x 1 행렬로, None은 알 수 없는 건데 데이터가 계속 들어오는 때를 대비하여 이렇게 한다고 

~~~python
input data type is  <class 'list'>
a type is <class 'numpy.ndarray'>
~~~

## tensors5.py

tensorflow로 하나 numpy로 하나 결과는 같다라는것을 보여주는 코드

*결과 값은 tensors2.py와 동일*

## tensors6.py

4x3행렬이랑 1x3행렬을 더한다는게 말이 안되는데 이게 **broadcasting** 기법이란다

차원을 늘리는건 되는데 줄이는건 안됨

tensors7.py를 보니까 4x3이랑 1x4로 해놨던데

얘들은 당연히 차원이 안맞는 예시를 보여주고 에러가 난다고 한다.

## tensors8.py

얘도 늘려주는거란다.

앞에거 뒤에거 둘다

이런걸 **broadcasting**이라고 한다.

## tensors9.py


~~~python
first 
 [0 1 2 3 4 5]
second 
 [[0 1 2]
 [3 4 5]]
thrid 
 [[0 1]
 [2 3]
 [4 5]]
~~~

이제보니까 위에 third 오타났네

arange 함수는 0~n-1까지 리스트(정확히는 numpy.ndarray)에 넣어주는 함수 같다

reshape는 [n,m]이라 하면 nxm짜리로 위에거를 바꿔주는것 같다.


## tensors10.py

위에서는 numpy로 했다면 이번에는 tensorflow로 reshape를 했다

이번에는 좀 다른점은 reshape에 -1이 들어간건데, 나머지를 함수가 알아서 채우라는 거라고 한다.

```
[[ 1.  2.  3.]
 [ 3.  4.  5.]
 [ 5.  6.  7.]
 [ 8.  9. 10.]]
```

뭔가 이해가 안되서 한번 써봐야겠다

```
1 2 3   0 0 0   1 2 3
2 3 4 + 1 1 1 = 3 4 5
3 4 5   2 2 2   5 6 7
4 5 6   4 4 4   8 9 10
```

ㅇㅎ
