# <!-- Codeforces 1593A — Elections -->

# <!-- Given 3 candidates' vote counts, determine for each candidate how many additional votes they need to become strictly greater than both other candidates. -->




n = int(input())

for i in range(n):
    a,b,c = map(int,input().split())

    m = max(a,b,c)

    ansa = 0
    ansb = 0
    ansc = 0

    if a==m:
        if m==b:
            ansa = 1
            ansb = 1
        else:
            ansb = a-b+1

        if m==c:
            ansa = 1
            ansc = 1
        else:
            ansc = a-c+1
    elif b==m:
        ansa = b-a+1
        if c==m:
            ansb = 1
            ansc = 1
        else:
            ansc = b-c+1
    else:
        ansc = 0
        ansa = c-a+1
        ansb = c-b+1

    print(ansa,ansb,ansc)