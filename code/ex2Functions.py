# Load psychopy modules
from psychopy import visual, event, core
win = visual.Window(size=[500, 500])
text = visual.TextStim(win)

# Messages
welcome = 'hi and welcome to this experiment'
instruction = 'really, there\'s not much to do. We just show a bunch of messages. Press RETURN to continue.'
thanks = 'thank you and goodbye. We hope you enjoyed!'

# Show welcome message
text.setText(welcome)  # set text
text.draw()  # prepare to show it
win.flip()  # actually show it
response = event.waitKeys(keyList=None)  # accepts all keys
if response[0] == 'q':  # response[0] is the name of the first pressed key
    core.quit()  # quit if 'q' was pressed

# Show instruction
text.setText(instruction)
text.draw()
win.flip()
response = event.waitKeys(keyList=['return', 'q'])  # listen for return and q only
if response[0] == 'q':
    core.quit()

# Show debriefing
text.setText(thanks)
text.draw()
win.flip()
response = event.waitKeys#(keyList=None)  # accepts all keys