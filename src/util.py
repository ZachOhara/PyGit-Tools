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
			
def promptInput(prompt):
	while True:
		result = input(prompt)
		if result != "":
			return result
		print("\nSorry, but you've only entered a blank string. Try again...\n")
			