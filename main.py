class Elevator:
    def __init__(self,bottom,top):
        self.bottom=bottom
        self.top=top
        self.floor=bottom

    def floor_up(self):
        self.floor=self.floor+1
    def floor_down(self):
        self.floor=self.floor-1
    def go_to_floor(self,ch):


        if ch>=self.top or ch<=self.bottom:
            print('invalid floor')

        while ch!=self.floor and ch<=self.top and ch>=self.bottom:
            if self.floor<ch:
                self.floor_up()
            if self.floor>ch:
                self.floor_down()
            print(self.floor)
#h=Elevator(0,10)
#h.go_to_floor(6)
#h.go_to_floor(0)

class Builduing:
    def __init__(self,top,bottom,no):
        self.top=top
        self.bottom=bottom
        self.no=no
        self.l=[]

        for i in range(self.no):

            self.l.append(Elevator(self.bottom,self.top))

    def run_elevator(self, elevator_no, floor):
        self.l[elevator_no].go_to_floor(floor)
    def fire_alarm(self):
        for i in self.l:
            i.go_to_floor(self.bottom)

b=Builduing(10,0,7)
b.run_elevator(3,5)
b.fire_alarm()











