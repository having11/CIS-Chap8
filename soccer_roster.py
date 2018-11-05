class Team_roster():
    def __init__(self):
        self.players = {}
        self.menu_options = {"a":"Add player","d":"Remove player","u":"Update player rating", \
        "r":"Output players above a rating","o":"Output roster","q":"Quit"}
    def add_player(self):
        jersey_num = input("Enter a new player's jersey number:\n")
        self.players[jersey_num] = int(input("Enter a new rating for player:\n"))
    def remove_player(self):
        number_to_del = input("Enter a jersey number:\n")
        del self.players[number_to_del]
    def populate_roster(self, player_num):
        for i in range(player_num):
            jersey_num = (input("Enter player "+str(i+1)+"'s jersey number:\n"))
            self.players[jersey_num] = int(input("Enter player "+str(i+1)+"'s rating:\n"))
            print()
    def update_player(self):
        jersey_num = input("Enter a jersey number:\n")
        self.players[jersey_num] = int(input("Enter a new rating for player:\n"))
    
    def out_above_rating(self):
        rating = int(input("Enter a rating:\n"))
        print("\nABOVE",rating)
        for key in self.players:
            score = self.players[key]
            if score > rating:
                print("Jersey number: %s, Rating: %i"%(key,score))
        
    def output_roster(self):
        print("\nROSTER")
        for player in self.players:
            print("Jersey number: %s, Rating: %i"%(player,self.players[player]))
            
    def eval_option(self,choice):
        choice = choice.lower()
        if choice=="a":
            self.add_player()
        elif choice=="o":
            self.output_roster()
        elif choice=="d":
            self.remove_player()
        elif choice=="u":
            self.update_player()
        elif choice=="r":
            self.out_above_rating()
    
    def output_menu(self):
        print("\nMENU")
        for option in self.menu_options:
            print("%s - %s"%(option,self.menu_options[option]))
        choice = input("\nChoose an option:\n")
        while choice != 'q':
            self.eval_option(choice)
            print("\nMENU")
            for option in self.menu_options:
                print("%s - %s"%(option,self.menu_options[option]))
            choice = input("\nChoose an option:\n")
        

roster = Team_roster()
roster.populate_roster(5)
roster.output_roster()
roster.output_menu()

