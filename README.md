# Class RPG


## Development Setup
1. Fork the [main repository](https://github.com/ICS4U-Gallo/class-rpg-game) on GitHub.
2. Clone the repo from GitHub.
    ```sh
    git clone https://github.com/<YOUR USENAME>/class-rpg-game.git
    ```
3. `cd` into the directory
    ```sh
    cd class-rpg-game
    ```
4. Add original repository to your git remote under the name `upstream`.
    ```sh
    git remote -v
    git remote add upstream https://github.com/ICS4U-Gallo/class-rpg-game.git
    git remote -v
    ```
5. Install Poetry and project dependancies (optional). You at least need to ensure you have `pygame` and `pytest` installed on your system.
    ```sh
    pip install poetry
    poetry install
    ```

## Everyday Development
1. Pull in main repository changes and fix any merge conflicts. This depends on step 4 from Development Setup. If there are issues, they will most likely be in the `git merge` part. Just ask the teacher for help or google "how to git merge". 
    ```sh
    git fetch upstream
    git checkout main
    git merge upstream/main
    git push origin main
    ```
2. Make changes to your code.
3. Commit the changes to your code.
    ```sh
    git add -A
    git commit -m "Enter a commit message here"
    git push
    ```

If your code works, consider opening a pull request on GitHub.com from your forked repo.

### Running the game
In the game's root directory, type:
```sh
$ python -m rpg
```
Or if it tells you do not have cetrain dependancies (and you installed poetry):
```sh
poetry run python -m rpg
```

