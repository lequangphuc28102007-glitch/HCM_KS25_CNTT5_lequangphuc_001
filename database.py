from models import Player

class PlayerManager:
    def __init__(self):
        self.players = []

    def find_by_id(self, id):
        for player in self.players:
            if player.id == id:
                return player
            
        return None
    
    def add_player(self, player):
        if self.find_by_id() is None:
            self.players.append(player)
            return True
        return False


    def update_player(self, id):
        new_player_id = self.find_by_id(new_player_id)
        if new_player_id:
            print("")
        


    def delete_player(self, id):
        player_id = self.find_by_id(id)

        if player_id:
            self.players.remove(player_id)
            

    def search_player(self, keyword):
        result = []
        for player in self.players:
            if keyword.strip() == player.name:
                result.append(player)
                return result
            
    