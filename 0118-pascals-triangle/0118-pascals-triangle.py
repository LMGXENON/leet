class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = [1]

        for i in range(numRows):
            triangle.append(row)
            next_row = [1]

            for j in range(len(row) - 1):
                next_row.append(row[j] + row[j + 1])
            next_row.append(1)

            row = next_row

        return triangle

