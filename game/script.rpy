label initialization:
    $ inventory = Inventory()
    $ daytime = Daytime()

    $ inventory.AddItem(item1, 1)
    $ inventory.AddItem(item2, 3)

    ### Girls
    call load_all_characters

    ### Quests
    call load_all_quests

    ### Locations
    $ L_map1 = Location("map1")
    $ L_map2 = Location("map2")

    ### Locations Unlock
    $ L_map1.SetUnlockStatus(True)
    
    ### Locations Characters
    $ L_map1.AddCharacterOnMap(lisa, "lisa default", Vector2(0, 0))
    $ L_map2.AddCharacterOnMap(jade, "jade default", Vector2(1, 0))
    
    return

screen Sui:
    #textbutton str(daytime.GetDaytimeName()) action Function(daytime.PassTime()) text_color "#000000"
        
    hbox xalign 1.0 yalign 0.0:
        imagebutton:
            idle "exc"
            hover "exc"

            action [Hide("Sui"), Show("Sinventory")]

label start:
    call initialization

    show screen Sui

    jump map

    return

label map:
    scene None

    call screen Smap

screen Smap:
    add "bg plain" xalign 0.5 yalign 0.5
    
    if L_map1.isUnlocked:
        hbox xalign 0.0 yalign 0.5:
            imagebutton:
                idle "exc"
                hover "exc"

                action L_map1.action

    if L_map2.isUnlocked:
        hbox xalign 1.0 yalign 0.5:
            imagebutton:
                idle "exc"
                hover "exc"

                action L_map2.action