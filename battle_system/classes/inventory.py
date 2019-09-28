class Item:
    def __init__(self, name, type, description, prop, reach):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        self.reach = reach


class HealingItem(Item):
    pass


class AttackItem(Item):
    pass
