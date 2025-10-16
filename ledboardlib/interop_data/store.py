import os

from ledboardlib.interop_data.dataclass import InteropData


class InteropDataStore:
    def __init__(self, filepath: str):
        self._filepath = filepath
        self.data: InteropData | None = None
        self.load()

    def load(self) -> InteropData:
        if os.path.exists(self._filepath):
            with open(self._filepath, "r") as file:
                self.data = InteropData.from_json(file.read())
                print(f"Loaded interop data from {self._filepath}")
        else:
            self.data = InteropData()

        return self.data

    def save(self):
        with open(self._filepath, "w+") as file:
            file.write(self.data.to_json(indent=2))
            print(f"Saved interop data to {self._filepath}")
