

# f (n) = (n - 1) + f (n - 1)
 # f (0) = 0


def countEdges1(n):


    table = [[] for i in range(n)]

    sum = 0

    for i in range(n):
        # add all edge that are linked
        # to the current vertex

        sum += i
        table.append(sum)

        return sum // 2




#1- It is n(n-1)/2 for undirected.

# 2- And n(n-1) for directed.

# Where n is the number of vertices.


def countEdges(n):



    for i in range(n):
        if i <= n-2:
            edges = n - 1
         return n*(n-1) /2
    else:
        return n*(n-1)


print(countEdges(4))


def countedges2(n):

    memo = {}
    # Base cases
    if n  == 0:
        return 0

        # See if we've already calculated this
    if n in memo:
        print n
        return memo[n]

    result = (n - 1) + countedges2(n - 2)

    # Memoize
    memo[n] = result


    return result;