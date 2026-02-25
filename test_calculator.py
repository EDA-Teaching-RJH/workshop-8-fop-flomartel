from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    else:
        print("2 squared was 4, that's great")

    if square(3) != 9:
        print("3 squared was not 9")
if __name__ == "__main__":
    main()