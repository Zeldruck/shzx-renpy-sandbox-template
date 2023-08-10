init python:
    class Phone(object):
        """docstring for Phone"""
        def __init__(self, phoneHomeScreen):
            super(Phone, self).__init__()
            self.phoneHomeScreen = phoneHomeScreen

            self.navigation = []

        def ReturnToLastApp(self):
            if len(self.navigation) == 0:
                return

            lastApp = self.navigation.pop(0)
            # Do smth with it

        def ResetNavigation(self):
            self.navigation = []

        def AddAppToNavigation(self, app):
            if app == None:
                return

            self.navigation.insert(0, app)

        

screen PhoneMainScreen():
    add "black"

    # quit button
    hbox xalign 1.0 yalign 0.0:
        imagebutton:
            idle "exc"
            hover "exc"

            action [Hide(phone.phoneHomeScreen), Show("Sui")]


    grid 2 2:
        xspacing 0
        yspacing 50

        xalign 0.5
        yalign 0.0

        ypos 0.3
        
        # Settings App -- Do a custom screen for app icons
        use AppIcon(app_settings)

        for i in range(3):
            null
    
    use PhoneBottomBar

screen PhoneBottomBar(app = None):
    # home button
    hbox xalign 0.5 yalign 1.0:
        imagebutton:
            idle "exc"
            hover "exc"

            if app != None:
                action [app.closeAction, Function(phone.ResetNavigation)]

screen app_settings_screen():
    add "black"

    use PhoneBottomBar(app_settings)