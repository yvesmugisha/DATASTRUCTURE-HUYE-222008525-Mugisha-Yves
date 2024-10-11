         # FOOD DONATION SYSTEM 


available_food = []
undo_stack = []
donation_queue = []

def add_food(food_item):
    available_food.append(food_item)

def donate_food(food_item):
    if food_item in available_food:
        available_food.remove(food_item)
        donation_queue.append(food_item)
        undo_stack.append(food_item)

def process_donation():
    if donation_queue:
        return donation_queue.pop(0)

def undo_last_donation():
    if undo_stack:
        food_item = undo_stack.pop()
        available_food.append(food_item)
        return food_item

def get_available_food():
    return available_food

def get_donation_queue():
    return donation_queue

add_food("Apples")
add_food("Bread")
donate_food("Apples")

print(get_available_food())
print(get_donation_queue())
process_donation()
print(get_donation_queue())
undo_last_donation()
print(get_available_food())
