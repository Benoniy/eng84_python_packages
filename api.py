# Python requests package
# connect to website using requests api

# Task 1 - connect to bbc.co.uk and ensure its online
import requests
# reponses = requests.get("https://www.bbc.co.uk/")
# print(reponses.status_code)  # Status code 200 means running, 400 or 404 means dead


# Task 2 - create a function called status code check
# The function should return a status code and message
def status_code_check(website):
    status = requests.get(website).status_code

    if status == 200:
        return f"The website {website} is running properly, status code 200"
    else:
        return f"There was an error while connecting to {website}. Status code {status}"


if __name__ == "__main__":
    print(status_code_check("https://www.bbc.co.uk/"))
    print(status_code_check("https://www.aaaaaaaa.com/"))  # the heck?????
    print(status_code_check("https://www.marvel.com/404"))


# Task 2 - Itterate the code to use requests instance evaluation
# The function should return a status code and message
print("\n")
def status_code_check(website):
    response = requests.get(website)

    if response:
        return f"The website {website} is running properly, status code 200"
    else:
        return f"There was an error while connecting to {website}. Status code {response.status_code}"


if __name__ == "__main__":
    print(status_code_check("https://www.bbc.co.uk/"))
    print(status_code_check("https://www.aaaaaaaa.com/"))  # the heck?????
    print(status_code_check("https://www.marvel.com/404"))


