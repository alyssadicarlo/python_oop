class Person:
  
  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    self.friends = []
    self.greeting_count = 0
    self.unique_greeted = []
    
  def __str__(self):
    return '{} {} {}'.format(self.name, self.email, self.phone)

  def greet(self, other_person):
    self.greeting_count += 1
    if other_person not in self.unique_greeted:
      self.unique_greeted.append(other_person)
    print('Hello %s, I am %s!' % (other_person.name, self.name))
    
  def num_unique_people_greeted(self):
    return len(self.unique_greeted)
    
  def print_contact_info(self):
    print("{}'s email: {}".format(self.name, self.email))
    print("{}'s phone number: {}".format(self.name, self.phone))
    
  def add_friend(self, other_person):
    self.friends.append(other_person)
    
  def num_friends(self):
    return len(self.friends)
      

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
