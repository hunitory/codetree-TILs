class member:
    def __init__(self, member_id = "codetree", member_level=10):
        self.member_id = member_id
        self.member_level = member_level
    
    def print_member(self):
        print(f'user {self.member_id} lv {self.member_level}')

person = member()
person.print_member()
member1 = input().split()

person = member(member1[0], int(member1[1]))
person.print_member()