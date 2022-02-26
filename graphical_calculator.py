from graphics import *
from Button import *
from EasyRectangle import *

class Calculator: 
    def __init__(self):
        """""creating base calculator"""
        self.calcrect = EasyRectangle(0, 0, 150, 150)
        self.calcrect.setFill('lightgreen')
        """""creating inputs"""
        self.input1 = Entry(Point(-30, 40), 15)
        self.input2 = Entry(Point(30, 40), 15)
        """""creating operation buttons"""
        self.add_butt = Button(-20, 20, 10, 10, 'lightpink', '+')
        self.minus_butt = Button(20, 20, 10, 10, 'lightpink', '-')
        self.mult_butt = Button(-20, 5, 10, 10, 'lightpink', '*')
        self.div_butt = Button(20, 5, 10, 10, 'lightpink', '/')
        '''''creating results & result texts'''
        self.result = EasyRectangle(0, -20, 90, 15)
        self.result.setFill('lightyellow')
        self.result_text = Text(Point(0, -15), '')

        self.add_butt_result = Text(Point(0, -15), '')
        self.minus_butt_result = Text(Point(0, -15), '')
        self.mult_butt_result = Text(Point(0, -15), '')
        self.div_butt_result = Text(Point(0, -15), '')
        
        self.clear_butt = Button(-50, -50, 20, 10, 'gray', 'Clear')
        self.result_butt = Button(0, -50, 25, 10, 'gray', 'Result')
        self.quit_butt = Button(50, -50, 20, 10, 'gray', 'Quit')

    """""drawing all features created in __init__ function to the window"""
    def draw(self, win):

        self.calcrect.draw(win)
        self.input1.draw(win)
        self.input2.draw(win)
        self.add_butt.draw(win)
        self.minus_butt.draw(win)
        self.mult_butt.draw(win)
        self.div_butt.draw(win)
        self.result.draw(win)
        self.clear_butt.draw(win)
        self.result_butt.draw(win)
        self.quit_butt.draw(win)
    """""results"""
    def display_result(self, result):
        self.result_text.setText(int(result))

    def clear(self):
        self.input1.setText('')
        self.input2.setText('')
        self.result_text.setText('')

        

    def run(self, win): 
        while True:
            p = win.getMouse()

            if self.quit_butt.clicked(p):
                pass
            elif self.clear_butt.clicked(p):
                self.clear()
            elif self.add_butt.clicked(p) and self.result_butt.clicked(p):
                self.result_text.setText(self.input1 + self.input2)
            elif self.minus_butt.clicked(p):
                self.result_text = self.minus_butt_result
            elif self.mult_butt.clicked(p):
                self.result_text = self.mult_butt_result
            elif self.div_butt.clicked(p):
                self.result_text = self.div_butt_result
        
        
       

def main():
    win = GraphWin('Calculator', 500, 500)
    win.setCoords(-100, -100, 100, 100)
    win.setBackground('lightgray')
 
    calc = Calculator()
    calc.draw(win)
    calc.run(win)
    #win.getMouse()
    
    win.close()

main()