import unittest
import command_line_tool as cli
import gzip, shutil, requests


class TestCommandLineTool(unittest.TestCase):
    def setUp(self):
        """ setting up needed files to test a few functions in test_request_data and test_get_data """
        self.csv_name = "test_file.csv"
        self.zipped_csv = "test_file.csv.gz"
        self.response = requests.get(
            "http-link"
        )

        with open(self.csv_name, "rb") as f_in:
            with gzip.open(self.zipped_csv, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

    def tearDown(self):
        cli.clean(self.zipped_csv)

    def test_request_data(self):
        self.assertEqual(
            cli.request_data(
                "http-link"
            ),
            (
                "test_data.csv.gz",
                [100, "28", "51621", "a888a1c57cf6af2ffee687bfdd7dc4c5"],
            ),
        )

        with self.assertRaises(Exception):
            cli.request_data(1)
            cli.request_data(-1)

        with self.assertRaises(Exception):
            cli.request_data(
                "http-link"
            )

        with self.assertRaises(Exception):
            self.cli.request_data(
                "http-link"
            )

        with self.assertRaises(Exception):
            cli.request_data(
                "http-link"
            )

    def test_clean(self):
        f = open("test.txt", "w+")
        f.close()
        self.assertEqual(cli.clean("test.txt"), "file removed")

    def test_get_data(self):

        self.assertEqual(
            cli.get_data(self.zipped_csv),
            [100, "28", "51621", "a888a1c57cf6af2ffee687bfdd7dc4c5"],
        )

        with self.assertRaises(Exception):
            cli.get_data(self.csv_name)

        with self.assertRaises(Exception):
            cli.get_data("cas.p")


if __name__ == "__main__":
    unittest.main()
