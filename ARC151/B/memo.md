自力で解けなかった
i=1~Nの、APiの整数列をAPとする

AとAPを辞書順で比較した際、下記の３つの関係性が存在する。
- A < AP　（この関係性になるAの組み合わせの数を X1とする）
- A = AP　（この関係性になるAの組み合わせの数を X2とする）
- A > AP　（この関係性になるAの組み合わせの数を X3とする）

A > AP となるAの組み合わせと　A < AP　となるAの組み合わせの数が同じになり
下記の等式が成り立つことに気づければ、A = APとなる　Aの組み合わせを調べる問題に変換できる

X1 = X3 = (N**m -  X2) // 2