from Utilities.ConfigReader import configReader
from Utilities.ExcelReader import *


def getData():
    path = configReader.getExcelPath()

    rows = getRowCount(path, 'login1')

    print(rows)

    columns = getColumnCount(path, 'login1')

    print(columns)

    email = []

    password = []

    # result = []

    for r in range(2, rows + 1):
        email.insert(r, readData(path, 'login1', r, 1))

    print(email)

    for s in range(2, rows + 1):
        password.insert(s, readData(path, 'login1', s, 2))

    print(password)

    """for t in range(2, rows + 1):
        result.insert(t, readData(path, 'login1', t, 3))"""

    data = list(zip(email, password))

    return data
