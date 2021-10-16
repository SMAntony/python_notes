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
