import os
import unittest

from py_vor.tools.download_from_s3 import download_from_s3


class S3Test(unittest.TestCase):

    def test_download(self):
        bucket_name = 'ksco92'
        file_name = 'defiant.sql'

        download_from_s3(file_name, bucket_name, '')

        files = [f for f in os.listdir('.') if os.path.isfile(f)]

        is_downloaded = True if file_name in files else False

        assert is_downloaded

        os.remove(file_name)


if __name__ == "__main__":
    S3Test()
