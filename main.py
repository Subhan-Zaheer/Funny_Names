
import random

class Name:
    first_name = ""
    last_name = ""
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
    def __repr__(self):
        return (f"{self.first_name} {self.last_name}")


def funny_name(friends):
    # rand = random.randint(0, len(friends)-1)
    for i in range(len(friends) - 1):
        rand = random.choice([x for x in range(len(friends)) if x!=i ])
        temp = friends[i].last_name
        friends[i].last_name = friends[rand].last_name
        friends[rand].last_name = temp
    return friends


if __name__ == '__main__':

    num_of_Friends = int(input("Enter the number of your friends : "))
    friends = []
    print(f"Enter your {num_of_Friends} Friend's name.\n")
    for i in range(num_of_Friends):
        name = input(f"Enter your {i} friend's name with space between first name and last name : ")
        ls = name.split(" ")
        f_name = ls[0]
        l_name = ls[1]
        print(f"\n{i+1} friend's name is : {f_name} {l_name}")
        name = Name(f_name, l_name)
        friends.append(name)
    funny_Names_list = funny_name(friends)
    print(funny_Names_list)