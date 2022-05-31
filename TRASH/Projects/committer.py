from git import Repo
import random
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


REPOSITORY_LIST = [
    '/Projects/Destry/.git',
    '/Projects/DRF-Introduction/.git',
    '/Projects/HayotbekAbdulazizov/.git',
]

MESSAGE_LIST = [
    'Changed Models F', 'Fixed Bug in models F ', 'Model field alternation F', 'Changed Model Function F',
    'Some changes in views  F', 'Views bug is solved F',
    'Cleared and restored because of unsolved issue F ','Cleared all files F ',
    'Preparing to add some api to models F', 
    'Appered bugs in urls F',
]








def git_push():
    RANDOM_REPOSITORY = random.choice(REPOSITORY_LIST)
    PATH_OF_GIT_REPO = f'{BASE_DIR}{RANDOM_REPOSITORY}'  # make sure .git folder is properly configured
    COMMIT_MESSAGE = f"{random.choice(MESSAGE_LIST)} {RANDOM_REPOSITORY}"

    try:
        print('ZERO step')
        repo = Repo(PATH_OF_GIT_REPO)
        print('1 step')
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    




# import time
# for  i in range(1,50):
git_push()
    # time.sleep(0.2)