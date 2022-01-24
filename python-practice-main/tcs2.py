"""Product of Quadruplet
A non-empty array A consisting of N numeric values is given.

The product of quadruplet (P, Q, R, S) equates to A[P] * A[Q] * A[R] * A[S] (0 < P < Q < R < S < N).

For example, array A such that:

A[0] = -3 A[1] = 1 A[2] = 2 A[3] = -2 A[4] = 5 A[5] = 6 A[6] = 1

•(0, 1, 2, 3), product is -3 * 1 * 2 * -2 = 12

•(1, 2, 4, 5), product is 1 * 2 * 5 * 6 = 30

•(2, 4, 5, 6), product is 2 * 5 * 6 * 1 = 60

60 is the product of quadruplets (2, 4, 5, 1), which is maximal.

Your goal is to find the maximal product of any quadruplet for input Array A[ ].

Write an efficient algorithm for the following assumptions:

•N is an integer within the range [4..100,000);

Example 1:

Input:

5

3

3

3

3

3

Output:

81



Example2:

Input:

Enter count of values you are going to insert:

3

Enter 3 numbers:

2

3

3

Output:

Invalid Input

"""
a = []
max = 0
for i in range(int(input())):
    a.append(int(input()))
if len(a) <= 3:
    print("invalid input")
else:
    for i in range(len(a)):
        for j in range(i, len(a)):
            for k in range(j, len(a)):
                for l in range(k, len(a)):
                    b = a[i]*a[j]*a[k]*a[l]
                    if b > max:
                        max = b
if max != 0:
    print(max)
