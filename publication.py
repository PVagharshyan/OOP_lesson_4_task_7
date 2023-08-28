def check_date(data: str) -> bool:
    data = data.split('.')
    if len(data) != 3:
        return False
    for i in data:
        if not i.isdigit():
            return False
    return (
        1 <= int(data[0]) <= 31 and
        1 <= int(data[1]) <= 12
    )

class Publication:
    def __init__(self) -> None:
        self.putdata()

    def getdata(self) -> dict:
        result_dict = { "title" : self._title, "price" : self._price }
        return result_dict

    def putdata(self) -> None:
        v_title = input("input title: ")
        self._title = v_title
        while True:
            try:
                v_price = input("input price: ")
                v_price = float(v_price)
                break
            except ValueError as err:
                print(err)
        self._price = v_price

class Publication2(Publication):
    def __init__(self) -> None:
        self.putdata()
    def getdata(self) -> dict:
        result_dict = {
            "publication_data" : self._publication_data
        }
        result_dict = { **result_dict, **super().getdata() }
        return result_dict

    def putdata(self) -> None:
        super().putdata()
        v_publication_data = ''
        while not check_date(v_publication_data):
            v_publication_data = input("publication data: ")
        self._publication_data = v_publication_data



