print("The list of medals in Taekwondo Olympics 2020 women 49 kilograms: ")
takwondo_olympics2020_w49k = {
    "Gold" : {"Thailand"},
    "Silver" : {"Spain"},
    "Bronze" : {"Israel", "Serbia"}
}

for type, menus_in_group in takwondo_olympics2020_w49k.items():

    for each_menu in menus_in_group:
        print(f"{each_menu } received {type} medal")

print("The dictionary of medal is ", (takwondo_olympics2020_w49k))

# Name = Alinkar Lu
# Student ID = 643040818-5