
![](https://i.imgur.com/IWBIgYf.png)
# osuStaffGenerator

A small tool that uses the osu!api and takes in a list of users to generate a standard format staff list for osu! tournament forum posts.

### Example

![](https://i.imgur.com/36qa4Is.png)

### Usage

![](https://i.imgur.com/QEtSxRh.png)

Usage is very straightforward. An example is given, then for each set of roles you can enter a list of usernames with commas between. Capitalisation of usernames doesn't matter, as long as they are valid usernames. 

Once all roles have been filled or left empty, wait a few seconds for osu! API to fetch info on all requested users. When completed, the staff list will be copied to your clipboard, and you can now paste it.

### Setup

This will be updated to include more user-friendly options.

1) Download and unzip the repo.
2) Ensure Python 3.10+ is installed.
3) Open terminal and install the dependencies:
	- pip install pyperclip
4) In terminal, cd to where the application was unzipped.
5) Once in the right directory, run the application:
	- python main.py
6) You will be prompted to enter an osu! API key. Learn more [here](https://osu.ppy.sh/wiki/en/osu%21api), and visit the application page to et your API key. 
	- The API key is only used for the session, and won't be added to the config unless you opt to store it. Remember, do not share your API key with anyone. 

### Flags

Flag images are taken from [flagcdn](https://flagcdn.com), and are 16x12. These dimensions can be changed manually in the URL, but currently this program doesn't support changing size.
