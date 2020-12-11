personal_info = {"height":"168cm",
                 "Fav_Color":"Black",
                 "Fav_Author":"Dale Carnegie"}
question = input("Type 'height' or 'Fav_Color' or 'Fav_Author' to know about me: ")
print(personal_info.get(question))
