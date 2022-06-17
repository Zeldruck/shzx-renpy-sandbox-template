label lisa_choices:
    show lisa default
    with dissolve

    call screen choices(lisa.GetChoices())

label lisa_quest1:

    "This is lisa quest1"

    $ lisaQ1.EndQuest()
    $ L_map2.SetUnlockStatus(True)

    "Quest 1 end"

    hide lisa default

    jump map

label lisa_quest2:

    "This is lisa quest2"

    $ lisaQ2.EndQuest()
    $ L_map1.SetUnlockStatus(False)

    $ inventory.AddItem(item1, 1)

    lisa.c "Hey, to thank you here is a [item1.name]"

    lisa.c "Take care"

    "Quest 2 end"

    hide lisa default

    jump map


label lisa_casualTalk:

    "This is lisa casual talk"

    "Return to actual map"

    hide lisa default

    jump map

label lisa_nothing:

    "This is lisa nothing"

    "Return to actual map"

    hide lisa default

    jump map