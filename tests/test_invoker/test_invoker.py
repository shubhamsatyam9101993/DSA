from unittest import mock
from src.invoker import Invoker
from tests.facade_fixtures import FacadeFixtures
from pathlib import Path


class TestInvoker(FacadeFixtures):

    @property
    def get_path(self):
        return str(Path().absolute()).split("src")[0]+"/hello.csv"

    @staticmethod
    def get_invoker_obj():
        return Invoker()

    @mock.patch("src.invoker.Invoker.write_df")
    @mock.patch("src.invoker.Invoker.read_csv")
    def test_invoker_read_csv(self, mock_read, mock_write):
        mock_read.return_value = self.data_set
        mock_write.return_value = None
        self.get_invoker_obj().do()
        mock_write.assert_called_once()
