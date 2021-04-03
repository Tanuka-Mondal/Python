def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == '4':
      count = count + 1

  return count



value = input("Enter some comma separated values: ")
MyList = value.split(",")



data = list_count_4(MyList)

print(MyList)
print(data)