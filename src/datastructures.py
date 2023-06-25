
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Tenemos que coger el objeto que nos pasa y complementar la información.
        # El ID va a ser generado por el  _generateId()
        # El last_name siempre tiene que ser el self.last_name

        new_member = {
            "id": self._generateId(),
            "first_name": member['first_name'],
            "last_name": self.last_name,
            "age": member['age'],
            "lucky_numbers": member['lucky_numbers']
        }

        self._members.append(new_member)

    def delete_member(self, id):
       for m in self._members:
           if m['id'] == id:
               return self._members.remove(m)

    def get_member(self, id):
        for m in self._members:
            if m['id'] == id:
                return m

    # this method is done, it returns a list with all the family members

    def get_all_members(self):
        return self._members
