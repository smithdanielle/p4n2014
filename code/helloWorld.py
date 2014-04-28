from psychopy import visual, core, event, logging

logging.console.setLevel(logging.EXP) # add logging objects
logFile = logging.LogFile('lastrun.log','a') # methods in psychopy are camelCase, class is AlternateCase; a for append
logFile.setLevel(logging.DEBUG) # can have different logging levels for different targets
logging.warn("send a warning")
logging.error("you screwed up")
logging.debug("just checking you know that this is happening")

win = visual.Window([400,400]) # set up a window that is 400px by 400px
txt = visual.TextStim(win, text = "Hello World!")

for frameN in range(60): # present text for exactly 60 frames
    txt.setOri(frameN) # make stimuli dynamic
    txt.draw()
    win.flip()

win.close()