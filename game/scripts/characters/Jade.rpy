label jade_choices:
    #Set outfit and bg with location
    show jade default
    with dissolve

    call screen choices(jade.GetChoices())


label jade_quest1:

    "This is jade quest1"

    $ jadeQ1.EndQuest()

    "Quest end"

    "Jade asks you to find [item1.name] x2 for her"

    hide jade default

    jump map


label jade_quest2:
    if inventory.HasItem(item1, 2):
        $ inventory.RemoveItem(item1, 2)

        jade.c "Thank you for the 2 [item1.name]"

        $ jadeQ2.EndQuest()

        "Quest end"
    else:
        jade.c "You still don't have what I asked you ?"


    hide jade default

    jump map


label jade_for_lisa_quest1:

    "This is jade for lisa quest1"

    $ jLisaQ1.EndQuest()

    "Quest end"

    hide jade default

    jump map


label jade_casualTalk:

    "This is jade casual talk"

    "Return to actual map"
    
    hide jade default

    jump map

    return


label jade_nothing:

    "This is jade nothing"

    "Return to actual map"

    hide jade default

    jump map

    return