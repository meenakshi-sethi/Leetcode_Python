# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#Approach 1: Two Pointer Approach

def maxProfit(prices):
    if not prices:
        return 0
    
    # two pointer approach
    left, right = 0, 1 #left = buy and right = sell 
    max_profit = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    
    return max_profit

# Test cases
print("Two Pointer Approach:")
print(maxProfit([7, 2, 5, 1, 7, 4]))  # Output: 6
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0
print(maxProfit([]))  # Output: 0
print(maxProfit([1, 2, 3, 4, 5]))  # Output: 4
print(maxProfit([5, 4, 3, 2, 1]))  # Output: 0

# Time Complexity: O(n)
# Space Complexity: O(1)


# Approach 2: Brute Force Approach
def maxProfitBF(prices):
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

# Test cases
print("Brute Force Approach:")
print(maxProfitBF([7, 2, 5, 1, 7, 4]))  # Output: 6
print(maxProfitBF([7, 1, 5, 3, 6, 4]))  # Output: 5
print(maxProfitBF([7, 6, 4, 3, 1]))  # Output: 0
print(maxProfitBF([]))  # Output: 0
print(maxProfitBF([1, 2, 3, 4, 5]))  # Output: 4
print(maxProfitBF([5, 4, 3, 2, 1]))  # Output: 0

# Time Complexity: O(n^2)
# Space Complexity: O(1)    
# Note: The brute force approach is not efficient for large input sizes,
# as it checks every possible pair of buy and sell days, leading to time complexity and Time Limit Exceeds.

# Approach 3: Greedy Approach - (pending)


