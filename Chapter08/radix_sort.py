from counting_sort import counting_sort

def radix_sort(arr, max_len):
  """
  >>> a = [1,4,2,6,74,2,56,8,39]
  >>> radix_sort(a, 2)
  [1, 2, 2, 4, 6, 8, 39, 56, 74]
  """
  result = arr
  for length in range(1, max_len + 1):
    digit_getter = lambda num: num % pow(10, length) // pow(10, length - 1)
    result = counting_sort(result, digit_getter)

  return result
