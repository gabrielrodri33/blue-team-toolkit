from dataclasses import dataclass
from datetime import datetime
import re


@dataclass
class LogEntry:
    timestamp: str
    source: str
    level: str
    message: str
    raw: str


SYSLOG_PATTERN = re.compile(
    r"^(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+"
    r"(?P<source>\S+)\s+"
    r"(?P<message>.+)$"
)


def parse_log(file_path):
    parsed_logs = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                level = "INFO"

                if "error" in line.lower():
                    level = "ERROR"

                elif "warning" in line.lower():
                    level = "WARNING"

                match = SYSLOG_PATTERN.match(line)

                if match:
                    timestamp = match.group("timestamp")
                    source = match.group("source")
                    message = match.group("message")
                else:
                    timestamp = str(datetime.now())
                    source = file_path
                    message = line

                entry = LogEntry(
                    timestamp=timestamp,
                    source=source,
                    level=level,
                    message=message,
                    raw=line
                )

                parsed_logs.append(entry)

            except Exception as error:
                print(f"[WARNING] Failed to parse line: {line}")
                print(error)

    return parsed_logs


if __name__ == "__main__":
    logs = parse_log("sample.log")

    for log in logs:
        print(log)