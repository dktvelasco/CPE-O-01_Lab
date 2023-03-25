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
    
    
    @patch('builtins.input', side_effect=['invalid', '1', 'invalid', '2', 'q'])
    def test_playGame_invalid_input(self, mock_input):
        game = [[None]*3 for _ in range(3)]
        with patch('oxo_logic.userMove') as mock_user:
            with patch('oxo_logic.computerMove') as mock_computer:
                mock_user.side_effect = ['invalid', None, None, 'X']
                oxo_args_ui.playGame(game)
                mock_user.assert_has_calls([call(game, 0), call(game, 1)])
                mock_computer.assert_called_once_with(game)
    @patch('builtins.input', side_effect=['q'])
    def test_playGame_draw(self, mock_input):
        game = [['O', 'X', 'O'], ['X', 'X', 'O'], ['O', 'O', 'X']]
        with patch('oxo_logic.userMove') as mock_user:
            with patch('oxo_logic.computerMove') as mock_computer:
                result = oxo_args_ui.playGame(game)
                mock_user.assert_not_called()
                mock_computer.assert_not_called()
                self.assertEqual(result, 'D')
    
    
