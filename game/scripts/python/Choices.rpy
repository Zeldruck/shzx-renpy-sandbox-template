init -1 python:
    class ChoiceTab(object):
        """docstring for ChoiceTab"""
        def __init__(self, title, jumpLabel):
            super(ChoiceTab, self).__init__()
            self.title = title
            self.label = jumpLabel
            self.action = Jump(jumpLabel)

screen choices(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.title action i.action