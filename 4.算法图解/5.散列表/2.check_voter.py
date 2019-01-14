voted = {}


def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


check_voter("tom")  # let them vote!
check_voter("mike")  # let them vote!
check_voter("mike")  # kick them out!
