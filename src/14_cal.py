"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
import argparse
from datetime import datetime

cal = calendar.TextCalendar()
current_time = datetime.now()

parser = argparse.ArgumentParser(description='Render a calendar in the terminal')
parser.add_argument('--month', type=int,
                    help='an integer that represents the months, 1-12 inclusive')
parser.add_argument('--year', type=int,
                    help='an integer that represents the year')

args = parser.parse_args()

print(args.year )

def main():
  if args.year==None and args.month==None:
    return cal.prmonth(current_time.year,current_time.month)
  elif args.year==None and args.month!=None and 1 <= args.month <= 12:
    return cal.prmonth(current_time.year,args.month)
  elif args.year!=None and args.month!=None and 1 <= args.month <= 12:
    return cal.prmonth(args.year,args.month)
  else :
    parser.print_help()

main()