init -1 python:
    class Quest(object):
        """docstring for Quest"""
        def __init__(self, characterQuest, hint, newChoices):
            super(Quest, self).__init__()
            self.isCompleted = False
            
            self.c = characterQuest

            self.cQuests = []
            self.nQuests = []
            self.nCharacters = []

            self.hint = hint
            self.choices = newChoices

        def DefineQuest(self, completedQuestsRequired, nextQuests, nextCharacters):
            self.cQuests = completedQuestsRequired
            self.nQuests = nextQuests
            self.nCharacters = nextCharacters
        
        def EndQuest(self):
            self.isCompleted = True
            self.c.RemoveActualQuest(self)

            for i in range(len(self.nCharacters)):
                self.nCharacters[i].AddNewActualQuest(self.nQuests[i])