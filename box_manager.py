from info_box import *

class BoxManager:
    def __init__(self, frame, data_list):
        self.box_size = 100
        self.selection = None
        for i in range(len(data_list)):
            InfoBox(frame, data_list[i], self.box_size, lambda n=i: self.select(n))

        pass
    def select(self,n):
        self.selection = n

    def get_selection(self):
        return self.selection






