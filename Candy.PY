def candy(ratings):
    n = len(ratings)
    total_candy = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            total_candy[i] = total_candy[i - 1] + 1
            print(total_candy)

    for n in range(n - 2, -1, -1):
        if ratings[n] > ratings[n + 1]:
            total_candy[n] = max(total_candy[n], total_candy[n + 1] + 1)
            print(total_candy)

    return sum(total_candy)


# ratings = [1,3,2,2,1]
ratings = [1, 2, 87, 87, 87, 2, 1]
# ratings = [1, 0, 2]
# ratings = [1,2,2]
c = candy(ratings)

print(c)
