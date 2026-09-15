import datetime

try:
    today = datetime.datetime.now()
    epoch = datetime.datetime.fromtimestamp(0)

    formated_today = today.strftime("%b %-d %Y")
    formated_epoch = epoch.strftime("%B %-d, %Y")

    delta = today - epoch
    delta_in_seconds = delta.total_seconds()

    seconds_formated = f"{delta_in_seconds:,.4f}"
    scientific_notation = "{:.2e}".format(delta_in_seconds)
    print(f"Seconds since {formated_epoch}: {seconds_formated} or \
{scientific_notation} in scientific notation")
    print(formated_today)
except Exception as e:
    print(f"Error: {e}")
