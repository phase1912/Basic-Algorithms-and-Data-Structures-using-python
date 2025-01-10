# Analysis of Sorting Algorithms: Merge Sort, Insertion Sort, and Timsort

## Results
The detailed comparison is shown in the table below:

| Array Size | Merge Sort Time (s) | Insertion Sort Time (s)  | Timsort Time (s) |
|---------|----------------------|--------------------------|------------------|
| 1000    | 0.001238             | 0.015888                 | 0.000079             |
| 10000   | 0.019055             | 1.659607                 | 0.000970             |
| 100000  | 0.202117             | N/A                      | 0.018052             |

(Note: The `N/A` for Insertion Sort indicates that it was not tested for larger datasets due to inefficiency.)

## Conclusion
Timsort's efficiency stems from its hybrid design, which:
1. Uses Merge Sort for its logarithmic complexity on large datasets.
2. Incorporates Insertion Sort for efficiently handling small or nearly sorted segments.

This combination ensures optimal performance across various scenarios, making it the default choice for Python's sorting operations. The empirical analysis validates the theoretical complexities and demonstrates why Timsort is the preferred algorithm for general-purpose sorting tasks.
