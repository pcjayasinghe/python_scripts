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
import json

# Extra Minutes Generator
extraMinutes = random.randrange(5, 10)

# Value variablesvim 
startDate = datetime.datetime.now().replace(microsecond=0)
endDate = startDate + datetime.timedelta(minutes=extraMinutes)
MSISDN = random.randrange(771000001, 771000005)
shortCode = random.randrange(110, 120)
userName = names.get_full_name()

# Print The logfile
randomLog = {'start date': str(startDate), 'End Date': str(endDate), 'msisdn': MSISDN, 'Short Code': shortCode, 'user name': userName}
print(randomLog)

# Loop log file printing
i = 0
while i < 10:
    print(randomLog)
    i += 1




