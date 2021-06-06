#!/usr/bin/env python3

# =============================================================================
# |<-- Note -->|
# This 5 key vaslue paire log generator python script
# 1.id
# 2.start_datetime
# 3.end_datetime
# 4.MSISDN
# 5.SHORT_CODE
# 6.USER_NAME
# =============================================================================
import datetime
import names
import random

# Extra Minutes Generator
extraMinutes = random.randrange(5, 10)

# Value variables
startDate: datetime = datetime.datetime.now().replace(microsecond=0)
endDate = startDate + datetime.timedelta(minutes=extraMinutes)
MSISDN = random.randrange(771000001, 771000005)
shortCode = random.randrange(110, 120)
userName = names.get_full_name()

# Print The logfile
print("{", "start date:", startDate, ",", "End Date: ", endDate,  ",", "msisdn :", MSISDN, ",", "Short Code :", shortCode, ",", "user name :", userName, "}")

#print("{", "msisdn :", MSISDN, ",", "user name :", userName, "}")

#print('{' "start_date" ':' + startDate + ','  '}')

