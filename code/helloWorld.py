from psychopy import visual, core, event

win = visual.Window([400,400]) # set up a window that is 400px by 400px
txt = visual.TextStim(win, text = "Hello World!")

for frameN in range(60): # present text for exactly 60 frames
    txt.setOri(frameN) # make stimuli dynamic
    txt.draw()
    win.flip()

win.close()