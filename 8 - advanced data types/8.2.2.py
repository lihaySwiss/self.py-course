def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda tuple: tuple[1], reverse = True)
    
    