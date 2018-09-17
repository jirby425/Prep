


def listExample():
    l = []
    for i in range (0,10):
        l.append(i)
    for i in l:
        print l[i],

def dictExample():
    d = {"this":1, "is": 2, "a":3, "test":4}
    print d
    print d["this"]

    for key in d.keys():
        print key + ": " + str(d[key])


if __name__ == "__main__":
    print "Hello world"
    listExample()
    dictExample()
    #test commit
