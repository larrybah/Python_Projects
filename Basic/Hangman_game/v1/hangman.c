#include <stdio.h>
/**
 * Hangman game (word guessing game).
 * We create an array of words and
 * ask the user to guess a word we have in the array.
 *
 * main - entry point of the program.
 */

char start_game();
int guessed_result();

int main(void)
{
	char words[4][15] = {"Beauty", "Salutation", "Love", "Developer"};
	start_game();

	//test
	for (int i = 0; i < 4; i++)
	{
		printf("\n%s\n", words[i]);
	}
	return (0);
}

/**
 * start_game - starts the game and welcome players
 *
 */
char start_game()
{
	printf("Welcome to the Hangman game...\n");
	printf("Guess the right word\n");
	printf("You have three guesses\n");
}
