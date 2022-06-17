label map1:
    # Show bg in function of the time TODO

    scene bg map1_day

    "This is map 1 & try events on going on this map #TODO"

    call screen Smap1

screen Smap1:
    # Show bg in function of the time TODO

    #add bg map1_day xalign 0.5 yalign 0.5

    for i in range(len(L_map1.characters)):
        hbox xalign 0.0 yalign 0.0:
            xpos L_map1.cPositions[i].x
            ypos L_map1.cPositions[i].y

            imagebutton:
                idle L_map1.sCharacters[i]
                hover L_map1.sCharacters[i]

                action Jump(GetCharacterChoicesPath(L_map1.characters[i]))


label map2:
    # Show bg in function of the time TODO

    scene bg map2_day

    "This is map 2 & try events on going on this map #TODO"

    call screen Smap2

screen Smap2:
    # Show bg in function of the time TODO

    #add "bg map2 day" xalign 0.5 yalign 0.5

    for i in range(len(L_map2.characters)):
        hbox xalign 0.0 yalign 0.0:
            xpos L_map2.cPositions[i].x
            ypos L_map2.cPositions[i].y

            imagebutton:
                idle L_map2.sCharacters[i]
                hover L_map2.sCharacters[i]

                action Jump(GetCharacterChoicesPath(L_map2.characters[i]))