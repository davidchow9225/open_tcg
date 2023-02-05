"""This script exists to serve as an example of what you can do with 'trading_card_api'.
"""
import open_tcg as tcg_api

def yu_gi_oh_example():
    """Creates an example of the API's usage via the in-built 'Yu-Gi-Oh!' types.
    """
    #? This string exists to be appended to via the internal functions.
    def create_object_instances():
        """Creates instances of the three types of 'Yu-Gi-Oh!' cards.
        """
        #* Lowercase keyworded arguments are used to allow for maximum control over constructor inputs.
        MONSTER = tcg_api.yu_gi_oh.MonsterCard(name="Blue-Eyes White Dragon",
            type="Dragon",
            level=8,
            attack=3000,
            defense=2500)
        SPELL = tcg_api.yu_gi_oh.SpellCard(name="Pot Of Greed",
            type="Normal",
            effect="Draw 2 cards.")
        TRAP = tcg_api.yu_gi_oh.TrapCard(name='Magic Cylinder',
            type="Normal",
            effect="When an opponent's monster declares an attack: Target the attacking monster; negate the attack, and if you do, inflict damage to your opponent equal to its ATK.")
        #* This syntax will pack these three variables into a Tuple before returning it to the caller.
        return MONSTER, SPELL, TRAP 

    def appended_object_info(*objects: tcg_api.Card):
        """Returns a string containing the text-representations of the object isntances, unless they are not 'Yu-Gi-Oh!' cards.
        """
        #* Input Sanitation Practices.
        MONSTER = objects[0] if isinstance(objects[0], tcg_api.yu_gi_oh.MonsterCard) else TypeError('%s is not an instance of %s.' % (objects[0], tcg_api.yu_gi_oh.MonsterCard))
        SPELL = objects[1] if isinstance(objects[0], tcg_api.yu_gi_oh.SpellCard) else TypeError('%s is not an instance of %s.' % (objects[1], tcg_api.yu_gi_oh.SpellCard))
        TRAP = objects[2] if isinstance(objects[0], tcg_api.yu_gi_oh.TrapCard) else TypeError('%s is not an instance of %s.' % (objects[2], tcg_api.yu_gi_oh.TrapCard))
        #? The string representations of these classes are joined for clean printing with Newline Characters(\n) as delimeters.
        return '\n'.join((MONSTER.__str__(), SPELL.__str__(), TRAP.__str__()))

    #? The card object instances are unpacked from the Tuple via an asterisk(*) and piped into the above inner function as arguments.
    return appended_object_info(*create_object_instances())


#* Encapsulates the main logic of this module.
def main():
    """The logic that is ran when this script is ran/called directly.
    """
    print(yu_gi_oh_example())


#? Allows for control over the execution and importing of this module.
if __name__ == '__main__':
    main()
else:
    print(f'{__name__} has been successfully imported.')