#!/usr/bin/env python3

import sys
from errorTestTools import *

exCode = runTests({
# "0. Valid INIT"     : ["0 0.0 0.0 0.0 0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","7.0e9","7.0e9","7.0e9"],
  "1. Empty Line"     : ["\t\t\t\t","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","7.0e9","7.0e9","7.0e9"],
  "2. Wrong Type"     : ["0.0 0.0 0.0 0.0 0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","7.0e9","7.0e9","7.0e9"],
  "3. Invalid 'itra'" : ["-1 0.0 0.0 0.0 0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","7.0e9","7.0e9","7.0e9"],
  "4. Invalid 'iver'" : ["0 0.0 0.0 0.0 -1","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","7.0e9","7.0e9","7.0e9"],
  "5. Too Many Lines" : ["0 0.0 0.0 0.0 0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","7.0e9","7.0e9","7.0e9","Oops"],
},sys.argv,10,6)

sys.exit(exCode)
