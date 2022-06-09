
from git import Git
from github import Github
import datetime
import time
import random


from main.models import  GitProfile, Repository

MESSAGE_LIST = [
    'Changed Models F', 'Fixed Bug in models F ', 'Model field alternation F', 'Changed Model Function F',
    'Some changes in views  F', 'Views bug is solved F',
    'Cleared and restored because of unsolved issue F ','Cleared all files F ',
    'Preparing to add some api to models F', 
    'Appered bugs in urls F',
]






def schedule_api():
    GitProfile.objects.create(username='me', pat='me', full_name = 'men')
    
    for x in GitProfile.objects.all():
        print(f"Git profile - {x.username}")
        print(f"Git PAT - {x.pat}")
        g = Github(x.pat)
        times = random.randrange(15, 25)
        print(f"Times - {times}")
        time.sleep(0.5)


        for i in range(times):
            repo = g.get_user().get_repo(x.repos.order_by("?").first().name)
            print( 'REPO = ',repo)
            try:
                repo.create_file('commit.txt', random.choice(MESSAGE_LIST),"We did it !")
                print(repo,' == CREATED')
            except:
                file = repo.get_contents("commit.txt")
                repo.update_file("commit.txt", random.choice(MESSAGE_LIST), f"{datetime.datetime.now()}", sha=file.sha)
                time.sleep(1)
                print(repo,' == UPDATED')
        print("====================", x.username, 'is done ')    

    return True




def helloer():
    GitProfile.objects.create(username='me', pat='me', full_name = 'men')
    print('GitProfile Created')
    return True