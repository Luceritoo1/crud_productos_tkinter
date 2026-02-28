import logging


def configurar_logging():
    logging.basicConfig(
        filename="sistema.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def registrar_info(mensaje):
    logging.info(mensaje)


def registrar_error(mensaje):
    logging.error(mensaje)