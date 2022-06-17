init -1 python:
    class Location(object):
        """docstring for Location"""
        def __init__(self, locationLabel):
            super(Location, self).__init__()
            self.characters = []
            self.sCharacters = []
            self.cPositions = []

            self.label = locationLabel
            self.action = Jump(locationLabel)
            self.isUnlocked = False
            
        def SetUnlockStatus(self, unlockStatus):
            self.isUnlocked = unlockStatus

        def AddCharacterOnMap(self, character, spriteCharacterName, v2Pos):
            if character == None and character in self.characters:
                return

            self.characters.append(character)
            self.sCharacters.append(spriteCharacterName)
            self.cPositions.append(v2Pos)

        def RemoveCharacterOnMap(self, character):
            if character == None and not(character in self.characters):
                return

            pIndex = self.characters.index(character)
            self.characters.remove(character)
            self.sCharacters.pop(pIndex)
            self.cPositions.pop(pIndex)