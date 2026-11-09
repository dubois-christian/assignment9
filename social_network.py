"""An undirected social network represented with adjacency lists."""


class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend is not self and friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"Person not added. {name} already exists!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        missing = []
        for name in (person1_name, person2_name):
            if name not in self.people and name not in missing:
                missing.append(name)
        if missing:
            for name in missing:
                print(f"Friendship not created. {name} doesn't exist!")
            return
        if person1_name == person2_name:
            print("Friendship not created. A person cannot be their own friend!")
            return
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friends = ", ".join(friend.name for friend in person.friends)
            print(f"{person.name} is friends with: {friends or '(no friends yet)'}")


def main():
    network = SocialNetwork()
    for name in ("Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"):
        network.add_person(name)

    for first, second in (
        ("Alex", "Jordan"),
        ("Alex", "Morgan"),
        ("Jordan", "Taylor"),
        ("Morgan", "Casey"),
        ("Taylor", "Riley"),
        ("Casey", "Riley"),
        ("Morgan", "Riley"),
        ("Alex", "Taylor"),
    ):
        network.add_friendship(first, second)

    network.add_friendship("Jordan", "Johnny")
    network.add_person("Alex")
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Alex")
    print()
    network.print_network()


if __name__ == "__main__":
    main()
