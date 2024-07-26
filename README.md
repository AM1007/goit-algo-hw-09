# Greedy algorithms and dynamic programming

### Task Description

In the notes, we discussed an example of breaking down a sum into coins. We have a set of coins `[50, 25, 10, 5, 2, 1]`. Imagine you are developing a system for a cash register that needs to determine the optimal way to give change to a customer.

You need to write two functions for the cash register system that dispenses change to the customer:

1. Greedy Algorithm Function: find_coins_greedy
   This function should take an amount to be given as change and return a dictionary with the number of coins of each denomination used to make up that amount. For example, for an amount of 113, this would be the dictionary `{50: 2, 10: 1, 2: 1, 1: 1}`. The algorithm should be greedy, meaning it should first choose the largest available denominations of coins.

2. Dynamic Programming Function: find_min_coins
   This function should also take an amount for change but use dynamic programming to find the minimum number of coins needed to make up that amount. The function should return a dictionary with the denominations of coins and their quantities to achieve the given amount in the most efficient way. For example, for an amount of 113, this would be the dictionary `{1: 1, 2: 1, 10: 1, 50: 2}`.

Compare the efficiency of the greedy algorithm and the dynamic programming algorithm based on their execution time or Big-O notation, and consider their performance with large amounts. Highlight how they handle large sums and why one algorithm might be more efficient than the other in certain situations. Add your conclusions to the readme.md file of the homework assignment.

### Results of algorithm testing

| Amount | Greedy Algorithm Function (s) | Dynamic Programming Function (s) |
| -----: | ----------------------------: | -------------------------------: |
|     10 |                     0.0002378 |                        0.0044103 |
|     55 |                     0.0002895 |                         0.027688 |
|    113 |                     0.0003526 |                        0.0625774 |
|    207 |                     0.0003163 |                         0.121451 |
|    505 |                     0.0002632 |                         0.337086 |
|   1001 |                     0.0002756 |                         0.736058 |

#### 1. Greedy Algorithm

**Description:**
The greedy algorithm selects the highest denomination coins that can be used until the amount is fully distributed.

**Time Complexity:**

Coin iteration: Each coin is checked once, so the time complexity depends on the number of coins in the set.
Random amount: It depends on how quickly the amount can be distributed using the largest coins.
On average, the time complexity of the greedy algorithm can be considered O(n), where n is the number of coins in the set. However, for specific implementations, this complexity may vary depending on the coin set and the amount.

> The greedy algorithm works optimally when the coin denominations form "satisfactory" structures (e.g., multiples of each other). Otherwise, its effectiveness can be reduced, and it may not find the optimal solution for all sets of coins.

#### 2. Dynamic Programming Algorithm

**Description:**
The dynamic programming algorithm uses a table to store the minimum number of coins needed to achieve each amount up to the target amount.

**Time Complexity:**

Initialization: Initializing the min*coins and coin_count arrays takes O(m), where m is the amount to be distributed.
Table filling: For each coin and each amount up to the target amount, the algorithm performs checks and updates the table. This has a complexity of O(c * m), where c is the number of coins and m is the amount.
Therefore, the overall time complexity of the dynamic programming algorithm is O(c \_ m), where c is the number of coins and m is the amount for which the distribution is needed.

> Dynamic programming always finds the optimal solution and is suitable if the coin set can be arbitrary. However, its time complexity can be high for large amounts, requiring more computational resources.

#### Conclusions:

The greedy algorithm typically has lower time complexity compared to dynamic programming and is faster in simple cases where the coin denominations allow for a greedy approach. However, its efficiency can decrease with more complex sets of coins.

Dynamic programming ensures an exact result and is suitable for any set of coins but may have higher time complexity and require more memory, especially for large amounts.
