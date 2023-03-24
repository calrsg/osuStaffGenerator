import requests
import json
import pyperclip

class Config:

    config = "./config.json"

    @staticmethod
    def readConfig():
        with open(Config.config) as file:
            contents = json.loads(file.read())
            file.close()
            return contents["osu"]["osu_api"]

    @staticmethod
    def fetchAPIKey():
        while API.getUser("peppy") is None:
            API.key = input("Enter a valid API key: ")

        store = input("API key validated, would you like to locally store your key for future use? [y/n]")

        if store == "y":
            with open(Config.config, "r", encoding='utf-8') as file:
                contents = json.load(file)
                contents["osu"]["osu_api"] = API.key
                file.close()
            with open(Config.config, "w", encoding='utf-8') as file:
                json.dump(contents, file, ensure_ascii=False, indent=4)


class API:
    key = Config.readConfig()
    url = "https://osu.ppy.sh/api/"

    @staticmethod
    def getUser(username):
        request = requests.get(f"{API.url}get_user?k={API.key}&u={username}&m=0")
        if request.status_code != 200:
            print(f"Error fetching data, status code {request.status_code}")
            return None
        data = request.json()
        if len(data) < 1:
            return None
        return data[0]

    @staticmethod
    def formatUser(user):
        """
        Take in an osu! Api user
        :param user:
        :return:
        """
        img = f"[img]https://flagcdn.com/16x12/{user['country'].lower()}.png[/img]"
        link = f"[url=https://osu.ppy.sh/users/{user['user_id']}]{user['username']}[/url]"
        return f"{img} {link}"


def main():
    if API.key == "":
        print("No API key found.")
        Config.fetchAPIKey()

    print("For each of the following staff roles, enter a set of names separated by commas, with no spaces."
          "\neg. 'HOSTS: Gala,peppy'"
          "\nLeave blank and press enter if you do not need a role filled.")
    hosts = input("HOSTS:")
    headmappoolers = input("HEAD MAPPOOLERS: ")
    mappoolers = input("MAPPOOLERS: ")
    playtesters = input("PLAYTESTERS: ")
    referees = input("REFEREES: ")
    streamers = input("STREAMERS: ")
    commentators = input("COMMENTATORS: ")
    graphics = input("GRAPHICS: ")
    sheeters = input("SHEETERS: ")

    roles = [["Host", hosts], ["Head Mappooler", headmappoolers], ["Mappooler", mappoolers], ["Playtester", playtesters], ["Referee", referees],
             ["Streamer", streamers], ["Commentator", commentators], ["Graphics", graphics], ["Sheeters", sheeters]]

    result = ""
    print("Processing roles, please wait...")
    for role in roles:
        output = f"{role[0]}: "
        if len(role) > 0:
            usernames = role[1].split(sep=",")
            usernames.sort()
            count = 0
            for username in usernames:
                count += 1
                user = API.getUser(username)
                if user is not None:
                    userText = API.formatUser(user)
                    output += f"{userText}"
                    if count != len(usernames):
                        output += f" | "
            result += f"{output}\n"
    pyperclip.copy(result)
    print("Staff list has been copied to your clipboard.")


if __name__ == "__main__":
    main()