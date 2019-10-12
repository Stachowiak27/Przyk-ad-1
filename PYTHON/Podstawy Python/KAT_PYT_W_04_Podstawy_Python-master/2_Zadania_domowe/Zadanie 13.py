
def censor(text):
    new_text = text.split(" ")
    censor_list = ["Java","C#","Ruby","PHP"]
    for item in censor_list:
        if item in text:
            new_string = text.replace(item,"****")
            return new_string


c = (censor("Java is the best, but PHP is the bestests!"))

print(c)


