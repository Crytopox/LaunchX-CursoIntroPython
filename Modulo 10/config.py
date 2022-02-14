def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

def main2():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as error:
        print("Couldn't find the config.txt file!", error)
    except IsADirectoryError as error:
        print("Found config.txt but it is a directory, couldn't read it", error)
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

def main3():
    try:
        configuration = open('config.txt')
    except OSError as error:
        if error.errno == 2:
            print("Couldn't find the config.txt file!")
        elif error.errno == 13:
            print("Found config.txt but couldn't read it")

if __name__ == '__main__':
    print("First try catch")
    main()
    print("Second try catch")
    main2()
    print("Third try catch")
    main3()