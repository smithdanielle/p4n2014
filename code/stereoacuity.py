from psychopy import visual, core, event, data, gui

# set things that don't change throughout the experiment
win = visual.Window([400,400], fullscr=False, units='deg', monitor='default')
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
fileName = "data/{participant}_{dateStr}".format(**info)
#dataFile = open(fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'

# initialise stimuli
fixation = visual.Circle(win, size = 0.25,
    lineColor = 'white', fillColor = 'lightGrey')

rds = visual.DotStim(win, nDots=500, fieldSize=(2,2), 
    fieldShape='sqr', dotLife= -1, speed = 0.0, color='white')

#create the staircase handler
#staircase = data.StairHandler(startVal = 20.0,
#                          stepType = 'db', stepSizes=[8,4,4,2,2,1,1],
#                          nUp=1, nDown=3,  #will home in on the 80% threshold

rds.draw()

win.flip()

event.waitKeys()