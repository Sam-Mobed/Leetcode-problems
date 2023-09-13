"""
Just to test stuff.
"""

def minimumTimeRequired(jobs, k: int) -> int:

    def backtrack(i,currMaxTime):
        nonlocal ans,n,workers

        if currMaxTime>=ans:
            return ans
        
        if i==n:
            ans = min(ans,currMaxTime)
            return
        
        timeset = set()
        for j in range(k):
            if workers[j] not in timeset:
                workers[j] += jobs[i]
                backtrack(i+1, max(currMaxTime, workers[j]))
                workers[j]-=jobs[i]

                timeset.add(workers[j])

    n = len(jobs)
    workers = [0]*k
    ans = float('inf')

    backtrack(0,0)

    return ans


minimumTimeRequired([3,2,3],3)
