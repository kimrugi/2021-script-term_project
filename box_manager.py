from info_box import *

class BoxManager:
    def __init__(self, frame, data_list):
        self.box_size = 10
        for i in range(len(data_list)):
            InfoBox(frame, data_list[i], self.box_size, self.box_size*i)

        pass






