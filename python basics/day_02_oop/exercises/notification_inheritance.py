"""
WAP to consider a base class Notification with a method send(). Create a derived class EmailNotification that provides its own send() implementation. Inside the child class, demonstrate two different ways of invoking send():
● Calling the method through the current object.
● Calling the parent implementation through the inheritance relationship.
[self.send() vs super().send()]
Must follow:
1. Implement both approaches.
2. Observe and explain the difference in their behavior.
3. Be careful to identify what happens if the child method calls itself indirectly through the object again.
"""

class Notification:
    def send(self):
        print("Sending notification...")

class EmailNotification(Notification):
    def send(self):
        print("Sending email notification...")
        # Calling the method through the current object
        #self.send()  # This will cause infinite recursion and eventually a RecursionError
        # Calling the parent implementation through the inheritance relationship
        super().send()  # This will call the parent class's send() method
