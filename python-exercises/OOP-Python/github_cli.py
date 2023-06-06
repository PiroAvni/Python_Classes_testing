import requests


class Repository:
    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url

    def display_details(self):
        print(f"\nRepository: {self.name}")
        print(f"Description: {self.description}")
        print(f"URL: {self.url}")


class GitHubCLI:
    def __init__(self):
        self.username = ""
        self.repositories = []

    def run(self):
        self.get_username()
        self.fetch_repositories()
        self.display_repository_list()
        self.prompt_user_selection()

    def get_username(self):
        self.username = input("Enter your GitHub username: ")

    def fetch_repositories(self):
        url = f"https://api.github.com/users/{self.username}/repos"
        response = requests.get(url)

        if response.status_code == 200:
            repositories_data = response.json()

            for repo_data in repositories_data:
                name = repo_data["name"]
                description = repo_data["description"]
                url = repo_data["html_url"]
                repository = Repository(name, description, url)
                self.repositories.append(repository)
        else:
            print("Failed to fetch repositories. Please try again.")

    def display_repository_list(self):
        print(f"\nRepository List for {self.username}:\n")
        for i, repo in enumerate(self.repositories, start=1):
            print(f"{i}. {repo.name}")

    def prompt_user_selection(self):
        while True:
            selection = input("\nEnter a number to view repository details (or 'q' to quit): ")

            if selection == "q":
                break

            try:
                index = int(selection) - 1
                repository = self.repositories[index]
                repository.display_details()
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")


# Run the GitHub CLI
github_cli = GitHubCLI()
github_cli.run()
