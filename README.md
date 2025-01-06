# Uncommon Python Error: ZeroDivisionError in Nested Conditional
This repository demonstrates a subtle error in Python that can lead to a `ZeroDivisionError` even when explicit checks seem to be in place.

The error occurs due to an oversight in handling the case where the second argument (`b`) is zero. The code prioritizes checking `a` first. If `a` is non-zero but `b` is zero, the division operation still proceeds, leading to the error.

The solution involves reorganizing the conditional checks to catch the zero division error more effectively before the division operation is attempted.

## How to reproduce the bug
1. Clone this repository
2. Run `bug.py`
3. Observe the `ZeroDivisionError`.

## Solution
The solution is provided in `bugSolution.py`, reordering conditions to prioritize the check for a zero denominator.