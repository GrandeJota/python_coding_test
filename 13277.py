import sys
import decimal

decimal.getcontext().prec = 600000
a, b = ((decimal.Decimal(i) for i in sys.stdin.readline().split()))

print(a*b)