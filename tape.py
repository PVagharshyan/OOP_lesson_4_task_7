from publication import Publication2

class Tape(Publication2):
    def __init__(self) -> None:
        self.putdata()

    def getdata(self) -> dict:
        result_dict = {
            "playing_time" : self._playing_time
        }
        result_dict = { **result_dict, **super().getdata() }
        return result_dict

    def putdata(self) -> None:
        super().putdata()
        while True:
            try:
                v_playing_time = input("input playing time: ")
                v_playing_time = float(v_playing_time)
                break
            except ValueError as err:
                print(err)
        self._playing_time = v_playing_time
