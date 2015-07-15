# PyGit Tools

This is a small collection of dumb, useless, but fun tools written in python and using the GitHub API.

I may or may not support this software in the future, but feel free to send a pull request if you think you have a way to improve it. There is no warranty on this software, and I am absolutely not going to do full-time tech support for it, but I will try to be as helpful as I can if you're having problems. Send me an email, or create a new issue.

This entire repository is made available under the GNU General Public License v3.0. A full copy of this license is available as the [LICENSE](LICENSE) file in this repository, or at [gnu.org/licenses](http://www.gnu.org/licenses/).

## Dependencies:

This program uses the [github3.py library](https://github.com/sigmavirus24/github3.py), which is a python wrapper for the GitHub API. You can install it through PyPI:

> `pip install --pre github3.py`

The github3.py library is also dependent on two other libraries: [requests by Kenneth Reitz](https://github.com/kennethreitz/requests), and [uritemplate.py by Ian Cordasco](https://github.com/sigmavirus24/uritemplate). Those two libraries can also be installed through PyPI:

> `pip install requests`

> `pip install uritemplate.py`

## Added Tools:

### Linecount.py

This file will take the input of any GitHub username, and then count the number of lines of text that user has in all of their repositories combined. Needless to say, it takes a long time, but it still may be interesting to find out how many hundreds of thousands of lines you have on your (or someone else's) GitHub account. Right now, you have to give it your GitHub username and password for it to work, because it needs to be able to use the GitHub API as an authenticated user. I'll fix this later, but you can read the source code to verify that it doesn't do anything suspicious with your login data.

### MasterToDo.py

This file will, after confirming GitHub authentication, look through all of your repositories and search for to-do lists. It will compile all of the found lists into one master list, and then add some headings to make sure the sections keep separated.
