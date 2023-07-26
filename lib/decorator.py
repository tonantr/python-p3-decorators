def decorator(func):
    def wrapper():
        print(
            'I am the output that lets you know the function is about to be called.'
        )
        func()
        print(
            'I am the output that lets you know the function has been called.'
        )
    return wrapper

def get_called():
    print('I am the function and I am being called.')


# get_called = decorator(get_called)
# get_called()

# -------------------------------

def sweep_floors(time):
    if 1100 < time < 2100:
        print("Sweeping the floors...")
    else:
        print("I'm off duty!")

def wash_dishes(time):
    if 1100 < time < 2100:
        print("Washing the dishes...")
    else:
        print("I'm off duty!")

def chop_vegetables(time):
    if 1100 < time < 2100:
        print("Chopping the vegetables...")
    else:
        print("I'm off duty!")

# ----------------------------------

def checking_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@checking_working_hours
def sweep_floors(time):
    print('Sweeping the floors...')

@checking_working_hours
def wash_dishes(time):
    print('Washing the dishes...')

@checking_working_hours
def chop_vegetables(time):
    print('Chooping the vegetables...')



sweep_floors(800)
# I'm off duty!
wash_dishes(1000)
# I'm off duty!
chop_vegetables(1200)
# Chopping the vegetables...