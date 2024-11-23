nums = [5,6,2,1,3,4]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True
    return ls
# nums_bubble = bubble_sort(nums)
# print(nums_bubble)

def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        print(ls)
        ls[i], ls[lowest] = ls[lowest], ls[i]

# print(nums)
nums_select = selection_sort(nums)
print(nums_select)