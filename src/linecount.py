# Copyright (C) 2015 Zach Ohara
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import github3 as github

def main():
	session = promptLogin()
	accountname = promptGetUser()
	numRepos = 0
	numLines = 0
	print("\nCounting lines for all of %s's repositories. This may take a while...\n" % accountname)
	for repository in session.iter_user_repos(accountname):
		repoLines = countRepoLines(repository)
		numLines += repoLines
		numRepos += 1
		print(repository, "contains", repoLines, "lines of code.")
	print("\nThere are", numRepos, "repositories, with a combined total of", numLines, "lines of code.")
	
def promptLogin():
	while True:
		try:
			print("Log in to GitHub to get API access (passwords are not stored):")
			username = input("Username: ")
			password = input("Password: ")
			gh = github.login(username, password)
			print("\nSigning in...\n")
			gh.update_user()
			return gh
		except (github.GitHubError):
			print("Sorry, but the given credentials were not accepted. Please try again.\n")
			
def promptGetUser():
	while True:
		result = input("Enter the name of the user you want to track:\n")
		if result != "":
			return result
		print("\nSorry, but you've only entered a blank string. Try again...\n")
	

def countRepoLines(repo):
	lines = 0
	repo.refresh()
	contentDict = repo.contents('')
	if contentDict != None:
		for content in contentDict:
			lines += countDirLines(repo, contentDict[content])
	else:
		print("%s could not be opened. It will not be counted." % repo.full_name)
	return lines
	
def countDirLines(repo, currentDir):
	lines = 0
	if currentDir.type == 'dir':
		dirContent = repo.contents(currentDir.path)
		for subDir in dirContent:
			lines += countDirLines(repo, dirContent[subDir])
	elif currentDir.type == 'file':
		try:
			currentDir.refresh()
		except(github.GitHubError):
			print("%s/%s could not be opened. It will not be counted" % (repo.full_name, currentDir.path))
		lines = [c for c in currentDir.decoded].count(ord('\n'))
	return lines

if __name__ == "__main__":
	main()
