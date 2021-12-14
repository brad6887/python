import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy 

def find_CommonTracks(fileNames):
    """
    Find common tracks in given playlist files,
    and save them to common.txt
    """
    # a list of sets of track names
    trackNameSets = []
    for file in fileNames:
        


def findDuplicates(fileName):
    print('Finding duplicate tracks in %s...' % fileName)
    # read in playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks from the Tracks Dictionary
    tracks = plist['Tracks']
    # Create track list dictionary
    trackNames = {}
    # iterate through the tracks
    for trackID, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # Look for existing entries
            if name in trackNames:
                # if a name and duration match, increment the count
                # round the track lenth to the nearest second
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
                else:
                    # add dictionary entry as tuple (duration, count)
                    trackNames[name] = (duration, count+1)
        except:
            # ignore
            pass
                    