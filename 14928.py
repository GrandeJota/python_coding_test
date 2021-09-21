import sys
import decimal

decimal.getcontext().prec = 1000000

n = decimal.Decimal(sys.stdin.readline())

print(n%(20000303))