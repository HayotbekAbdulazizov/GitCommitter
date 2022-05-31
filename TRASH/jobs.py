from git import Repo

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
	PATH_OF_GIT_REPO = f"/home/hayotbek/Documents/GitHub/GitPython/TRASH/Projects/Destry/.git"  # make sure .git folder is properly configured
	COMMIT_MESSAGE = f"message"
	try:
		print('ZERO step')
		print('1 step')
		repo = Repo(PATH_OF_GIT_REPO)
		repo.git.add(update=True)
		repo.index.commit('Message')
		origin = repo.remote(name='origin')
		origin.push()
	except:
		print('====== Some error occured while pushing the code =======')    






git_push()
