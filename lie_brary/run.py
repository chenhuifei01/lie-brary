'''
Run the app or the getdata script, depending on the input provided
- To run the dashboard, type "python -m lie_brary dashboard"
- To run update data, type "python -m lie_brary getdata"

# Author: Reza R Pratama
'''

import sys
from lie_brary import app
from lie_brary.scripts import getdata

def run_dash():
    '''Run the dash app'''
    app.app.run_server(debug=True, port=8051)

def run_getdata():
    '''Run the getdata script'''
    getdata.getdata()


message = ('To run the dashboard, type "python -m lie_brary dashboard" | '
            'To run update data, type "python -m lie_brary getdata"')


def main():
    '''Run the app or the getdata script, depending on the input provided'''
    if len(sys.argv) > 1:
        if sys.argv[1] == 'dashboard':
            run_dash()
        elif sys.argv[1] == 'getdata':
            run_getdata()
        else:
            print("[Invalid Input Provided] " + message )
    else:
        print("[No Input Provided] " + message)
