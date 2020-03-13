# function to find first index >= x
def lowerIndex(arr, n, x):
    l = 0
    h = n - 1
    while (l <= h):
        mid = int((l + h) / 2)
        if (arr[mid] >= x):
            h = mid - 1
        else:
            l = mid + 1
    return l


# function to find last index <= x
def upperIndex(arr, n, x):
    l = 0
    h = n - 1
    while (l <= h):
        mid = int((l + h) / 2)
        if (arr[mid] <= x):
            l = mid + 1
        else:
            h = mid - 1
    return h


# function to count elements within given range
def countInRange(arr, n, x, y):
    # initialize result
    count = 0;
    count = upperIndex(arr, n, y) - lowerIndex(arr, n, x) + 1;
    return count


def jobOffers4(scores, lowerLimits, upperLimits):
    answer = []
    scores.sort()
    n = len(scores)
    for index, _ in enumerate(lowerLimits):
        answer.append(countInRange(scores, n, lowerLimits[index], upperLimits[index]))
    return answer


def count_dp_bottom(n, scores, end_index):

    table = [0 for i in range(n + 1)]

    # base case
    table[0] = 1

    # One by one consider given 3 scores and update the
    # table[] values after the index greater than or equal
    # to the value of the picked score.
    for i in range(3, n + 1):
        table[i] += table[i - 3]
    for i in range(5, n + 1):
        table[i] += table[i - 5]
    for i in range(10, n + 1):
        table[i] += table[i - 10]

    return table[n]



def jobOffers(scores , lowerlimit,upperlimit):

     n = len(scores)
     table = [0 for i in range(len(lowerlimit))]

     #base case
     table[0] = 0
     candidate = []
     answer =[]



     for i in  range(len(lowerlimit)):
         for j in range(len(scores)):

             if  scores[j] >= lowerlimit[i] and j<= upperlimit[i]:
                 print str("jude") + str(scores[j])
                 table.insert(i,scores[j])

                 candidate.insert(i,len(table))

         answer.append(len(candidate))
     return candidate



myscore =[4,8,7 ]
mylowerlimit = [2,4]
myupperlimit =[8,4]




print(jobOffers(myscore,mylowerlimit,myupperlimit))