import unittest

from py_vor.QueryRunner import QueryRunner
from py_vor.tools.get_secret import get_secret


class QueryRunnerTest(unittest.TestCase):

    def test_mysql_select_query(self):
        secret = get_secret('ksco92-MySQL-Secret')

        runner = QueryRunner(secret['engine'], secret['host'], secret['port'], secret['username'], secret['password'],
                             secret['dbname'], 'queries/select_user.sql', returns_rows=True, include_headers=False)

        results = runner.execute_all()

        expected = [['10001', '1953-09-02', 'Georgi', 'Facello', 'M', '1986-06-26']]

        assert results == expected


if __name__ == "__main__":
    QueryRunnerTest()
