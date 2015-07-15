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

import util

TODO_FILES = ["todo.md", "todo.txt"]
DIVIDER_STRING = "----------------------------------------------------------------\n\n\n"

def main():
	session = util.promptLogin()
	outputName = util.promptInput("Enter the desired output filename: ")
	outputFile = open(outputName, 'w')
	print()
	for repo in session.iter_repos():
		print(repo)
		repoTodo = getTodoFile(repo)
		if (repoTodo != None):
			repoTodo.refresh()
			outputFile.write(DIVIDER_STRING)
			outputFile.write("# TO-DO List found in %s:\n" % repo.full_name)
			outputFile.write(DIVIDER_STRING)
			outputFile.write(repoTodo.decoded.decode("utf-8"))
			outputFile.write("\n\n\n")
	print("\nDone! All found to-do files have been combined and saved as %s." % outputName)
	
def getTodoFile(repo):
	allRootFiles = repo.contents('')
	for fileKey in allRootFiles:
		content = allRootFiles[fileKey]
		if content.type == "file" and content.name.lower() in TODO_FILES:
			return content

if __name__ == '__main__':
	main()