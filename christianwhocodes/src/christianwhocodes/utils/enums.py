"""Core enumeration types used across the package."""

from enum import IntEnum, StrEnum

from .platform import Platform

__all__: list[str] = ["ExitCode", "InitAction", "PostgresFilename"]


class ExitCode(IntEnum):
    """Process exit codes."""

    SUCCESS = 0
    ERROR = 1


class InitAction(StrEnum):
    """Recognised project-initialisation verbs."""

    STARTPROJECT = "startproject"
    INIT = "init"
    CREATE = "create"
    NEW = "new"
    SETUP = "setup"
    BOOTSTRAP = "bootstrap"
    SCAFFOLD = "scaffold"


class PostgresFilename(StrEnum):
    """Platform-dependent PostgreSQL config file names."""

    PGPASS = "pgpass.conf" if Platform().os_name == "windows" else ".pgpass"
    PGSERVICE = ".pg_service.conf"
