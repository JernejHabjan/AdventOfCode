# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()
all = 0
for line in lines:

    l,w,h = line.split("x")
    l,w,h = int(l), int(w), int(h)
    one =  l * w
    two =  w * h
    three =  h * l

    #print(l,w,h)
    #print(one, two ,three)

    a,b,c = 2*(h+l), 2* (l+w), 2*(h+w)

    obseg = min(a,b,c)
    bow = w*h*l
    print(obseg)
    all += obseg + bow

    # all+= one+two + three + min(one, two, three)/2

print(all)