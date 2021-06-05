import hashlib  
strs = '35eb09'
def md5(s):
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()

def main():
    for i in range(10000000,100000000):
        a = md5(i)
        if a[0:6] == strs:
            print(i)
            exit(0)  
if __name__ == '__main__':
    main()
