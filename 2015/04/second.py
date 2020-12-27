import hashlib

key = "iwrupvqb"
i = 1
while True:
    h = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()
    if h[:6] == "000000":
        print(i)
        exit(0)
    i += 1
