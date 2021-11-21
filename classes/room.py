class Room:
    def __init__(self, name, guest_limit,):
        self.name = name
        self.guest_limit = guest_limit
        self.guest_list = []
        self.song_list = []
        self.entry_fee = 5
        

    def amount_of_guests(self):
        return len(self.guest_list)
    
    def check_in_guest(self, guest):
        self.guest_list.append(guest)

    def check_out_guest(self, guest):
        self.guest_list.remove(guest)
    
    def amount_of_songs(self):
        return len(self.song_list)

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        self.song_list.remove(song)
    
    def is_there_room_available(self):
        if self.amount_of_guests() < self.guest_limit:
            return True
        else:
            return False

    # ...............

    def guest_pays_entry_fee(self, guest):
        if guest.wallet >= self.entry_fee:
            return True
        else:
            return False

    def play_my_favourite_song(self, guest):
        for song in self.song_list:
            if guest.favourite_song == song.name:
                return "Whoo!"
            else:
                return "That's not my jam!"

    # ...............

   

    
            