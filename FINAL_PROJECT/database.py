users = {
    "chums@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Matthew",
                         "last_name":"Uy",
                         "org":"MedGrocer",
                         "brand":"Sinovac"},
    "joben@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joben",
                         "last_name":"Ilagan",
                         "org":"MedGrocer",
                         "brand":"Sinovac"},
    "bong@example.com":{"password":"Ch@ng3m3!",
                        "first_name":"Bong",
                        "last_name":"Olpoc",
                        "org":"MedGrocer",
                        "brand":"Sinovac"},
    "joaqs@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joaqs",
                         "last_name":"Gonzales",
                         "org":"MedGrocer",
                         "brand":"Sinovac"},
    "gihoe@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Gio",
                         "last_name":"Hernandez",
                         "org":"MedGrocer",
                         "brand":"Sinovac"},
    "vic@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Vic",
                       "last_name":"Reventar",
                       "org":"MedGrocer",
                       "brand":"Sinovac"},
    "joe@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Joe",
                       "last_name":"Ilagan",
                       "org":"MedGrocer",
                       "brand":"Sinovac"},
    "janna@example.com":{"password":"tan",
                         "first_name":"Janna",
                         "last_name":"Tan",
                         "org":"MedGrocer",
                         "brand":"Sinovac"}
}

def get_user(username):
    try:
        return users[username]
    except KeyError:
        return None
