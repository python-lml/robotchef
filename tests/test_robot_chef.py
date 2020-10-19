import sys

from mock import patch
from io import StringIO


@patch("sys.stdout", new_callable=StringIO)
def test_peking_duck(stdout):
    arguments = ["robotchef", "Peking Duck"]
    from robotchef.main import main

    with patch.object(sys, "argv", arguments):
        main()
        assert stdout.getvalue() == "I can roast Peking Duck\n"
