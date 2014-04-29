from psychopy import visual, core, event, data, gui
import copy

# set things that don't change throughout the experiment
win = visual.Window([800,800], fullscr=False, units='deg', 
    monitor='default', blendMode='add')
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

rds = visual.DotStim(win, nDots=500, fieldSize=(4,4), 
    fieldShape='sqr', dotLife= -1, speed = 0.0)

rdsLeft = copy.copy(rds)
rdsLeft.setColor([1.0,0,0])
rdsLeft.setFieldPos([-0.15,0])
rdsRight=copy.copy(rds)
rdsRight.setColor([0,0.6,0.6])
rdsRight.setFieldPos([0.15,0])

rdsLeft.draw()
rdsRight.draw()

win.flip()

event.waitKeys()