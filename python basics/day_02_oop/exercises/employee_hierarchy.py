"""
WAP for the training organization, which has the following relationship:
Classes: ‘Employee’, ‘Developer’ (child class of Employee), ‘Trainer’ (child class of
Employee), ‘TechMentor’ (child of Developer and Trainer).
Employee contains a common method work().
Both Developer and Trainer provide their own version of work().
TechMentor inherits from both Developer and Trainer.
Each implementation should use the inheritance chain appropriately so that
Python can determine the order in which methods are executed. []
Task:
1. Implement the complete hierarchy.
2. Create a TechMentor object.
3. Call work().
4. Print the MRO of TechMentor.
5. Explain why Python does not simply execute the methods based on the visual
left-to-right structure of the diagram.
"""

class Employee:
    def work(self):
        print("Employee is working.")

class Developer(Employee):
    def work(self):
        print("Developer is coding.")
        super().work()  # Call the parent class's work() method

class Trainer(Employee):
    def work(self):
        print("Trainer is training.")
        super().work()  # Call the parent class's work() method

class TechMentor(Developer, Trainer):
    def work(self):
        print("TechMentor is mentoring.")
        super().work()  # Call the parent class's work() method

# Create a TechMentor object
tech_mentor = TechMentor()
# Call work()
tech_mentor.work()
# Print the MRO of TechMentor
print("Method Resolution Order (MRO):", TechMentor.__mro__)
