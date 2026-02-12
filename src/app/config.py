import logging
import os

APP_LOG_CONFIG_FILE = os.path.join(os.path.dirname(__file__), "./log_conf.yml")
APP_LOG_LEVEL = logging.getLevelName(
    os.environ.setdefault("APP_LOG_LEVEL", "INFO").upper()
)

logging.root.setLevel(APP_LOG_LEVEL)
logging.basicConfig(filemode=APP_LOG_CONFIG_FILE)
logging.disable(logging.NOTSET)
logger = logging.getLogger(__name__)


# LIST HERE YOUR CONFIGURATION VARIABLES
APP_HOST = os.environ.setdefault("APP_HOST", "0.0.0.0")
APP_PORT = os.environ.setdefault("APP_PORT", "8000")
APP_CONF_VARIABLE = os.environ.setdefault(
    "APP_CONF_VARIABLE", f"give-here-a-default-value"
)