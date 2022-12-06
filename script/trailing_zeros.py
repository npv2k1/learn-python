def trailing_zeros(n):
  if n == 0:
    return 0
  k = 1
  tz = 0
  while 5 ** k <= n:
    tz += n // 5 ** k
    k += 1
  return tz


print(trailing_zeros(204))
print(trailing_zeros(205))
print(trailing_zeros(206))
print(trailing_zeros(207))
