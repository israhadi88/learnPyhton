#Build an RPG Character
# In this lab you will practice the basics of Python by building a small app that 
# creates a character for an RPG adventure.
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
full_dot = '●'
empty_dot = '○'
def create_character(name,strength, intelligence,charisma):
    if not isinstance(name,str):
        return 'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'
    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be intergers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no nome than 4'
    elif strength+intelligence+charisma != 7:
        return 'The character should start with 7 points'
    def stat_bar(value):
        return full_dot * value + empty_dot * (10 - value)
    
    # Return formatted string
    return f"{name}\nSTR {stat_bar(strength)}\nINT {stat_bar(intelligence)}\nCHA {stat_bar(charisma)}"
print(create_character('ren',3,3,1))