#classes and instances
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if self.age < 0:
            print('Age is not valid, setting age to 0.')
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print('You are young.')
        elif 13 <= self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

#Dictonaries and maps    
def findDirectory(name, key_values):
    if name in key_values:
        print(name,"=",key_values.get(name),sep = "") 
    else:
        print("Not found")

if __name__ == "__main__":
    n = int(input())
    keys_values = dict([map(str, input().strip().split()) for _ in range(n)])
    while True:
        try:
            name = input()
            findDirectory(name,keys_values)
        except (EOFError):
            break

#2D arrays
def SumOfDiag(mat3):
    n = len(mat3)
    sum_ = 0
    for i in range(n):
        sum_ += sum(mat3[i])
    sum_ = sum_ - (mat3[1][0]) - (mat3[1][2])
    return sum_
    
def FindMax(arr):
    s = {}
    count = 0
    for x in range (0,4):
        for y in range (0,4):
            temp_matrix= arr[x][y:y+3],arr[x+1][y:y+3],arr[x+2][y:y+3]
            sum_ = SumOfDiag(temp_matrix)
            s[count] = sum_
            count += 1
    return(s)
    
if __name__ == '__main__':

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    data = FindMax(arr)
    data = list(data.values())
    print(max(data))

#valid email filter code
    def fun(email):
    try:
        username, url = email.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False

    if username.replace('-', '').replace('_', '').isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

#some input asking codes
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

#reading unknown number of inputs
1.throw an exception:
    
while True:
  try:
    value = raw_input()
    do_stuff(value) # next line was found 
  except (EOFError):
    break #end of file reached

2.check input content:

while True:
  value = raw_input()
  if (value != ""):
    do_stuff(value) # next line was found 
  else:
    break 

3. use sys.stdin.readlines() to convert them into a list, and then use a for-each loop. More detailed explanation is Why does standard input() cause an EOF error

import sys 

# Read input and assemble Phone Book
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

# Process Queries
lines = sys.stdin.readlines()  # convert lines to list
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')
        
#to get matrix of n rows n cols as input and turning it into 2D array     
 arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
