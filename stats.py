
#function to calculate mode of a list of numbers
def mode(numbers):
  if len(numbers) == 0:
    return 0
  freq = {}             #creating a dictionary to store frequency of numbers
  mode = numbers[0]
  for num in numbers:
    number = freq.get(num, None)
    if number == None:  #number occured first time
        freq[num] = 1
    else:               #number has already occured
        freq[num] = number + 1
        if freq[num] > mode:
          mode = num
  return mode

#function to calculate mean of a list of numbers
def mean(numbers):
  if len(numbers) == 0:
    return 0
  sum = 0
  for num in numbers:
    sum += num
  return sum / len(numbers)
  

#function to calculate median of a list of numbers
def median(numbers):
  if len(numbers) == 0:
    return 0
  numbers.sort()
  midpoint = len(numbers) // 2
  if len(numbers) % 2 == 1:
      return numbers[midpoint]
  return (numbers[midpoint] + numbers[midpoint - 1]) / 2

fileName = input("Enter the file name: ")
f = open(fileName, 'r')
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

print("List of Numbers: ", numbers)
print("The Median is: ", median(numbers))   
print("The Mode is: ", mode(numbers))     
print("The Mean is: ", mean(numbers))      