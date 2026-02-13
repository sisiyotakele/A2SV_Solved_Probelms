class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        tr = [[0] * cols for _ in range(rows)]
        for r in range(len(img)):
            for c in range(len(img[0])):
                total = 0
                count  =0 
                for nr in range(max(0, r-1), min(rows, r+2)):
                    for nc in range(max(0, c-1), min(cols, c+2)):
                        total += img[nr][nc]
                        count += 1
                tr[r][c] = total // count
        return tr
