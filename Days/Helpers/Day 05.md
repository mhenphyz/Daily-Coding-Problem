I had some difficulty to understand how you can pass a method as a parameter to a function in python. 

The follow link helped a lot

[How do I pass a method as a parameter in Python](https://stackoverflow.com/questions/706721/how-do-i-pass-a-method-as-a-parameter-in-python)

When you have a method as a parameter the object have a special attribute named __call__() witch is define on documentations as bellow:

Class Instances

    Instances of arbitrary classes can be made callable by defining a __call__() method in their class.
