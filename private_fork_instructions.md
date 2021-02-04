# Creating a Private Fork of this Repo
stough, 202-

Incredibly grateful for [this post](https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274) solving the problem on a different repo.

This repo is public and Github does not allow the creation of private forks for public repositories.

The correct way of creating a private fork by duplicating the repo is documented here.

1. **Create a bare clone of the repository. (This is temporary and will be removed so just do it wherever.)**
```
git clone --bare git@github.com:joshuastough/imageprocessing.git
```

2. **Create a new private repository on Github and name it `my_imageprocessing`.**
> If for some reason you are unable to create a private repo, you can request unlimited private repos as a student by getting the [student pack from Github](https://education.github.com/pack).

3. **Mirror-push your bare clone to your new `my_imageprocessing` repository.**
> Replace `<your_username>` with your actual Github username in the url below.
```
cd imageprocessing.git/
git push --mirror git@github.com:<your_username>/my_imageprocessing.git
```

4. **Remove the temporary local repository you created in step 1.**
```
cd ..
rm -rf imageprocessing.git/
```

5. **You can now clone your `my_imageprocessing` repository on your machine (in my case in the workspace folder).**
```
cd ~/workspace
git clone git@github.com:<your_username>/my_imageprocessing.git
```

6. **You should add the original repo as remote to fetch (potential) future changes. Make sure you also disable push on the remote (as you are not allowed to push to it anyway).**
```
cd my_imageprocessing/
git remote add upstream git@github.com:joshuastough/imageprocessing.git
git remote set-url --push upstream DISABLE
```
> You can list all your remotes with `git remote -v`. You should see:
```
origin  git@github.com:<your_username>/my_imageprocessing.git (fetch)
origin  git@github.com:<your_username>/my_imageprocessing.git (push)
upstream        git@github.com:joshuastough/imageprocessing.git (fetch)
upstream        DISABLE (push)
```
> When you push, do so on origin with `git push origin`
> When you want to pull changes from `upstream` you can just fetch the remote and rebase on top of your work.
```
git fetch upstream
git rebase upstream/main
```
