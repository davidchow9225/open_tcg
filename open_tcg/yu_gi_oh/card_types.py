from trading_card_api.objects.card import BaseCardClass

class MonsterCard(BaseCardClass):
    def __init__(self, **kwargs):
        # Internal Variable Declarations
        #* Super-Class Variables
        _name = kwargs.get('name')
        _image_path = kwargs.get('image', None)
        #* Sub-Class Variables
        _monster_type = kwargs.get('type', None)
        _monster_level = kwargs.get('level', 0)
        _attack = kwargs.get('attack', 0)
        _defense = kwargs.get('defense', 0)
        _effect_text = kwargs.get('effect', None)
        #? Guard Clauses
        if _monster_level < 0:
            ValueError('Cannot have negative levels.')
        # Logic
        super().__init__(_name, _image_path)
        self.type = _monster_type
        self.level = _monster_level
        self.attack = _attack
        self.defense = _defense
        self.effect = _effect_text
    def __str__(self):
        return f"MonsterCard({self.name}, {self.image}, {self.type}, {self.level}, {self.attack}, {self.defense}, {self.effect})"
    

class SpellCard(BaseCardClass):
    def __init__(self, **kwargs):
        # Internal Variable Declarations
        #* Super-Class Variables
        _name = kwargs.get('name')
        _image_path = kwargs.get('image', None)
        #* Sub-Class Variables
        _spell_type = kwargs.get('type', 'Normal')
        _effect_text = kwargs.get('effect', None)
        # Logic
        super().__init__(_name, _image_path)
        self.type = _spell_type
        self.effect = _effect_text
    def __str__(self):
        return f"SpellCard({self.name}, {self.image}, {self.type}, {self.effect})"

class TrapCard(BaseCardClass):
    def __init__(self, **kwargs):
        # Internal Variable Declarations
        #* Super-Class Variables
        _name = kwargs.get('name')
        _image_path = kwargs.get('image', None)
        #* Sub-Class Variables
        _trap_type = kwargs.get('type', 'Normal')
        _effect_text = kwargs.get('effect', None)
        # Logic
        super().__init__(_name, _image_path)
        self.type = _trap_type
        self.effect = _effect_text
    def __str__(self):
        return f"TrapCard({self.name}, {self.image}, {self.type}, {self.effect})"
