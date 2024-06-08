import time
def countdown(t):
    while t:
        mints , seconds = divmod(t, 60)
        timer ="{:02d}:{:02d}".format(mints, seconds)
        print(timer, "\r")
        time.sleep(1)
        t -= 1
    print("Fire in the hole")
t = input("Enter the time in seconds: ")
countdown(int(t))