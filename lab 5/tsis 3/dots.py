def histogram(inputList):

    for i in range(len(inputList)):
        print (inputList[i]*'*')


List = list(map(int, input().split()))

histogram(List)
