from flask import Flask
import pathlib
from logging.handlers import TimedRotatingFileHandler
import logging


def init_logger(server):
    logger = logging.getLogger(__name__)
    log_handler = TimedRotatingFileHandler(server.root_path + server.config["LOG_FILE"],
                                           when=server.config["LOG_WHEN_ROLLOVER"],
                                           interval=server.config["LOG_INTERVAL"],
                                           backupCount=server.config["LOG_BACK_UP_CNT"],
                                           )
    log_handler.setLevel(server.config["LOG_LVL"])
    format_str = "%(asctime)s - PID %(process)d - %(filename)s - %(levelname)s - Session %(uuid)s - %(message)s"
    log_handler.setFormatter(logging.Formatter(format_str))
    logger.addHandler(log_handler)
    return logger


def create_server(config_file):
    root_dir = pathlib.Path(__file__).parent.parent
    server = Flask(__name__, root_path=root_dir.__str__())
    server.config.from_pyfile(root_dir.joinpath(config_file), silent=False)
    server.template_folder = root_dir.__str__() + server.config["HTML_TEMPLATES"]
    server.static_folder = root_dir.__str__() + server.config["STATIC_FOLDER"]
    server.logger = init_logger(server)
    server.logger.debug(server.static_folder)
    with server.app_context():
        import Routes
        server.logger.info("Import Routes")
    return server


if __name__ == "__main__":
    config_file = "website/config/FlaskProperties.py"
    server = create_server(config_file)
    server.run()
