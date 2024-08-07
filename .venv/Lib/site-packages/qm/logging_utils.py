import sys
import logging

from qm.user_config import UserConfig


def config_loggers(user_config: UserConfig) -> None:
    package_logger = logging.getLogger("qm")
    if user_config.enable_user_stdout:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(user_config.default_logging_format))
        package_logger.addHandler(handler)
        package_logger.setLevel(user_config.logging_level)
    if user_config.upload_logs and user_config.datadog_token:
        if not user_config.user_token:
            raise ValueError("No user token is defined")
        from qm.datadog_api import DatadogHandler

        package_logger.addHandler(
            DatadogHandler(
                user_id=user_config.user_token,
                organization=user_config.organization,
                user_token=user_config.datadog_token,
                session_id=str(user_config.SESSION_ID),
            )
        )


def set_logging_level(level: int) -> None:
    """Sets the logging level of the qm-qua module ("qm")
    See `Messages control <https://qm-docs.qualang.io/guides/error#messages-control>`__ for more information.

    Args:
        level: A string of either: 'DEBUG', 'INFO', 'WARNING', or
            'ERROR'. Can also accept standard python logging levels.
    """
    package_logger = logging.getLogger("qm")
    try:
        package_logger.setLevel(level)
    except (ValueError, TypeError):
        package_logger.warning(f"Failed to set log level. level '{level}' is not recognized")
