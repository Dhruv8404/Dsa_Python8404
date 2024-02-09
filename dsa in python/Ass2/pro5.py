class Team:

    def __init__(self,name=None):
        self.name=name
  
    def show(self):
       print("Name::",self.name)
      
team_data = []
members = int(input("Enter the number of team members:"))

for i in range(members):
    i = input("Enter team member name: ")
    team_data.append(Team(i))

print("Team Member Names:")
for j in team_data:
    j.show()