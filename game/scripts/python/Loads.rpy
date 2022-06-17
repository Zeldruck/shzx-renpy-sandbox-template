label after_load:
    call load_all_characters
    call load_all_quests

    return

label load_all_characters:
    if jade == None:
        $ jade = Npc(Character("Jade"), "Jade", [ChoiceTab("Casual talk", "jade_casualTalk"), ChoiceTab("Nothing", "jade_nothing")])
    if lisa == None:
        $ lisa = Npc(Character("Lisa"), "Lisa", [ChoiceTab("Casual talk", "lisa_casualTalk"), ChoiceTab("Nothing", "lisa_nothing")])
        
    return


label load_all_quests:
    # Define quests
    # Jade
    if jadeQ1 == None:
        $ jadeQ1 = Quest(jade, "Quest1 jade hint...", [ChoiceTab("Quest1 jade", "jade_quest1")])
    if jadeQ2 == None:
        $ jadeQ2 = Quest(jade, "Quest2 jade hint...", [ChoiceTab("Quest2 jade", "jade_quest2")])
    if jLisaQ1 == None:
        $ jLisaQ1 = Quest(jade, "Quest1 jade for lisa hint...", [ChoiceTab("Quest1 jade for lisa", "jade_for_lisa_quest1")])

    # Lisa
    if lisaQ1 == None:
        $ lisaQ1 = Quest(lisa, "Quest1 hint...", [ChoiceTab("Quest1", "lisa_quest1")])
    if lisaQ2 == None:
        $ lisaQ2 = Quest(lisa, "Quest2 hint...", [ChoiceTab("Quest2", "lisa_quest2")])


    # Define paths
    # Jade
    $ jadeQ1.DefineQuest([], [jadeQ2], [jade]) # jade
    $ jadeQ2.DefineQuest([], [], []) # jade

    $ jLisaQ1.DefineQuest([], [lisaQ2], [lisa]) # jade for lisa

    # Lisa
    $ lisaQ1.DefineQuest([], [jLisaQ1], [jade]) # lisa
    $ lisaQ2.DefineQuest([], [], []) # lisa


    # Define first quests for the characters if needed
    if not jadeQ1.isCompleted and not (jadeQ1 in jade.actualQuests):
        $ jade.AddNewActualQuest(jadeQ1)

    if not lisaQ1.isCompleted and not (lisaQ1 in lisa.actualQuests):
        $ lisa.AddNewActualQuest(lisaQ1)

    return