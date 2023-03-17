from unittest.mock import patch
import output

def test_number_guessing_game():
    with patch('builtins.input', side_effect=['50', 'quit', 'no']):
        with patch('builtins.print') as mocked_print:
            with patch('random.randint', return_value=42):
                output.number_guessing_game()
                mocked_print.assert_any_call('Too high! Guess lower.')
                mocked_print.assert_any_call('Farewell! The correct number was 42.')

    with patch('builtins.input', side_effect=['30', '42', 'no']):
        with patch('builtins.print') as mocked_print:
            with patch('random.randint', return_value=42):
                output.number_guessing_game()
                mocked_print.assert_any_call('Too low! Guess higher.')
                mocked_print.assert_any_call('Congratulations! You guessed the correct number 42 in 2 attempts.')