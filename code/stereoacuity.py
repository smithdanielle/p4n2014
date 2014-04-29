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
info['refDisp'] = 0.16 # disparity of reference stays constant at 0.16 deg


#create the base filename for our data files
fileName = "data/{participant}_{dateStr}".format(**info)
#dataFile = open(fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'

#create the staircase handler
staircase = data.StairHandler(startVal = 0.3,
                          stepType = 'lin', stepSizes=[0.05,0.03,0.03,0.02,0.02,0.01,0.01],
                          nUp=1, nDown=1,  #will home in on the 50% threshold

# initialise stimuli
fixation = visual.Circle(win, size = 0.25,
    lineColor = 'white', fillColor = 'lightGrey')
    
rds=visual.DotStim(win, nDots=500, fieldSize=(4,4), fieldShape='sqr', dotLife= -1, speed = 0.0)

target = copy.copy(rds)

reference = copy.copy(rds)

referenceLeft=copy.copy(reference)
referenceLeft.setColor([1.0,0,0])
referenceLeft.setFieldPos([-(info['refDisp'])/2,0])
referenceRight=copy.copy(reference)
referenceRight.setColor([0,0.6,0.6])
referenceRight.setFieldPos([(info['refDisp'])/2,0])

# display fixation cross
fixation.draw()
win.flip()
event.waitKeys()

for thisIncrement in staircase:
    # set location of the stimuli
    targetSide= random.choice([-1,1]) #will be either +1(right) or -1(left)
    referenceLeft.setPos([-5*targetSide, 0])
    referenceRight.setPos([-5*targetSide, 0])
    
    # set disparity of target
    targetLeft=copy.copy(target)
    targetLeft.setColor([1.0,0,0])
    targetLeft.setFieldPos(-thisIncrement/2,0])
    targetRight=copy.copy(target)
    targetRight.setColor([0,0.6,0.6])
    targetRight.setFieldPos(thisIncrement/2,0])
    
    # draw all stimuli
    referenceLeft.draw()
    referenceRight.draw()
    targetLeft.draw()
    targetRight.draw()
    fixation.draw()
    
    # now show them
    win.flip()
    core.wait(2)
    
    # blank screen
    fixation.draw()
    
    #get response
    thisResp=None
    while thisResp==None:
        allKeys=event.waitKeys()
        for thisKey in allKeys:
            if thisIncrement<refDisp:
                if thisKey=='right':
                    if targetSide==-1: thisResp = 1#correct
                    else: thisResp = -1             #incorrect
                elif thisKey=='left':
                    if targetSide== 1: thisResp = 1#correct
                    else: thisResp = -1             #incorrect
            elif thisIncrement>refDisp:
                if thisKey=='left':
                    if targetSide==-1: thisResp = 1#correct
                    else: thisResp = -1             #incorrect
                elif thisKey=='left':
                    if targetSide== 1: thisResp = 1#correct
                    else: thisResp = -1             #incorrect
            elif thisKey in ['q', 'escape']:
                core.quit() #abort experiment
                
    #add the data to the staircase so it can calculate the next level
    staircase.addData(thisResp)
    dataFile.write('%i,%.3f,%i\n' %(targetSide, thisIncrement, thisResp))

#staircase has ended
dataFile.close()

win.close()