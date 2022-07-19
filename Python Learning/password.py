for i in range(3):
    p = int(0)
    q = int(0)
    r = int(0)
    s = int(0)
    pws = input("enter password")

    if len(pws) >0 and len(pws) <=8:

        for j in range(0,len(pws)):

            if ord(pws[j]) >= 48 and 