import os
import sys
import logging
import pytest
from jproperties import Properties

@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        """
        Creates a logger instance
        :return: Logger instance
        """
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    def getProperties(self, property_file):
        """
        Load properties from a properties file
        :param property_file: Name of the properties file (without .properties extension)
        :return: Properties object
        """
        Root_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(Root_Dir)
        properties_folder = os.path.join(Root_Dir, "config")
        properties_path = os.path.join(properties_folder, "{}.properties".format(property_file))
        
        p = Properties()
        with open(properties_path, 'rb') as property_file:
            p.load(property_file, encoding="utf-8")

        # Check for secrets file
        secrets_path = os.path.join(properties_folder, "secrets.properties")
        if os.path.exists(secrets_path):
            with open(secrets_path, 'rb') as secrets_file:
                p.load(secrets_file, encoding="utf-8")

        return p

    def get_website_url(self):
        """
        Gets the website URL from config
        :return: Website URL
        """
        properties = self.getProperties("opencart")
        return properties.get("website_url").data
