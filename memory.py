#implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals

def new_game():
    
    global state, list1,list2, exposed, prev1,prev2,count
    # prev1, prev2 store the index of each of the two cards
    # that were clicked in the previous turn.
    list1 = []
    list2 = []
    count = 0
    #To count the numbers of turns
    state = 0
    exposed=[]
    for i in range(8):
        list1.append(i)
        list2.append(i)
    #append list1 into list2 to make a list of 16 elements
    list2.extend(list1)   
    random.shuffle(list2)
    #Initialze exposed to False
    for i in range(len(list2)):
        exposed.append(False)
    
    
   
  
    
# define event handlers
def mouseclick(pos):
    global state
    global exposed,prev1,prev2,count    
   
    if state == 0:       
         exposed[pos[0]/50] = True
         state = 1
         prev1 = pos[0]/50
        
    elif state == 1:
      if not exposed[pos[0]/50]:  
        exposed[pos[0]/50] = True
        state = 2
        prev2 = pos[0]/50
        count +=1
        label.set_text("Turns = "+str(count))
        
    elif state == 2:
       if not exposed[pos[0]/50]:  
          exposed[pos[0]/50] = True
        
          if list2[prev1]!=list2[prev2]:
            exposed[prev1] = False
            exposed[prev2] = False
          prev1=pos[0]/50
          state = 1
        
   
    
def draw(canvas):
    for i in range(len(list2)):
      if exposed[i]:
         canvas.draw_text(str(list2[i]), [50*i,50], 40, "WHITE")
      else:       
         canvas.draw_polygon([(50*(i),0), (50*(i+1),0),(50*(i+1),100), (50*i,100)], 1, 'RED','GREEN')
     
     
# create frame and add a button and labels
frame = simplegui.create_frame("Memory states", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
# get things rolling
new_game()
frame.start()

