class SparseMatrix:
    def __init__(self, data):
        self.data = data  # (i, j, v) 형태의 튜플 리스트로 표현된 희소 행렬 데이터

    def add(self, other):
        result = []
        i = j = 0

        while i < len(self.data) and j < len(other.data):
            if self.data[i][:2] == other.data[j][:2]:
                result.append(
                    (
                        self.data[i][0],
                        self.data[i][1],
                        self.data[i][2] + other.data[j][2],
                    )
                )
                i += 1
                j += 1
            elif self.data[i][:2] < other.data[j][:2]:
                result.append(self.data[i])
                i += 1
            else:
                result.append(other.data[j])
                j += 1

        # 남은 요소 추가
        while i < len(self.data):
            result.append(self.data[i])
            i += 1

        while j < len(other.data):
            result.append(other.data[j])
            j += 1

        return SparseMatrix(result)

    def __str__(self):
        return str(self.data)


def main():
    # 예시 희소 행렬 생성
    sparse1 = SparseMatrix([(1, 1, 5), (2, 3, 3), (4, 5, 7)])
    sparse2 = SparseMatrix([(1, 1, 2), (2, 2, 4), (3, 3, 6)])

    # 덧셈 연산 수행
    result = sparse1.add(sparse2)
    print(result)


main()
