
class Club:
    def __init__(self, name, mascot_name, mascot_species, show_name):
        self.name = name
        self.members = []
        all_members = []

    def add_member(self, member_name):
        self.members.append(member_name)

    def all_members(self):
        for member in self.members:
            print(member)

    def mascot(self, mascot_name, mascot_species):
        self.mascot = Mascot(mascot_name, mascot_species)

    def club_show(self, show_name):
        self.club_show = MakinMusicShow(show_name)

class Member:
    def __init__(self, name):
        self.name = name
        self.paid_dues = False
        if self.paid_dues == True:
            print(f"{self.name} has paid dues.")
        else:
            print(f"{self.name} has not paid dues.")

class Mascot:
    def __init__(self, name, species):
        self.name = 'unknown'
        self.species = 'unknown'
    
    def mascot(self, name, species):
        self.name = name
        self.species = species
    
class MakinMusicShow:
    def __init__(self, name, theme):
        self.name = name
        self.theme = 'Unknown'
        self.songs_list = []
    
    def theme(self, theme):
        self.theme = theme

    def perform(self):
        for song in self.songs_list:
            print(f"Cool Choreography to {song}")   
