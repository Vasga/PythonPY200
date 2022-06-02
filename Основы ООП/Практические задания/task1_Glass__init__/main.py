from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume,(int, float)):
            raise TypeError
        if not capacity_volume > 0: #  TODO инициализировать объект "Стакан"
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass1 = Glass(200, 150)
    glass2 = Glass(500, 250)

    # TODO попробовать инициализировать не корректные объекты
