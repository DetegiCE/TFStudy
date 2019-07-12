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
