"""Central MySQL connection helper.

Database credentials are read from the environment so that they are never
committed to source control. Copy ``.env.example`` to ``.env`` and fill in the
real values, or export the variables in your shell before starting the app.
"""

import os

import mysql.connector

# Optional convenience: load a local .env file when python-dotenv is installed.
# The app works without it as long as the variables are exported in the shell.
try:  # pragma: no cover - purely a developer convenience
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # noqa: BLE001 - dotenv is optional
    pass


DB_HOST = os.environ.get("MYSQL_HOST", "localhost")
DB_USER = os.environ.get("MYSQL_USER", "root")
DB_NAME = os.environ.get("MYSQL_DATABASE", "facialrecognition")
DB_AUTH_PLUGIN = os.environ.get("MYSQL_AUTH_PLUGIN", "mysql_native_password")


def get_connection():
    """Return a new MySQL connection built from environment variables.

    Raises:
        RuntimeError: if ``MYSQL_PASSWORD`` is not configured.
    """
    password = os.environ.get("MYSQL_PASSWORD")
    if password is None:
        raise RuntimeError(
            "MYSQL_PASSWORD is not set. Copy .env.example to .env and provide "
            "the database password (or export MYSQL_PASSWORD) before running "
            "the application."
        )

    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=password,
        database=DB_NAME,
        auth_plugin=DB_AUTH_PLUGIN,
    )
