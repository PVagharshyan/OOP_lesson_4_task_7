from tape import Tape
from book import Book
from publication import Publication

def main() -> None:
    print("!main!")
    tape = Tape()

    print("get book data: ")
    print(tape.getdata())

if __name__ == "__main__":
    main()
