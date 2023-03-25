import unittest
from unittest.mock import patch
import io
import oxo_args_ui
class TestOXOArgsUI(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'q'])
    def test_playGame_quit(self, mock_input):
        game = [[None]*3 for _ in range(3)]
        with patch('oxo_logic.saveGame') as mock_save:
            with patch('sys.exit') as mock_exit:
                oxo_args_ui.playGame(game)
                mock_save.assert_called_once_with(game)
                mock_exit.assert_called_once()
