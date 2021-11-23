import floor_button


class Floor:
    # This are all the floors in the building
    FLOORS = (0, 1, 2, 3, 4, 5)

    def __init__(self):
        self.lift_button = floor_button.FloorButton()
