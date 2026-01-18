import logging

class Log_Maker():

    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=".\\logs\\nopcommerce.log",
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.INFO,
            force=True
        )
        return logging.getLogger()
