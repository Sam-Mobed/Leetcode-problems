"""
Just to test stuff.
"""

def climbStairs(n: int) -> int:
        table={key: 0 for key in range(1, n+1)} #initialize the table
        table[1]=1
        def dp(n,table):
            if n==0:
                return 1
            elif table[n]!=0:
                return table[n]
            else:
                table[n] += dp(n-1,table) + dp(n-2,table)
        
        dp(n,table)
        return table[n]

climbStairs(3)