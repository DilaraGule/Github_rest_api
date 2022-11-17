import requests

class GitHub:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"

    def getUser(self, username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()                                           # gelen yanıt jsona dönüştürülüyor (result = json.loads(response.text))

    def getRepositories(self, username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()

    def createRepository(self, name):
        response = requests.post(self.api_url + "/user/repos?access_token=" + self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()


github = GitHub()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçiminizi yapın: ")

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input("username: ")
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} followers: {result['followers']}")

        elif secim == '2':
            username = input("username: ")
            result = github.getRepositories(username)

            for repo in result:
                print(repo['name'])

        elif secim == '3':
            name = input("repository name: ")
            result = github.createRepository(name)
            print(result)
        else:
            print("Yanlış seçim")