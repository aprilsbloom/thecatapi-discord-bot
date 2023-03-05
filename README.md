# The Cat API Discord bot

Discord bot written in Python to utilize [TheCatAPI](https://thecatapi.com/) to fetch GIFs, images, and information about various breeds. I also utilize [Reddit's public subreddit endpoint](https://www.reddit.com/r/IllegallySmolCats.json?sort=hot&t=day&limit=100) to scrape videos. Unfortunately, links from that endpoint are without sound, but I will most likely add support for that in the future.

## Installation

This bot requires an API key from TheCatAPI, as well as a Discord token.

After you have gotten the API key from TheCatAPI, open `utils.py` and put the API key into the array named `keyList`.

Next, set the Discord token to the `token` variable.

You can then run `main.py` to launch the bot.

## Commands

- Gif
  - This command allows you to fetch a random cat gif.

- Image
  - This command allows you to fetch a random cat image. It takes an optional argument for the Breed ID, which can show you images of a specific breed.
  - You can fetch a list of Breed IDs that work with the bot by running `/breeds` and selecting `List` from the dropdown.

- Fact
  - This command fetches a random fact about cats. I used [my own collection of cat facts](https://gist.githubusercontent.com/paintingofblue/657d0c4d1202374889ce4a98a6b7f35f/raw/catfacts.txt) for this command.

- Video
  - This command fetches a random video from a [list of subreddits](https://github.com/paintingofblue/thecatapi-discord-bot/blob/main/API.py#L7). It shows the information about the post, such as the title, who posted it, the subreddit it was posted in and the post link.

- Breeds
  - This command has 2 different arguments. It can be used to show a description of your chosen breed, to show statistics about your breed, as well as list all supported breeds by the bot.
  - Information
    - Using the Breed ID `acur` to fetch information about the American Curl provides us with the following information

    <!-- markdownlint-disable-next-line no-inline-html -->
    <img style="width: 25%;" src="https://user-images.githubusercontent.com/90877067/209638911-d472e143-e587-4204-ab6f-9868d5757426.png">

  - Statistics
    - Using the Breed ID `acur` to fetch statistics about the American Curl provides us with the following information

    <!-- markdownlint-disable-next-line no-inline-html -->
    <img style="width: 25%;" src="https://user-images.githubusercontent.com/90877067/209639566-cb087fc9-1139-4444-88fb-3ad9caf4a983.png">

  - List
    - Running this command with the `List` argument shows us a list of 4 letter codes we can use with the bot.

    <!-- markdownlint-disable-next-line no-inline-html -->
    <img style="width: 25%;" src="https://user-images.githubusercontent.com/90877067/209639799-ff3489e7-0e84-4bdd-b790-8044894380e9.png">

- Schedule
  - This command allows you to add a Discord webhook to the hourly cat photo schedule I've created. It features 3 arguments, which allow you to either add a webhook, remove it, or view the current webhook added to the schedule.

- Help
  - This command basically sends a short version of this.
