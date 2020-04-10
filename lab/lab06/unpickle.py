import pickle

def most_common(List): 
    max = List[0]
    max_count = List.count(max)
    for element in List:
        count = List.count(element)
        if count > max_count:
            max = element
            max_count = count
    return max

DATA = pickle.load(open("shapecolour.p", "rb")) # alternative way
common = most_common(DATA)
print(f"Shape: {common['shape']}")
print(f"Colour: {common['colour']}")

# print(DATA)

