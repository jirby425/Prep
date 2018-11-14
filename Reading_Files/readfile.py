import sys








if __name__ == "__main__":
    file = sys.argv[1]
    print file
    f=open(file, "r")
    for line in f:
        for word in line.split():
            print word

    f.close()
