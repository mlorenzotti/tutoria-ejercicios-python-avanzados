memo={}
def formas(n):
    if n<0:
        return 0
    if n==0:
        return 1
    if n not in memo:
        memo[n]=formas(n-1)+formas(n-2)+formas(n-3)
    return memo[n]
    
for escalones in [4, 10, 30]:
 print("Escalones:", escalones, "- Formas:", formas(escalones))