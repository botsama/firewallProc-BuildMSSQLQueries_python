#Dump Queries with start to end port range

import sys

pstartNum = int(input("Source Port number start: "))
q1 = "SELECT COUNT(*) AS Port_"
q2 = "FROM [dbo].[zy2016-09]"
qWat = "WHERE [Column 1] like '%:"
qClose = "'"
for x in range(100):
    sys.stdout.write("%s%s %s \n" % (q1, pstartNum, q2));
    sys.stdout.write("%s%s%s \n" % (qWat, pstartNum, qClose));
    print("GO")
    print()
    pstartNum = pstartNum - 1
exit  ?