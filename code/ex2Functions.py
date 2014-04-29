# Load psychopy modules
from psychopy import visual, event, core

# Initialise stimuli
win = visual.Window(size=[500, 500])
textStim = visual.TextStim(win)
# Messages
welcome = 'hi and welcome to this experiment'
instruction = 'really, there\'s not much to do. We just show a bunch of messages. Press RETURN to continue.'
thanks = 'thank you and goodbye. We hope you enjoyed!'

# Create a function to show text
def showText(input, acceptedKeys=None):
    """Presents text and waits for accepted keys"""
    
    # Set and display text
    textStim.setText(input)
    textStim.draw()
    win.flip()
    
    # Wait for response and return it
    response = event.waitKeys(keyList=acceptedKeys)
    if response[0] == 'q':
        core.quit()
    return response

# Show welcome message
showText(welcome)

# Show instruction
showText(instruction, ['return', 'q'])

# Show debriefing
showText(thanks)
