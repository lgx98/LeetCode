# @before-stub-for-debug-begin
# from python3problem274 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#


# @lc code=start
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        
        """
        Variables:
            val_lo (int): binsearch lower limit, a legal h-index
            val_hi (int): binsearch upper limit, an illegal h-index
            idx_lo (int): all(num < val_lo for num in citations[:idx_lo])
            idx_hi (int): all(num >= val_hi for num in citations[idx_hi:])
        """
        val_lo, val_hi, idx_lo, idx_hi = 0, len(citations) + 1, 0, len(citations)

        ## binary-search largest psuedo h-index
        # A psuedo h-index is defined as a value of h such that
        # the given researcher has published at least h papers that
        # have each been cited at least h times.
        # It is possible to use binary search here because:
        # if x is a psuedo h-index, any number less than x is a psuedo h-index; and
        # we are finding the lmaximum of it.
        while val_lo + 1 < val_hi:
            val_pivot = (val_lo + val_hi) // 2

            # partition [lo,hi) into [lo, retval) and [retval, hi), where left < pivot_val and right >= pivot_val
            # similar to quicksort/topk, but the pivot is a custom value instead of an element from the array
            # partition is used to:
            # 1) find how many numbers are no less than val_pivot
            # 2) partially order the array to exponentially(statistical expectation) cut down serach range for the next iteration
            # 3) be somewhat friendly to cache and next-line prefetcher; might need pointer-chase prefetcher to help python
            lo, hi = idx_lo, idx_hi
            temp = citations[lo]  # save first element, add back at last
            hi -= 1
            while lo < hi:
                while (lo < hi) and (val_pivot <= citations[hi]):
                    hi -= 1
                citations[lo] = citations[hi]
                while (lo < hi) and (val_pivot > citations[lo]):
                    lo += 1
                citations[hi] = citations[lo]
            citations[lo] = temp  # add back saved first element
            if temp < val_pivot:  # move the index of pivot accordingly
                lo += 1

            # if this val_pivot qualifies for a psuedo h-index
            if len(citations) - lo >= val_pivot:
                # search right half (larger psuedo h-indexex)
                val_lo, idx_lo = val_pivot, lo
            else:
                # vice versa
                val_hi, idx_hi = val_pivot, lo

        return val_lo


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    citations = [10, 11]
    result = s.hIndex(citations)

    # guess, partitioned
    #     2, [1,0,3,6,5]
    # guess, partitioned
    #     3, [1,0,3,6,5]

    # citations_examined, best_candidate, n_ge_candidate, counter_lt_candidate
    #             0,              5,              0,                   {}
    #             1,              4,              0,                {3:1}
    #             2,              3,              1,                {0:1}
    #             3,              3,              2,                {0:1}
    #             4,              3,              2,            {0:1,1:1}
    #             5,              3,              3,            {0:1,1:1}
    print(result)
    print(citations)
