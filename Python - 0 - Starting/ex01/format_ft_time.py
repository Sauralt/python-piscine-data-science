from datetime import datetime

now = datetime.now()
epoch = datetime(1970, 1, 1)
seconds = (now - epoch).total_seconds()

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(now.strftime("%b %-d %Y"))
