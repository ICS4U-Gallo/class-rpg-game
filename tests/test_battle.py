from main import Battle
from character import Character


def test_battle_class():
        
    player = []
    for _ in range(3):
        c = Character()
        player.append(c)


    enemy = []
    for _ in range(4):
        c = Character()
        enemy.append(c)

    battle = Battle(player, enemy)

    assert battle._player_party == player
    assert battle._enemy_party == enemy

    assert len(battle._turn_order) == len(player + enemy)
    
    for char in player + enemy:
        assert char in battle._turn_order
    

def test_get_current_character():
    mr_gallo = Character()
    battle = Battle([mr_gallo], [])

    assert battle.get_current_character() == mr_gallo
    battle._turn += 1
    assert battle.get_current_character() == mr_gallo


def test_get_current_character_more_than_one():
    mr_gallo = Character()
    mr_paravanni = Character()
    battle = Battle([], [])
    battle._turn_order = [mr_gallo, mr_paravanni]

    assert battle.get_current_character() == mr_gallo
    battle._turn += 1
    assert battle.get_current_character() == mr_paravanni
    battle._turn += 1
    assert battle.get_current_character() == mr_gallo
    



# battle.handle_attack(weapon, enemy)
