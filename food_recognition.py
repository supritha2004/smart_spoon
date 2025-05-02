
def recognize_food_name(filename):
    name = filename.lower()
    if 'soup' in name:
        return 'soup', 300
    elif 'salad' in name:
        return 'salad', 100
    elif 'meat' in name:
        return 'meat', 250
    return 'unknown', 150
