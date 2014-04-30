# Data analysis
Using a programming language to analyse data allows reproducibility.

## Scipy ecosystem
Many different libraries for data analysis in Python.

`numpy.random` is an entire module dedicated to generation of random numbers.

The `scipy` library contains lots of useful hodgepodge like optimisation routines.

## Matplotlib
Doesn't look much better than R, but has very nice interactive graphs (for instance, will zoom in on a selected part of a graph).

Can also import images as 3D array (w-pix, h-pix, channels (r, g, b, and alpha). Can then plot as slices (i.e. only one channel etc) - very good at manipulating images (e.g. sliced fourier transform of an image - can show high and low frequencies).

## Analysing data from the Posner task
Always keep `.psydat` files -- useful for reproducible research. Most analysis is done using `.csv` files though. Logfiles are useful for looking at information you'd have forgotten to save otherwise (i.e. timings).

Don't use dot notation in `pandas` `df` for indexing - use explicit naming instead, which makes it work like a dictionary.

# Eyetracking

Look at [Pupil-Lab](www.pupil-lab.org). Could I use [Gazeparser](http://gazeparser.sourceforge.net/) to make my Eyewriter and Psychopy talk to each other? Perhaps email [Sol Simpson](https://github.com/isolver) to ask about incorporating it into `ioHub` for easy universal eyetracker control and data collection?

I quite fancy starting to build hardware as a hobby - for instance, an eyetracker, Arduino RT box... Let's see.

# Extending Builder
If you include a `README` file in the same directory as an experiment file, it will automatically open when the experiment is loaded in Builder. Many variables are always defined when using a Builder script (e.g. `globalClock`), so they can be referenced within code components.

If we compile a Builder script, open it in Coder view and change it, the changes won't be carried over to Builder. Use `code snippets` instead!

## Adding feedback to the Stroop demo
No such thing, need a new routine. Insert within `trials` loop, after the `trial` component. Add code snippet - must have a compatible variable name (no spaces) - I used `checkCorr`.

Builder automatically creates `resp.corr` (through keyboard component). In the `begin routine`, add this code:

``` python
if resp.corr:
    msg = 'Correct'
    msgColor = 'green'
else:
    msg = 'Incorrect'
    msgColor = 'red'
```

Then create a text component (called `feedbackMsg`), and in the text box put `$msg` and the color box put `$msgColor` to show some feedback.

Order of components is important! Make sure you don't overwrite things or set attributes a trial too late.

## BART demo
An example of how far you can take code components.

# General purpose programming
`enumerate` in Python goes through a loop and returns the `n` value as well as the name for each item in a list.

# Resampling statistics (permutation tests)
Don't need to use LUTs or calculate statistics; can do assumption-free tests similar to a t-test. If the means of two groups are the same, they are from the same population. If this is true, we can reproduce this through resampling. When resampling, must keep `group n` the same to avoid false reduction of variance.

If the original values are different to the original values, permutation would make this obvious. To check significance, check overlap of 95% CI. To do this, must sort the resampled mean differences then extract the top and bottom 2.5% (*criterion values*). In the `stats` module, there is a function called `percentileofscore()` which gives percentage likelihood, analogous to p-values.

> How many resamples is enough? No real answer... 5000 is considered OK, but can be tested for optimality by how similar the p-values are each time you run it (still some differences at 100000).

Nonparametric stats version involves rank-ordering and throwing away a whole bunch of information. **Resampling** keeps all of the information, but takes into account the skewed distributions - all the stats with none of the loss of power. Resampling **will** give a different answer to a t-test if the data are non-normal.

Jon often uses resampling stats... Unpaired samples, paired samples (with constraint of it is known which scores go together). Can even do permutation tests for multi-factorial analysis of variance.

Not the sample as bootstrapping, as that allows construction of confidence interval without a hypothesis test (using resampling with replacement rather than shuffling). Read up on this.