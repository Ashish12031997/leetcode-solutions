from typing import List
def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
        total_unit = 0
        sorted_arr = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        for i,j in sorted_arr:
            if truckSize > 0:
                if truckSize <i:
                    total_unit += j*truckSize
                    break
                truckSize -= i
                total_unit += j*i
            else:
                break
        return total_unit

print(maximumUnits([[1,3],[2,2],[3,1]],4))
