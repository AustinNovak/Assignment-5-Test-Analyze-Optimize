from collections import Counter

# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.

def most_frequent(numbers):
    if not numbers:
        return None
    freq = Counter(numbers)
    return max(freq, key=freq.get)


"""
Time and Space Analysis for Problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(k), where k = number of unique elements.
- Why this approach? Counter is built for counting items quickly and clearly.
- Could it be optimized? Not really; all items must be checked once.
- Trade-offs: Counter is simple and efficient but uses extra memory.
"""

# Test Cases
print("Problem 1 Tests:")
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # → 3
print(most_frequent([5, 5, 5]))              # → 5
print(most_frequent([1, 2, 3, 4]))           # → any of them
print(most_frequent([]))                     # → None
print()


# 🔍 Problem 2: Remove Duplicates While Preserving Order

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


"""
Time and Space Analysis for Problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Keeps order while removing duplicates using a set.
- Could it be optimized? Not much — sets are already efficient.
- Trade-offs: Slightly higher space use for the set.
"""

# Test Cases
print("Problem 2 Tests:")
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # → [4, 5, 6, 7]
print(remove_duplicates([]))                  # → []
print(remove_duplicates([1, 1, 1, 1]))        # → [1]
print(remove_duplicates([1, 2, 3]))           # → [1, 2, 3]
print()


# 🔍 Problem 3: Return All Pairs That Sum to Target

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs


"""
Time and Space Analysis for Problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Hash lookup makes it much faster than nested loops.
- Could it be optimized? Not significantly for unsorted data.
- Trade-offs: Uses more memory for speed.
"""

# Test Cases
print("Problem 3 Tests:")
print(find_pairs([1, 2, 3, 4], 5))     # → [(1, 4), (2, 3)]
print(find_pairs([0, -1, 2, -3, 1], -2))  # → [(-3, 1)]
print(find_pairs([5, 7, 9, 13, 11, 6, 8], 14))  # → [(5, 9), (7, 7) none, etc.]
print(find_pairs([], 5))                # → []
print()


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)

def add_n_items(n):
    capacity = 1
    arr = []
    for i in range(n):
        if len(arr) == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            capacity *= 2
        arr.append(i)
    print("Final list:", arr)


"""
Time and Space Analysis for Problem 4:
- Best-case: O(1) → Appending when there’s free space.
- Worst-case: O(n) → Happens during a resize when copying items.
- Average-case (amortized): O(1)
- Space complexity: O(n) → Depends on number of elements added.
- Why this approach? This mimics how real dynamic arrays resize internally.
- Could it be optimized? No — doubling is already the most efficient.
- Trade-offs: Doubling uses more temporary memory but makes inserts fast overall.
"""

# Test Cases
print("Problem 4 Tests:")
add_n_items(1)
add_n_items(6)
print()


# 🔍 Problem 5: Compute Running Totals

def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result


"""
Time and Space Analysis for Problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? It’s simple and efficient using one pass.
- Could it be optimized? Yes, we can update the list in-place to save space.
- Trade-offs: In-place saves memory but changes the original data.
"""

# Test Cases
print("Problem 5 Tests:")
print(running_total([1, 2, 3, 4]))  # → [1, 3, 6, 10]
print(running_total([0, 0, 0]))     # → [0, 0, 0]
print(running_total([-1, 1, -1, 1]))  # → [-1, 0, -1, 0]
print(running_total([]))             # → []
print()


# Step 5: Optimized Version (In-Place Running Total)

def running_total_optimized(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


"""
Optimization Comparison (Problem 5):
- Original Time: O(n)
- Optimized Time: O(n)
- Original Space: O(n)
- Optimized Space: O(1)
- Explanation: Updates the same list instead of creating a new one.
  Saves memory but changes the input data.
"""

# Test Cases for Optimized Version
print("Optimized Running Total Tests:")
print(running_total_optimized([1, 2, 3, 4]))  # → [1, 3, 6, 10]
print(running_total_optimized([5]))           # → [5]
print(running_total_optimized([]))            # → []
print()
