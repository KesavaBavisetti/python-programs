#Default Parameters:
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()           # Output: Hello, Guest!
greet_user("Alice")     # Output: Hello, Alice!


#Calling Functions Inside Functions:
def greet(name):
    return f"Hello, {name}!"

def greet_and_emphasize(name):
    greeting = greet(name)
    return greeting.upper() + "!!!"

result = greet_and_emphasize("Alice")
print(result)  # Output: HELLO, ALICE!!!


#Scope of Variables:
#Global ga declare chesina variables ni program lo nuv ekkadpadte akkad vaadkovach mowa! Ade nuv oka variable ni function lopata declare chesthe nuv daani aa particular function lo maatrame vaadkogalav.
global_variable = "I'm global"

def function_with_local_variable():
    local_variable = "I'm local"
    print(global_variable)     # Output: I'm global
    print(local_variable)      # Output: I'm local

function_with_local_variable()
print(global_variable)         # Output: I'm global
# print(local_variable)       # Raises NameError: name 'local_variable' is not defined