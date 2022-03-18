class Territory:

    def __init__(self, position, name, r) -> None:
        self.position = position
        self.name = name
        self.connected_terrotories = []
        self.r = r