from functools import cmp_to_key


def solution(data, ext, val_ext, sort_by):
    cols = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    def cmp(x, y):
        return x[cols[sort_by]] - y[cols[sort_by]]


    data = [row for row in data if row[cols[ext]] <= val_ext]

    answer = sorted(data, key=cmp_to_key(cmp))
    return answer