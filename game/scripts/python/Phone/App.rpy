init python:
    class App(object):
        """docstring for App"""
        def __init__(self, appName, appIcon, appScreen):
            super(App, self).__init__()
            self.appName = appName
            self.appIcon = appIcon
            self.appScreen = appScreen

            self.openAction = [ToggleScreen(appScreen), Function(phone.AddAppToNavigation, self)]
            self.closeAction = ToggleScreen(appScreen);
            self.returnAction = ToggleScreen(appScreen);

screen AppIcon(app):
    vbox:
        xalign 0.0 
        yalign 0.5
        spacing 0

        hbox:
            spacing 0

            imagebutton:
                idle app.appIcon
                hover app.appIcon

                action app.openAction
            
            text app.appName