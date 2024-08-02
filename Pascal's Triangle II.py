from typing import List

def getRow(rowIndex: int) -> List[int]:
    row = [1] * (rowIndex + 1)
    for i in range(1, rowIndex):
        row[i] = row[i - 1] * (rowIndex - i + 1) // i
    return row


print(getRow(4))
