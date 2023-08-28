from publication import Publication2

class Book(Publication2):
    def __init__(self) -> None:
        self.putdata()

    def getdata(self) -> dict:
        result_dict = {
            "page_count" : self._page_count
        }
        result_dict = { **result_dict, **super().getdata() }
        return result_dict

    def putdata(self) -> None:
        super().putdata()
        while True:
            try:
                v_page_cout = input("input page count: ")
                v_page_cout = int(v_page_cout)
                break
            except ValueError as err:
                print(err)
        self._page_count = v_page_cout

def main() -> None:
    print("!Book!")
    b = Book()
if __name__ == "__main__":
    main()
