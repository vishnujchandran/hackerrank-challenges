# DIAGONAL DIFFERENCE

<p>Given a square matrix, calculate the absolute difference between the sums of its diagonals.</p>
<p>For example, the square matrix  is shown below:</p>
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9 = 15.
The right to left diagonal = 3+5+9 = 17. 
Their absolute difference is |15 - 17| = 2 .

<p><strong>Function description</p></strong>

<p>Complete the diagonalDifference function in the editor below.</p>
<p>diagonalDifference takes the following parameter:</p>
  int arr[n][m]: an array of integers

<p><strong>Return</p></strong>
int: the absolute diagonal difference

<p><strong>Input Format</p></strong>
<p>The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
Each of the next  lines describes a row, arr[i], and consists of n space-separated integers arrr[i][j].</p>
<p><strong>Output Format</p></strong>
Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

<p><strong>Sample Input</p></strong>
<pre><code>3
11 2 4
4 5 6
10 8 -12</pre></code>
<p><strong>Output</p></strong>
<pre><code>15</pre></code>

<p><strong>Explanation</p></strong>

The primary diagonal is:
11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15
