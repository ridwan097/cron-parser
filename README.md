# Cron Expression Parser

This is a command-line tool that parses a cron expression and outputs the expanded values for each time field.

## Requirements

- Python 3.11+ **or**
- Docker (recommended for easy execution)

### Running With Python

```bash
python cron_cli.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

### Running With Docker

1. Build the Docker image:

```bash
docker build -t cron-cli .
```

2. Run the image with a cron expression:

```bash
docker run --rm cron-cli "*/15 0 1,15 * 1-5 /usr/bin/find"
```

The output should be:

| Field        | Values                     |
| ------------ | -------------------------- |
| minute       | 0 15 30 45                 |
| hour         | 0                          |
| day of month | 1 15                       |
| month        | 1 2 3 4 5 6 7 8 9 10 11 12 |
| day of week  | 1 2 3 4 5                  |
| command      | /usr/bin/find              |
