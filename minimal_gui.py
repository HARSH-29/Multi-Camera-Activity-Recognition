
# coding: utf-8

# In[ ]:


from tkinter import * ;
master = Tk() ;
master.geometry ( "200x200" ) ;

def run_testing() :
    import subprocess as sp ;
    sp.Popen( ['python' , 'final_gui.py'] ) ;


def closewindow() :
    exit() ;

def run_training() :
	import subprocess as sp ;
	sp.Popen ( ['python' , 'main_code.py'] ) ;
button3 = Button ( master , text="Run Training" , width = 10 , command=run_training ) ;
button3.pack() ;

button = Button ( master , text="Run Testing" , width = 10 , command=run_testing ); 
button.pack() ;

button2 = Button ( master , text = "Close Window" , width = 10 , command=closewindow ) ;
button2.pack() ;

master.mainloop()

