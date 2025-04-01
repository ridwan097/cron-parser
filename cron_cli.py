import sys


DATE_RANGES= {
    "minute": range(0, 60),
    "hour": range(0, 24),
    "day of month": range(1, 32),
    "month": range(1, 13),
    "day of week": range(0, 7),
}

def expand_cron_field(field_expression, field_name):
    cron_parts = field_expression.split(',')
    values = set()
    valid_range = DATE_RANGES[field_name]

    for part in cron_parts:
        if part == '*':
            values.update(valid_range)
        elif part.startswith('*/'):
            step = int(part[2:])
            values.update(valid_range[::step])
        elif '-' in part:
            start, end = map(int, part.split('-'))
            values.update(range(start, end + 1))
        else:
            values.add(int(part))

    return sorted(values)


def parse_cron(value):
    fields = value.split()
    if len(fields)!= 6:
        sys.exit("Invalid cron format. Expected 6 fields: minute hour day_of_month month day_of_week command")
    
    minute, hour, day_of_month, month, day_of_week = fields[:5]
    
    command = ' '.join(fields[5:])
    
    minute_range = expand_cron_field(minute, "minute")
    hour_range = expand_cron_field(hour, "hour")
    day_of_month_range = expand_cron_field(day_of_month, "day of month")
    month_range = expand_cron_field(month, "month")
    day_of_week_range = expand_cron_field(day_of_week, "day of week")
    
    return minute_range, hour_range, day_of_month_range, month_range, day_of_week_range, command
            
            
def show_schedule(cron_details):
    for field in ["minute", "hour", "day of month", "month", "day of week"]:
        print(f"{field.ljust(14)}{' '.join(map(str, cron_details[field]))}")
    print(f"{'command'.ljust(14)}{cron_details['command']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python schedule.py <cron_expression>")
        sys.exit(1)
    
    data = sys.argv[1]
    try:
        parsed_cron = parse_cron(data)
        cron_details = {
            "minute": parsed_cron[0],
            "hour": parsed_cron[1],
            "day of month": parsed_cron[2],
            "month": parsed_cron[3],
            "day of week": parsed_cron[4],
            "command": parsed_cron[5],
        }
        show_schedule(cron_details)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    
    
if __name__ == "__main__":
    main()

    