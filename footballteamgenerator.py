class Player:
    def __init__(self, name: str, endurance: int, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    # Getters
    def get_name(self):
        return self.__name

    def get_endurance(self):
        return self.__endurance

    def get_sprint(self):
        return self.__sprint

    def get_dribble(self):
        return self.__dribble

    def get_passing(self):
        return self.__passing

    def get_shooting(self):
        return self.__shooting

    # Setters
    def set_name(self, name: str):
        self.__name = name

    def set_endurance(self, endurance: int):
        self.__endurance = endurance

    def set_sprint(self, sprint: int):
        self.__sprint = sprint

    def set_dribble(self, dribble: int):
        self.__dribble = dribble

    def set_passing(self, passing: int):
        self.__passing = passing

    def set_shooting(self, shooting: int):
        self.__shooting = shooting

    def __str__(self):
        return (f"Player: {self.__name}\n"
                f"Endurance: {self.__endurance}\n"
                f"Sprint: {self.__sprint}\n"
                f"Dribble: {self.__dribble}\n"
                f"Passing: {self.__passing}\n"
                f"Shooting: {self.__shooting}\n")
                
                
class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    # Getters
    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating

    def get_players(self):
        return self.__players

    # Setters
    def set_name(self, name: str):
        self.__name = name

    def set_rating(self, rating: int):
        self.__rating = rating

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.get_name()} has already joined"
        self.__players.append(player)
        return f"Player {player.get_name()} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.get_name() == player_name:
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"