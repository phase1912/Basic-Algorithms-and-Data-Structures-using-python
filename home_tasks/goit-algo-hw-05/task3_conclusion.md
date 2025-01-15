# Analysis of Searching Algorithms: Boyer Moore, Knut Morris Pratt, Rabin Karp

## Results
The detailed comparison is shown in the table below:

| File      | Pattern          | Boyer Moore Time (s) | Knut Morris Pratt Time (s) | Rabin Karp Time (s) |
|-----------|------------------|----------------------|----------------------------|---------------------|
| text1.txt | алгоритми        | 0.000020             | 0.000033                   | 0.000079            |
| text1.txt | somenotexisttext | 0.000217             | 0.000988                   | 0.002730            |
| text2.txt | Параметри        | 0.000419             | 0.001278                   | 0.002735            |
| text2.txt | somenotexisttext | 0.000289             | 0.001450                   |    0.004106         |


## Conclusion
Fastest algorithm overall: Boyer Moore Time (s)
