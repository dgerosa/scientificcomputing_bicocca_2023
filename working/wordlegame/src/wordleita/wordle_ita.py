import random
import requests
from datetime import datetime, timedelta
from typing import List, Dict

ATTEMPTS: int = 6
"""Number of attempts."""
WORD_LENGTH: int = 5
"""Length of words."""
URL: str = (
    "https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/660000_parole_italiane.txt"
)
"""URL to retrieve a list of words."""
COLORS: Dict[str, str] = {
    "default": "\033[0m",
    "black": "\033[30m",
    "yellow": "\033[43m",
    "green": "\033[42m",
}
"""Dictionary to define a more clear game experience."""


class Wordle:
    """
    The Wordle class manages the game, where the player has to guess a 5-letter word
    within 6 attempts. The target word is selected deterministically based on the current date.
    """

    def __init__(self):
        """
        Initializes the Wordle class by loading the list of words, selecting the target word,
        and setting the number of available attempts.
        """
        self.words_list = self.load_words()
        self.target_word = self.select_target_word()
        self.attempts = ATTEMPTS

    def select_target_word(self) -> str:
        """
        Selects the target word for the game based on the number of days since January 1, 2020.
        This ensures the word is deterministic for each specific day.

        Returns:
            str: The selected target word.
        """
        today = datetime.now().date()
        epoch = datetime(2020, 1, 1).date()
        days_since_epoch = (today - epoch).days

        random.seed(days_since_epoch)
        return random.choice(self.words_list)

    def play(self) -> None:
        """
        Manages the main flow of the game. Prompts the player to enter guesses, provides feedback
        on each attempt, and displays a message of victory or defeat. Also, shows the time remaining
        until the next word is available.
        """
        print(
            "Benvenuto a Wordle! Hai 6 tentativi per indovinare la parola di 5 lettere.\n"
        )
        guess = ""
        for attempt in range(self.attempts):
            while True:
                guess = input(f"Tentativo {attempt + 1}/{self.attempts}: ").lower()
                if len(guess) == 5 and guess.isalpha():
                    break
                print("Inserisci una parola valida di 5 lettere.")

            if guess == self.target_word:
                print(f"{COLORS['green']}{COLORS['black']}{guess}{COLORS['default']}")
                if attempt + 1 == 1:
                    print(
                        f"\nCongratulazioni! Hai indovinato la parola in {attempt + 1} tentativo!"
                    )
                else:
                    print(
                        f"\nCongratulazioni! Hai indovinato la parola in {attempt + 1} tentativi!"
                    )
                break
            else:
                self.response(guess, self.target_word)

        if guess != self.target_word:
            print(
                f"\nMi dispiace, hai esaurito i tentativi. La parola era '{self.target_word}'."
            )

        remaining_time = self.time_next_word(datetime.now())
        print(
            f"\nTempo rimanente per la prossima parola: {self.format_time(remaining_time)}."
        )

    @staticmethod
    def load_words() -> List[str]:
        """
        Loads the list of words from the specified URL and filters only the 5-letter words.

        Returns:
            List[str]: A list of 5-letter words.
        """
        response = requests.get(URL)
        text = response.text
        words = text.splitlines()
        return [word for word in words if len(word) == WORD_LENGTH]

    @staticmethod
    def response(guess: str, target: str) -> None:
        """
        Generates and prints feedback for a guess. Each letter is colored to indicate if it is correct
        (green), present in the word but in the wrong position (yellow), or absent (no color).

        Args:
            guess (str): The player's guessed word.
            target (str): The target word to be guessed.
        """
        result: List[str] = [" "] * len(guess)
        target_counts: Dict[str, int] = {}

        for char in target:
            target_counts[char] = target_counts.get(char, 0) + 1

        for i in range(len(guess)):
            if guess[i] == target[i]:
                result[i] = (
                    f"{COLORS['green']}{COLORS['black']}{guess[i]}{COLORS['default']}"
                )
                target_counts[guess[i]] -= 1

        for i in range(len(guess)):
            if result[i] == " ":
                if guess[i] in target_counts and target_counts[guess[i]] > 0:
                    result[i] = (
                        f"{COLORS['yellow']}{COLORS['black']}{guess[i]}{COLORS['default']}"
                    )
                    target_counts[guess[i]] -= 1
                else:
                    result[i] = guess[i]

        print("".join(result))

    @staticmethod
    def time_next_word(now: datetime) -> timedelta:
        """
        Calculates the time remaining until midnight, when the next word is selected.

        Args:
            now (datetime): The current datetime.

        Returns:
            timedelta: The time remaining until midnight.
        """
        next_midnight = datetime.combine(
            now.date() + timedelta(days=1), datetime.min.time()
        )
        return next_midnight - now

    @staticmethod
    def format_time(remaining_time: timedelta) -> str:
        """
        Formats a timedelta object into a readable string showing hours, minutes, and seconds.

        Args:
            remaining_time (timedelta): The time remaining.

        Returns:
            str: A formatted string displaying the time remaining.
        """
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours} ore, {minutes} minuti, {seconds} secondi"


if __name__ == "__main__":
    game = Wordle()
    game.play()

