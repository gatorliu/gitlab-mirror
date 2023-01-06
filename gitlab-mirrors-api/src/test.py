from git import Repo

if __name__ == '__main__':
    repo = Repo('E:\MyProject\FT\gitlab-mirro')
    print( repo.remotes.origin.fetch(prune=True))
    #print( repo.remotes.origin.pull())
    #print(repo.remotes.origin.push(mirror=True))


    
    
