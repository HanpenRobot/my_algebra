線形作用素の環
ベクトル空間XからXへの線形作用素の全体
```math
A=Hom(X,X)
```

Aにベクトル算法を
```math
(ag+bg)(x)=af(x)+bg(x) ,(f,g \in A, a,b \in K)
```
と定義して、Aをベクトル空間と考えると

```math
x: f \mapsto y=f(x)
```
の考え方(線形写像自身に空間の構造を規定する役割を担わせる考え方)で

```math
Hom(A,X)=X
```

とみなせる。次にある線形方程式
```math
Lx=0
```

を満たす解の集合$`Ker(L)\subset X`$とは何かを考えてみる。線形写像$`M,L \in A=Hom(X,X)`$どうしの積$`M\circ L`$を
```math

M\circ L=M(Lx)
```

$`M(Lx)`$は線形写像$`M,L \in A=Hom(X,X)`$の合成写像を意味する。すると$A=Hom(X,X)`$は環とみなすことができる。
```math
J_{L}={M\circ L; M \in A=Hom(X,X)}
```
とおいて、商環$`A/J_{L}`$を考えると

```math
Hom(A/J_{L},X)=Ker(L)
```
となる。実際、$`A \in A/J_{L}`$に対して、$`x \in X=Hom(A,X)`$が定める線形写像は
```math
Hom(A,X)=X \ni x: A \mapsto Ax=(A+M \circ L)x, (\forall M \in A=Hom(X,X))
```
