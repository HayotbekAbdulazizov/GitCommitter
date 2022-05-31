import requests
import time
from pathlib import Path
from git import Repo
import random
from pathlib import Path




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








# def git_push():
# 	RANDOM_REPOSITORY = random.choice(REPOSITORY_LIST)
# 	RANDOM_MESSAGE = random.choice(MESSAGE_LIST)

# 	PATH_OF_GIT_REPO = f"{BASE_DIR}{RANDOM_REPOSITORY}"  # make sure .git folder is properly configured
# 	COMMIT_MESSAGE = f"{RANDOM_MESSAGE} {RANDOM_REPOSITORY}"
# 	try:
# 		print('ZERO step')
# 		print(f'{BASE_DIR}{RANDOM_REPOSITORY}')
# 		print(RANDOM_MESSAGE)
# 		print('1 step')






# 		# repo = Repo(PATH_OF_GIT_REPO)
# 		repo = Repo('/home/hayotbek/Documents/GitHub/GitPython/GitCommitter/Projects/HayotbekAbdulazizov/.git')
# 		repo.git.add(update=True)
# 		# repo.index.commit(COMMIT_MESSAGE)
# 		repo.index.commit('Message')
# 		origin = repo.remote(name='origin')
# 		origin.push()
# 		print(RANDOM_REPOSITORY, '---', RANDOM_MESSAGE)
# 	except:
# 		print('====== Some error occured while pushing the code =======')    






def schedule_api():

	RANDOM_REPOSITORY = random.choice(REPOSITORY_LIST)
	RANDOM_MESSAGE = random.choice(MESSAGE_LIST)

	PATH_OF_GIT_REPO = f"{BASE_DIR}{RANDOM_REPOSITORY}"  # make sure .git folder is properly configured
	COMMIT_MESSAGE = f"{RANDOM_MESSAGE} {RANDOM_REPOSITORY}"


	print('ZERO step')
	repo = Repo(f'{BASE_DIR}{RANDOM_REPOSITORY}')
	repo.git.add(update=True)
	repo.index.commit(RANDOM_MESSAGE)
	origin = repo.remote(name='origin')
	origin.push()
	print('1 step')
	print(f"Repos:{RANDOM_REPOSITORY} \n Dir:{BASE_DIR} \n BDIR: {BASE_DIR, RANDOM_REPOSITORY} \n Message:{RANDOM_MESSAGE}" )

	return True































# 	https://localazy.com/my/community