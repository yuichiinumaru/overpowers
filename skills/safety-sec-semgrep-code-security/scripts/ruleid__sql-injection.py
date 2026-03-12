#!/usr/bin/env python3

# ruleid: sql-injection
cursor.execute("SELECT * FROM users WHERE id = " + user_input)

# ok: sql-injection
cursor.execute("SELECT * FROM users WHERE id = %s", (user_input,))
