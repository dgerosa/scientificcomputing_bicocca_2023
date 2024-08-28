from unittest.mock import patch
from wordleita import Wordle
from datetime import datetime, timedelta
from typing import List


@patch("requests.get")
def test_load_words(mock_get) -> None:
    """
    Test the 'load_words' method of the Wordle class.
    This test checks if the method correctly loads and filters a list of 5-letter words.

    Args:
        mock_get (Mock): The mock object for 'requests.get'.
    """
    mock_get.return_value.text = "apple\nbread\ncrane\n"

    wordle: Wordle = Wordle()
    words_list: List[str] = wordle.load_words()

    assert len(words_list) == 3
    assert "apple" in words_list
    assert "bread" in words_list
    assert "crane" in words_list


@patch("random.choice")
@patch("datetime.datetime")
def test_select_target_word(mock_datetime, mock_choice) -> None:
    """
    Test the 'select_target_word' method of the Wordle class.
    This test checks if the method correctly selects a word based on the date and the list of words.

    Args:
        mock_datetime (Mock): The mock object for 'datetime.datetime'.
        mock_choice (Mock): The mock object for 'random.choice'.
    """
    mock_datetime.now.return_value.date.return_value = datetime(2024, 8, 28).date()
    mock_choice.return_value = "apple"

    wordle: Wordle = Wordle()
    wordle.words_list = ["apple", "bread", "crane"]
    target_word: str = wordle.select_target_word()

    assert target_word == "apple"


@patch("datetime.datetime")
def test_time_next_word(mock_datetime) -> None:
    """
    Test the 'time_next_word' method of the Wordle class.
    This test checks if the method correctly calculates the time remaining until midnight.

    Args:
        mock_datetime (Mock): The mock object for 'datetime.datetime'.
    """
    mock_datetime.now.return_value = datetime(2024, 8, 28, 10, 0, 0)

    wordle: Wordle = Wordle()

    current_time: datetime = mock_datetime.now()
    remaining_time: timedelta = wordle.time_next_word(current_time)
    next_midnight: datetime = datetime.combine(
        datetime(2024, 8, 29), datetime.min.time()
    )
    expected_remaining_time: timedelta = next_midnight - datetime(2024, 8, 28, 10, 0, 0)

    assert remaining_time.days == expected_remaining_time.days
    assert remaining_time.seconds == expected_remaining_time.seconds


def test_format_time() -> None:
    """
    Test the 'format_time' method of the Wordle class.
    This test checks if the method correctly formats a timedelta object into a readable string.
    """
    wordle: Wordle = Wordle()
    remaining_time: timedelta = timedelta(hours=2, minutes=15, seconds=30)
    formatted_time: str = wordle.format_time(remaining_time)

    assert formatted_time == "2 ore, 15 minuti, 30 secondi"

