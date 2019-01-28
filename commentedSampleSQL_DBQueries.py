import sys
# import sys so we can use sys.stdout.write

pstartNum = int(input("Source Port number start: "))
# Asking to have the user (You) enter a start number.

q1 = "SELECT COUNT(*) AS Port_"
# Start of SQL Query, in this case we are getting a count, instead of a display of the values matching the query.

q2 = "FROM [dbo].[zy2016-09]"
# From portion of a SQL Query

qWat = "WHERE [Column 1] like '%:"
# Query for your search criteria.

qClose = "'"
# Close the SQL Query for the like string.

for x in range(100):
# Run this loop 100 times.

    sys.stdout.write("%s%s %s \n" % (q1, pstartNum, q2));
# The left side with %s placement, says grab the 1st part of the Select variable, Current iteration of loop, with a space added for the variable for 'FROM (tablename)'.

    sys.stdout.write("%s%s%s \n" % (qWat, pstartNum, qClose));
# Here the %s triple string placement is to have no spaces.  We call the Query, current iteration of the start number from the loop, and close the line with a "'".

    print("GO")
# Execute each query instead of waiting for all of them to complete.
    
    print()
# prints a blank line.  I saw some crazy code to do this by other means, but since all I want is a blank line, this is way easier and fits the bill.

    pstartNum = pstartNum - 1
# Once the 1st loop finishes, subtract 1 from the starting port number.  Do this for each iteration, by sayin that variable is equal to -1 from it's current state. (Please note you will error if you start with a port number less than 100.)

exit
# stops the 100 loop, so I can copy and paste this into my SQL query window and get results.