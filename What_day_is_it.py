days = [" ", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday", "Monday"]

# to convert UTC to mins
def ConvUtc(utc):
    if ":" in utc:
        conv_ = utc.split(":")
        conv_ = list(map(int,conv_))
        conv_ = conv_[0] * 60 + conv_[1]
        return conv_
    else:
        return int(utc) * 60

def Comp(conv_mins, nconv_mins):
    comp_ = conv_mins + nconv_mins
    if comp_ > 1440:
        print(days[today + 1])
    elif comp_ < 0:
        print(days[today - 1])
    else:
        print(days[today])

# set todays date
today = int(input("Pick current Day(in London): \n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thrusday\n5. Friday\n6. Saturday\n7. Sunday\n"))

# get Greenwich input
utc = input("London/Greenwich Time: ")
conv_mins = ConvUtc(utc)

# UTC of where user lives
nutc = input()
nconv_mins = ConvUtc(nutc)

Comp(conv_mins, nconv_mins)