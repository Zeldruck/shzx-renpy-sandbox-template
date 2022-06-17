init -1 python:
    class Npc(object):
        """docstring for Npc"""
        def __init__(self, character, name, choices):
            super(Npc, self).__init__()
            self.choices = choices
            self.actualQuests = []

            self.c = character
            self.name = name

        def AddNewActualQuest(self, actualQuest):
            if actualQuest == None:
                return
            
            self.actualQuests.append(actualQuest)

        
        def RemoveActualQuest(self, actualQuest):
            if actualQuest == None or not (actualQuest in self.actualQuests):
                return

            self.actualQuests.remove(actualQuest)

        
        def GetChoices(self):
            nChoices = self.choices.copy()

            # Add quests choices
            for i in self.actualQuests:
                for x in i.choices:
                    nChoices.insert(len(nChoices)-1, x)

            return nChoices

    def GetCharacterChoicesPath(character):
        if character == None:
            return ""

        return str(str(character.name).lower() + "_choices")