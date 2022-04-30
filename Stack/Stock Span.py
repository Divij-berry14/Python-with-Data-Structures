def stock_span(price):
    output = [-1] * len(price)
    st_ = []
    output[0] = 1
    st_.append(0)

    for i in range(1, len(price)):
        while (not is_empty(st_)) and (price[top(st_)] < price[i]):
            st_.pop()

        if is_empty(st_):
            output[i] = i + 1
        else:
            output[i] = i - top(st_)

        st_.append(i)

    return output


def is_empty(st_):
    return len(st_) == 0


def top(st_):
    return st_[len(st_)-1]


n = int(input())
li = [int(x) for x in input().split()]
print(stock_span(li))