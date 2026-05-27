from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class IOCType(str, Enum):
    IP = "ip"
    DOMAIN = "domain"
    URL = "url"
    MD5 = "md5"
    SHA1 = "sha1"
    SHA256 = "sha256"
    PROCESS = "process"


@dataclass
class LogEvent:
    timestamp: datetime
    source: str
    level: LogLevel
    message: str
    raw: str


@dataclass
class NetworkEvent:
    timestamp: datetime
    src_ip: str
    dst_ip: str
    src_port: int
    dst_port: int
    protocol: str
    size: int


@dataclass
class Alert:
    id: str
    type: str
    severity: Severity
    source: str
    timestamp: datetime
    detail: str


@dataclass
class ProcessEvent:
    pid: int
    ppid: int
    name: str
    cmdline: str
    user: str
    start_time: datetime
    exe_path: str


@dataclass
class FileEvent:
    event_type: str  # modified | deleted | created
    path: str
    timestamp: datetime
    expected_hash: str | None = None
    actual_hash: str | None = None


@dataclass
class ConnectionEvent:
    timestamp: datetime
    local_addr: str
    remote_addr: str
    status: str
    pid: int
    process_name: str


@dataclass
class IOCMatch:
    ioc_type: IOCType
    ioc_value: str
    matched_in: str
    context_line: str
    timestamp: datetime


@dataclass
class SIEMIncident:
    incident_id: str
    correlation_key: str
    severity: Severity
    first_seen: datetime
    last_seen: datetime
    event_count: int
    events: list = field(default_factory=list)
