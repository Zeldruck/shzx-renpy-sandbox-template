init python:
    class Inventory(object):
        """docstring for Inventory"""
        def __init__(self):
            super(Inventory, self).__init__()
            self.items = []
            self.nb = []

        def HasItem(self, item, nb):
            return (item in self.items and self.nb[self.items.index(item)] >= nb)

        def AddItem(self, item, nb):
            if nb <= 0:
                return

            if item in self.items:
                self.nb[self.items.index(item)] += nb
            else:
                self.items.append(item)
                self.nb.append(nb)

            renpy.notify(str(nb) + " " + item.name + " have been added to your inventory")

        def RemoveItem(self, item, nb, forceRemove = False):
            if nb <= 0 or not(item in self.items):
                return

            itemIndex = self.items.index(item)
            currentNbItems = self.nb[itemIndex]

            if currentNbItems > nb:
                self.nb[itemIndex] -= nb
                renpy.notify(nb + " " + item.name + " have been removed from your inventory")
            elif currentNbItems == nb or forceRemove:
                renpy.notify(str(self.nb[itemIndex]) + " " + item.name + " have been removed from your inventory")
                self.items.pop(itemIndex)
                self.nb.pop(itemIndex)
            
    
    class Item(object):
        """docstring for Item"""
        def __init__(self, name, icon):
            super(Item, self).__init__()
            self.name = name
            self.icon = icon
       

screen Sinventory:
    add "black"

    # quit button
    hbox xalign 1.0 yalign 0.0:
        imagebutton:
            idle "exc"
            hover "exc"

            action [Hide("Sinventory"), Show("Sui")]


    grid 5 int(math.ceil(len(inventory.items) / 5.0)):
        xspacing 0
        yspacing 50

        xalign 0.5
        yalign 0.0

        ypos 0.3

        for i in range(len(inventory.items)):
            vbox:
                xalign 0.0 
                yalign 0.5

                spacing 0

                hbox:
                    spacing 0

                    imagebutton:
                        idle inventory.items[i].icon
                        hover inventory.items[i].icon

                    text str(inventory.nb[i]) xpos -50

        for i in range(int(math.ceil(len(inventory.items) / 5.0)) * 5 - len(inventory.items)):
            null

screen SinventoryItemTooltip(xpos, ypos, item):
    #
    add "black"