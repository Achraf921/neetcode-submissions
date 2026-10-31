class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #[1, 2, 3]
        #[9, 7, 9]
        #[6, 6, 7]
        # or we coult lowkey transpose that matrix and then reverse it

        # transpose:
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                r_ele = matrix[row][col]
                temp = matrix[col][row]
                matrix[col][row] = r_ele
                matrix[row][col] = temp

        # finally we just need to swap our rows
        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]


        