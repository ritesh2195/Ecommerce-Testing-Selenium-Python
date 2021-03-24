import configparser

config = configparser.RawConfigParser()

config.read("D://PYTHON//EcommerceAutomationPractice//Configuration//config.ini")


class configReader:

    @staticmethod
    def getURL():

        return config.get('Env', 'URL')

    @staticmethod
    def getExcelPath():

        return config.get('Env', 'ExcelFilePath')

    @staticmethod
    def getDBUser():

        return config.get('SQL', 'user')

    @staticmethod
    def getDBPassword():

        return config.get('SQL', 'password')

    @staticmethod
    def getDBHost():

        return config.get('SQL', 'host')

    @staticmethod
    def getDBName():

        return config.get('SQL', 'database')