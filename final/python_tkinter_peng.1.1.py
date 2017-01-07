#python tkinter
#python version 3.3.2

from tkinter import *


__author__ = {'author' : 'Chengcheng',
              'Email' : '435941269@qq.com',
              'Created' : '2016-12-21',
              'Version' : '1.1'}

class Peng(Frame):
    def createWidgets(self):
        self.scaling = 100.0
        self.canvas_width = 10
        self.canvas_height = 5.6
        self.draw = Canvas(self, width=(self.canvas_width * self.scaling),
                           height=(self.canvas_height * self.scaling),
                           bg='white')

        self.speed = Scale(self, orient=HORIZONTAL, label="ball speed",
                           from_=-200, to=200)
        
        self.speed.pack(side=BOTTOM, fill=X)

        self.ball_d = 1.0
        self.scaling_left = round(self.ball_d / 2, 1)
        self.scaling_right = self.canvas_width - self.scaling_left
        self.scaling_bottom = self.canvas_height - self.scaling_left
        self.scaling_top = self.scaling_left
       
        self.scale_value = self.speed.get() * 0.1
       
        self.balls = []
        self.ball_x = []
        self.ball_y = []
        self.ball_v_x = []
        self.ball_v_y = []

        self.ball = self.draw.create_oval("0.60i", "0.60i", "1.60i", "1.60i",
                                          fill="red")
        self.second_ball = self.draw.create_oval("2.0i", "2.0i", "3.0i", "3.0i",
                                                 fill='black')
        self.three_ball = self.draw.create_oval("4.0i", "4.0i", "5.0i", "5.0i",
                                                 fill='brown')
        self.four_ball = self.draw.create_oval("6.0i", "2.0i", "7.0i", "3.0i",
                                                 fill='green')
        self.five_ball = self.draw.create_oval("8.0i", "3.0i", "9.0i", "4.0i",
                                                 fill='gray')

        self.balls.append(self.ball)
        self.balls.append(self.second_ball)
        self.balls.append(self.three_ball)
        self.balls.append(self.four_ball)
        self.balls.append(self.five_ball)

        self.x = 1.1        
        self.y = 1.1
        self.velocity_x = -0.2
        self.velocity_y = 0.1

        self.second_ball_x = 2.5
        self.second_ball_y = 2.5
        self.second_ball_v_x = 0.1
        self.second_ball_v_y = -0.2

        self.three_ball_x = 4.5
        self.three_ball_y = 4.5
        self.three_ball_v_x = -0.1
        self.three_ball_v_y = -0.2

        self.four_ball_x = 6.5
        self.four_ball_y = 2.5
        self.four_ball_v_x = 0.1
        self.four_ball_v_y = -0.2

        self.five_ball_x = 8.5
        self.five_ball_y = 3.5
        self.five_ball_v_x = 0.1
        self.five_ball_v_y = 0.2

        
        self.update_ball_x_y()
        self.draw.pack(side=LEFT)

    def update_ball_x_y(self, *args):
        self.ball_x.append(self.x)
        self.ball_y.append(self.y)
        self.ball_v_x.append(self.velocity_x)
        self.ball_v_y.append(self.velocity_y)

        self.ball_x.append(self.second_ball_x)
        self.ball_y.append(self.second_ball_y)
        self.ball_v_x.append(self.second_ball_v_x)
        self.ball_v_y.append(self.second_ball_v_y)

        self.ball_x.append(self.three_ball_x)
        self.ball_y.append(self.three_ball_y)
        self.ball_v_x.append(self.three_ball_v_x)
        self.ball_v_y.append(self.three_ball_v_y)

        self.ball_x.append(self.four_ball_x)
        self.ball_y.append(self.four_ball_y)
        self.ball_v_x.append(self.four_ball_v_x)
        self.ball_v_y.append(self.four_ball_v_y)

        self.ball_x.append(self.five_ball_x)
        self.ball_y.append(self.five_ball_y)
        self.ball_v_x.append(self.five_ball_v_x)
        self.ball_v_y.append(self.five_ball_v_y)
    
    def update_ball_velocity(self, index, *args):
        self.scale_value = self.speed.get() * 0.1
        if (self.ball_x[index] > self.scaling_right) or (self.ball_x[index] < self.scaling_left):
            self.ball_v_x[index] = -1.0 * self.ball_v_x[index]
        if (self.ball_y[index] > self.scaling_bottom) or (self.ball_y[index] < self.scaling_top):
            self.ball_v_y[index] = -1.0 *  self.ball_v_y[index]

        
        for n in range(len(self.balls)):
            if (round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2) <= round(self.ball_d**2, 2)):
                temp_vx = self.ball_v_x[index]
                temp_vy = self.ball_v_y[index]
                self.ball_v_x[index] = self.ball_v_x[n]
                self.ball_v_y[index] = self.ball_v_y[n]
                self.ball_v_x[n] = temp_vx
                self.ball_v_y[n] = temp_vy
        #print(self.ball_v_x, self.ball_v_y)
        
        
    def get_ball_deltax(self, index, *args):
        deltax = (self.ball_v_x[index] * self.scale_value / self.scaling)
        self.ball_x[index] = self.ball_x[index] + deltax
        return deltax

    def get_ball_deltay(self, index, *args):
        deltay = (self.ball_v_y[index] * self.scale_value / self.scaling)
        self.ball_y[index] = self.ball_y[index] + deltay
        return deltay
    
    def moveBall(self, *args):
        self.update_ball_velocity(0)       
        deltax = self.get_ball_deltax(0)
        deltay = self.get_ball_deltay(0)
        self.draw.move(self.ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.moveBall)

    def move_second_ball(self, *args):
        self.update_ball_velocity(1)       
        deltax = self.get_ball_deltax(1)
        deltay = self.get_ball_deltay(1)        
        self.draw.move(self.second_ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_second_ball)


    def move_three_ball(self, *args):
        self.update_ball_velocity(2)       
        deltax = self.get_ball_deltax(2)
        deltay = self.get_ball_deltay(2)
        self.draw.move(self.three_ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_three_ball)

    def move_four_ball(self, *args):
        self.update_ball_velocity(3)       
        deltax = self.get_ball_deltax(3)
        deltay = self.get_ball_deltay(3)
        self.draw.move(self.four_ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_four_ball)

    def move_five_ball(self, *args):
        self.update_ball_velocity(4)       
        deltax = self.get_ball_deltax(4)
        deltay = self.get_ball_deltay(4)
        self.draw.move(self.five_ball,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_five_ball)

            
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()
        self.after(10, self.moveBall)
        self.after(10, self.move_three_ball)
        self.after(10, self.move_four_ball)
        self.after(10, self.move_five_ball)
        self.after(10, self.move_second_ball)
        
        
game = Peng()

game.mainloop()
