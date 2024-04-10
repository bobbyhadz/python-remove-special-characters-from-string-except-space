# Remove special characters except Space from String in Python

import re

a_string = 'b!o@b#b$y% h^a&d*z( c.o,m'


new_string = re.sub(r'[^a-zA-Z0-9\s]+', '', a_string)
print(new_string)  # 👉️ 'bobby hadz com'