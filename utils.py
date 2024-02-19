def fact(n):
	m=1
	for i in range(1, n+1):
		m*=i
	return m
def isfive(n):
	while n%5==0:
		n=n//5
	return n=1
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)
def is_p(n):
    if (fact(n-1)+1)%n==0:
        return "YES"
    return "NO"
