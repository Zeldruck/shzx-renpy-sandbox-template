label start:
    #Initialize the whole game's datas
    call initialization

    # Top bar ui informations
    show screen Sui

    # Start from the main map
    jump map

    return


label initialization:

    # Create the inventory & the day and time system
    $ inventory = Inventory()
    $ daytime = Daytime()

    # Add few items
    $ inventory.AddItem(item1, 1)
    $ inventory.AddItem(item2, 3)

    ### Girls
    call load_all_characters

    ### Quests
    call load_all_quests

    ### Locations
    call load_all_locations

    ### Locations Unlock during start
    $ L_map1.SetUnlockStatus(True)
    
    ### Locations Characters during start
    $ L_map1.AddCharacterOnMap(lisa, "lisa default", Vector2(0, 0))
    $ L_map2.AddCharacterOnMap(jade, "jade default", Vector2(1, 0))
    
    return

### Top bar ui
screen Sui:
    #textbutton str(daytime.GetDaytimeName()) action Function(daytime.PassTime()) text_color "#000000"
        
    hbox xalign 1.0 yalign 0.0:
        imagebutton:
            idle "exc"
            hover "exc"

            action [Hide("Sui"), Show("Sinventory")]

# Main map
label map:
    scene None

    call screen Smap

# Main map screen
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