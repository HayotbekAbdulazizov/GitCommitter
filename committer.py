
from git import Git
from github import Github
import datetime
import time
import random

dct = {
    'hayotbekabdulazizov':'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',
    'hayotbekabdulazizov1':'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',
    'hayotbekabdulazizov2':'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',
    'hayotbekabdulazizov3':'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',
    'hayotbekabdulazizov4':'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',
    'hayotbekabdulazizov5':'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',
    'hayotbekabdulazizov6':'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',
    'hayotbekabdulazizov7pp':'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',
}

print(f"Git profile - hayotbekabdulazizov")
print(f"Git PAT - ")
g = Github(dct['hayotbekabdulazizov6'])


repo = g.get_user().get_repo('Repos1')
try:
    repo.create_file('commit.txt','message from committer.py',"We did it !")
    print(repo,' == CREATED')
except:
    for i in range(25):
        file = repo.get_contents("commit.txt")
        repo.update_file("commit.txt", 'updated msg from committer.py', f"{datetime.datetime.now()}", sha=file.sha)
        print(i)
        time.sleep(0.2)
