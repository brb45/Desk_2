class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1

s = Subclass()
s.call_me()
# Calling method on Base Class
# Calling method on Right Subclass
# Calling method on Left Subclass
# Calling method on Subclass


# Looks good; our base method is only being called once.
#
# But what is super() actually doing here? Since the print
# statements are executed after the super calls, the printed output is in the order each method is actually executed.
# Let's look at the output from back to front to see who is calling what.
#
# First, call_me of Subclass calls super().call_me(), which happens to refer
# to LeftSubclass.call_me(). The LeftSubclass.call_me() method then calls super().call_me(),
# but in this case, super() is referring to RightSubclass.call_me().
#
# Pay particular attention to this: the super call is not calling the method on the superclass of
# LeftSubclass (which is BaseClass). Rather, it is calling RightSubclass, even though it is not a
# direct parent of LeftSubclass! This is the next method, not the parent method. RightSubclass then
# calls BaseClass and the super calls have ensured each method in the class hierarchy is executed once.



print(s.num_sub_calls, s.num_left_calls, s.num_right_calls,
s.num_base_calls)


# 1 1 1 1
# Calling method on Base Class
# Calling method on Left Subclass
# Calling method on Base Class
# Calling method on Right Subclass
# Calling method on Subclass

# isinstance() function #
# The isinstance() function is used to determine whether the object is an instance of the class or not.
#
# Syntax: isinstance(object, class_type)

# >>> isinstance(1, int)
# True
#
# >>> isinstance(1.2, int)
# False
#
# >>> isinstance([1,2,3,4], list)
# True
# Next chapter Exception Handling.
