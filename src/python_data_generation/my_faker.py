
import random
import time

class Hobby:
    def __init__(self, name=None):
        self.name = name
        self.hobbies_types = ["Reading", "Writing", "Drawing", "Painting", "Photography", "Hiking", "Cycling", "Swimming", "Running", "Gaming", "Traveling", "Fishing", "Gardening", "Cooking", "Baking", "Knitting", "Camping", "Birdwatching", "Puzzles", "Dancing", "Yoga", "Meditation", "Playing Guitar", "Playing Piano", "Singing", "Scrapbooking", "Pottery", "Jewelry Making", "Skiing", "Snowboarding", "Surfing", "Skateboarding", "Sailing", "Scuba Diving", "Rock Climbing", "Archery", "Tennis", "Golf", "Basketball", "Baseball", "Soccer", "Football", "Rugby", "Volleyball", "Martial Arts", "Boxing", "Fencing", "Table Tennis", "Billiards", "Bowling", "Roller Skating", "Ice Skating", "Kite Flying", "Stargazing", "Astronomy", "Magic Tricks", "Cosplaying", "Beekeeping", "Wine Tasting", "Craft Beer Brewing", "Mixology", "Candle Making", "Soap Making", "Calligraphy", "Origami", "Chess", "Drone Flying", "Blogging", "Podcasting", "Vlogging", "Horseback Riding", "Canoeing", "Kayaking", "Wind Surfing", "Paragliding", "Skydiving", "Bungee Jumping", "Model Building", "Homebrewing", "Quilting", "Whittling", "Macrame", "Embroidery", "Crocheting", "Stamp Collecting", "Coin Collecting", "Metal Detecting", "Rafting", "Sudoku", "Crosswords", "Geocaching", "Urban Exploration", "Aquarium Keeping", "Tarot Reading", "Beatboxing", "Radio Control Cars", "Parkour", "Board Games", "Digital Art", "Video Editing", "Graphic Design"]
    
    def get_rand(self):
        return random.choice(self.hobbies_types)
    

class Friendship:
    def __init__(self, name=None):
        self.name = name
        self.friendship_types = ["College Roommate Friends", "Childhood Playmates", "Work Colleagues Connection", "Sports Teammates Bond", "Neighborly Acquaintances", "Family Friends Since Birth", "Online Gaming Partners", "Book Club Companions", "Vacation Friends Met Abroad", "Mutual Hobby Enthusiasts", "Parent-Friends Through Kids", "High School Best Friends", "University Study Buddies", "Long Distance Pen Pals", "Ex-Partners Turned Friends", "Pet-Owner Friends Connection", "Fellow Musicians and Singers", "Travel Buddies From Trip", "Church Community Friends", "Local Social Club Members", "Military Service Friends", "Coworker Lunch Buddies", "Spouse's Friend Connection", "Therapy Group Comrades", "Yoga Class Companions", "Friends Through Siblings", "Old Friends Reconnected", "College Course Classmates", "Volunteering Companions", "Mentor-Mentee Relationship"]
    
    def get_rand(self):
        return random.choice(self.friendship_types)
    

class Access:
    def __init__(self, name=None):
        self.name = name
        self.access_types = ["Viewed Profile Only", "Left a Quick Note", "Added a Friendship", "Liked a Status Update", "Commented on Photo", "Checked Into Location", "Shared a Post to Timeline", "Uploaded New Profile Pic", "Joined a Public Group", "Participated in Poll", "Watched a Shared Video", "Responded to Event Invite", "Sent Direct Message", "Tagged in a Comment", "Started a Fundraiser", "Viewed Stories Archive", "Clicked on Marketplace Ad", "Muted Stories Temporarily", "Reacted to a Post", "Unfriended a Contact", "Reported an Issue", "Edited Profile Information", "Saved a Post for Later", "Requested Account Verification", "Listened to Shared Music", "Changed Privacy Settings", "Set Up Two-Factor Auth", "Subscribed to Notifications", "Completed a Quiz", "Unfollowed a Page"]
    
    def get_rand(self):
        return random.choice(self.access_types)

# class MyTime:
#     def __init__(self):
#         self.current_time = int(time.time()) # current epoch time in seconds

#     def get_rand(self):
#         num_secs_in_year = 31536000
#         return random.randint(self.current_time - num_secs_in_year, self.current_time - num_secs_in_year)

# # Test random generation

# h = print(Hobby().get_rand())
# f = print(Friendship().get_rand())
# a = print(Access().get_rand())

# mytime = MyTime().get_rand()

# from datetime import datetime
# dt_object = datetime.utcfromtimestamp(mytime)

# print(dt_object)