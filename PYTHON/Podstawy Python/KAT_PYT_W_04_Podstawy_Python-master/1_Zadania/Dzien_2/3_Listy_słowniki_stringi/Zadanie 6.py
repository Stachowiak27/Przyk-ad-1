
def message(input_dict):
   return "In"+" "+input_dict['movie']+" "+input_dict["name"]+" "+"is the"+" "+input_dict["role"]

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))

name = "Han Solo"
role = "smuggler"
movie = "Star Wars"

s = f"In {movie} , {name} is a {role}."

print(s)

print("================================================")
input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"}

for item in input_dict:
    print(item,input_dict[item])