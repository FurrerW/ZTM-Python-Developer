user_info = {
    "first_name": "Walter",
    "last_name": "Furrer",
    "age": 32,
    "country": "USA",
    "state": "NY",
    "city": "Islip",
    }

city_state = user_info["city"] + ", " + user_info["state"]
full_name = user_info["first_name"] + " " + user_info["last_name"]

greeting = "Hi, my name is " + full_name + ". I am " + str(user_info["age"]) + " years old, and I live in " + city_state + "."

print(greeting)

greeting2 = f"Hi, my name is {full_name}."

print(greeting2)