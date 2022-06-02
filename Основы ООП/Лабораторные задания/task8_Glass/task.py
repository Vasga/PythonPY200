from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.occupied_volume = None
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.init_occupied_volume(occupied_volume)
        self.add_water(occupied_volume)
        self.remove_water(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, water: int) -> None:
        if not isinstance(water, int):
            raise TypeError

        if water < 0:
            raise ValueError

        space = self.capacity_volume - self.occupied_volume
        if water > space:
            raise ValueError("")


    def remove_water(self, estimate_water: int) -> None:
        if not isinstance(estimate_water, int):
            raise TypeError
        a = self.occupied_volume
        if estimate_water > a:
            raise ValueError


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.occupied_volume -= 150

    print(glass.capacity_volume, glass.occupied_volume)
