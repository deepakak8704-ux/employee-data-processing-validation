import logging


logging.basicConfig(
    filename="output/application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)