from psychopy import visual, core, event, data, gui

# set things that don't change throughout the experiment
win = visual.Window([400,400], fullscr=False, units='pix')
globalClock = core.Clock()
respClock = core.Clock()

# initialise experiment information
info = {} # a dictionary
info['participant'] = ''
dlg = gui.DlgFromDict(info) # present dialog to collect info
if not dlg.OK:
    core.quit()
info['dateStr'] = data.getDateStr() #will create str of current date/time

#create the base filename for our data files
filename = "data/{participant}_{dateStr}".format(**info)
# initialise stimuli
fixation = visual.Circle(win, size = 5,
    lineColor = 'white', fillColor = 'lightGrey')

rds = visual.DotStim(win, nDots=500, fieldSize=(100,100), 
    fieldShape='sqr', dotLife= -1, speed = 0.0, color='white')

rds.draw()

win.flip()
event.waitKeys()