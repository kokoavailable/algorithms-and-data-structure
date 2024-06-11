def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  # 입력 배열을 두개로 나누며, 각 하위 배열에 대해 다시 병합 정렬을 호출한다.
  left_half = merge_sort(arr[:mid])
  right_half = merge_sort(arr[mid:])

  return merge(left_half, right_half)

def merge(left, right):
  sorted_array = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      sorted_array.append(left[i])
      i += 1
    else:
      sorted_array.append(right[k])
      j += 1

  sorted_array.extend(left[i:])
  sorted_array.extend(right[j:])
