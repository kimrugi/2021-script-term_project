from info_box import *

class BoxManager:
    def __init__(self, frame, data_list):
        self.box_size = 100
        self.selection = None
        self.box_list = []
        for i in range(len(data_list)):
            self.box_list.append(InfoBox(frame, data_list[i], self.box_size, lambda n=i: self.select(n)))

    def select(self,n):
        if self.selection is not None:
            self.box_list[self.selection].button_unselected()
        self.selection = n
        self.box_list[n].button_selected()

    def get_selection(self):
        return self.selection

