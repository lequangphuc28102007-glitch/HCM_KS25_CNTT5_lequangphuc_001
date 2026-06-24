from models import Player
from database import PlayerManager

def show_all(list_player: Player):

    print("-" * 125)
    print(f"{Mã:<20} | {Tên:<20} | {tocdo:<20} | {kythuat:<20} | {goal:<20} | {phongdo:<20} | {phânloại:<20}")
    print("-" * 125)
    for player in list_player:
        print(f"{player.id:<20} | {player.name:<20} | {player.speed_score} | {player.technique_score} | {player.goal_socre} | {player.average_score} | {player.performance_type} ")
    print("-" * 125)


