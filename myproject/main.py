import sys

def main(argv): #argvでコマンドライン引数受け取り
    print('exec main')
    print(sys.argv) 
    
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))