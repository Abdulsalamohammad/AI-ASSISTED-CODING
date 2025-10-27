"""
Quicksort vs Bubble Sort — Python implementations with step-by-step comments

WHERE THEY DIFFER (at a glance)
---------------------------------------------------------------------------
Strategy:
  • Quicksort: Divide-and-conquer. Pick a pivot, partition the array around it,
               then recursively sort the left and right parts.
  • Bubble sort: Repeatedly compare adjacent elements and "bubble" the largest
                 one to the end each pass.

Time complexity:
  • Quicksort:   Average O(n log n), Worst O(n^2) (bad pivots).
  • Bubble sort: O(n^2) in average and worst case; O(n) best case if the array
                 is already sorted and we stop early when no swaps occur.

Space complexity:
  • Quicksort:   O(log n) extra due to recursion (in-place partition).
  • Bubble sort: O(1) extra.

Stability (do equal items keep their original relative order?):
  • Quicksort (in-place variant here): NOT stable.
  • Bubble sort: Stable (adjacent swaps preserve order of equals).

When to use:
  • Quicksort is the practical go-to for large, random data (fast on average).
  • Bubble sort is simple for teaching/small inputs, but rarely used in practice
    on large data because it's O(n^2).
"""

from typing import List
import random


def quicksort(arr: List[int]) -> List[int]:
    """
    In-place quicksort (Lomuto partition) with a randomized pivot to avoid
    consistently bad splits on already-sorted data.

    Steps (high-level):
      1) Recursively sort a subarray arr[lo:hi+1].
      2) Choose a pivot (random index in [lo, hi]) and move it to the end.
      3) Partition: scan the subarray; move <= pivot to the left side.
      4) Put the pivot into its final position; everything left is <= pivot,
         everything right is > pivot.
      5) Recurse on the left and right sides.

    Returns the same list object (sorted in-place) for convenience.
    """

    def partition(lo: int, hi: int) -> int:
        # --- Step 2: choose a random pivot to reduce chance of worst-case O(n^2)
        pivot_index = random.randint(lo, hi)
        arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]
        pivot = arr[hi]  # pivot value now at the end

        # i will track the "boundary" between <= pivot (to the left) and > pivot (to the right)
        i = lo - 1

        # --- Step 3: scan arr[lo:hi), moving elements <= pivot to the left side
        for j in range(lo, hi):
            # If current element belongs to the <= pivot region...
            if arr[j] <= pivot:
                i += 1
                # ...swap it just after the last element known to be <= pivot
                arr[i], arr[j] = arr[j], arr[i]

        # --- Step 4: place the pivot in its final sorted position (i+1)
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        return i + 1  # pivot's index; left side <= pivot, right side > pivot

    def _quicksort(lo: int, hi: int) -> None:
        # --- Base case: one or zero elements are already sorted
        if lo >= hi:
            return
        # Partition the subarray and get pivot's final place
        p = partition(lo, hi)
        # --- Step 5: recursively sort the two halves (excluding the pivot)
        _quicksort(lo, p - 1)
        _quicksort(p + 1, hi)

    # Guard for empty list (works fine without, but this is explicit)
    if len(arr) <= 1:
        return arr

    _quicksort(0, len(arr) - 1)
    return arr  # sorted in-place


def bubble_sort(arr: List[int]) -> List[int]:
    """
    In-place bubble sort with early-exit optimization.

    Steps (high-level):
      1) Make repeated passes from start to end-1.
      2) Compare each adjacent pair (arr[j], arr[j+1]).
      3) If they are out of order, swap them so the larger one moves right.
      4) After the i-th pass, the i largest elements are in place at the end,
         so we can shorten the next pass by i.
      5) If a full pass makes no swaps, the array is already sorted (stop early).

    Returns the same list object (sorted in-place) for convenience.
    """
    n = len(arr)
    if n <= 1:
        return arr

    # Outer loop controls how many passes we make
    for i in range(n - 1):
        swapped = False  # Track whether we performed any swaps in this pass

        # Inner loop: compare adjacent pairs up to the last unsorted index (n-1-i)
        for j in range(0, n - 1 - i):
            # --- Step 2: compare neighbors
            if arr[j] > arr[j + 1]:
                # --- Step 3: swap if out of order (this "bubbles" the larger value rightward)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # --- Step 5: no swaps means the array is already sorted; break early (best case O(n))
        if not swapped:
            break

    return arr  # sorted in-place


if __name__ == "__main__":
    # Demo / quick test
    data1 = [5,6,8,1,2,3,7,4,9,10]
    data2 = data1.copy()

    print("Original:", data1)
    print("Quicksort:", quicksort(data1))   # sorts in-place, returns the same list
    print("Bubble   :", bubble_sort(data2)) # sorts in-place, returns the same list
