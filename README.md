<img src='https://raw.githubusercontent.com/Rerum-Crea/.github/main/art/Headers/Logo-Header-TAT.png' alt='Art Header' width='100%' height='100%'>
<br>

# Add-Proxys Branch

A set of Twitch tools for functions like Creating accounts, Following Users, View Boting, and more!



## Contents

- [Features](##Features)
- [Installation](##Installation)
- [Usage](##Usage)
- [Contributing](##Contributing)
- [License](##License)
- [Questions](##Questions)

## Features

The current features are pretty simple and are only for the most basic use cases using selenium:

- [Create a Twitch account](###Create-a-Twitch-account)
- [Follow a Twitch user](###Follow-a-Twitch-user)
- [Mass view Twitch users](###Mass-view-Twitch-users)

### Create-a-Twitch-account

The first feature is to create a Twitch account.
This is done using selenium to pretend to be a user to create a new account.

This can be useful for creating accounts for bots, or for creating accounts for people who are not Twitch users.

Pros:

- Easy to use.
- Can create accounts fast.
- Can create accounts with custom usernames.
- Records the account information.
- No email verification required.

Cons:

- Users need to complete captcha.
- You need a good proxy list.

### Follow-a-Twitch-user

The second feature is to follow a Twitch user.
This is done using selenium to pretend to be a user to follow a user.

This can be useful for following users in mass amounts.

Pros:

- Easy to use.
- Can follow users fast.
- Can follow users with custom usernames.

Cons:

- Users need to complete captcha.

### Mass-view-Twitch-users

The third feature is to mass view Twitch users.
This is done using selenium to pretend to be a user to view a user.

This can be useful for mass viewing users in mass amounts.

Pros:

- Easy to use.
- Can view users fast.
- Uses proxies to view users.

Cons:

- You need a good proxy list.

## Installation

To install the application, download the [source code](https://github.com/Necrownyx/Twitch-Account-Toolbox/archive/refs/heads/main.zip) and run the following command after extracting the archive:

```
pip install -r requirements.txt
```

## Usage

To use the application you first need to decide which features you want to use.

The list below shows the features that are currently available and the filenames that you need to use to run the application.
The files are in the modules folder.

- [TAC.py](###TAC.py) - Twitch Account Creator
- [TAF.py](###TAF.py) - Twitch Account Follower

### TAC.py

To set up the application, you need add information to the files below:

- [__usernames.txt](__usernames.txt) - The usernames of the accounts to be created.
- [__proxies.txt](__proxies.txt) - The proxies to use.


Then run the following command to run the application:

```
python TAC.py
```

Then wait a second for the application to start.
Solve the captcha.
Enjoy!

**Note:** Twitch only allows you to create a limited amount of accounts in an amount of time.

### TAF.py

To set up the application, you need add information to the files below:

- [___infolist.txt](___infolist.txt) - The usernames:passowords of the users *Generated with [TAC.py](###TAC.py)*.
- [TAF.py](./Modules/TAF.py) - You need to add the link to the choosen twitch channel in the channel variable at the top of the file.

Then run the following command to run the application:

```
python TAF.py
```

### TSV.py

To set up the application, you need add information to the files below:

- [TSV.py](./Modules/TSV.py) - You need to add the link to the choosen twitch channel in the channel variable at the top of the file.
- [__proxies.txt](__proxies.txt) - The proxies to use.

Then run the following command to run the application:

```
python TSV.py
```

Enter the amount of users you want to view. **Note:** A large number of users can cause lag.
Enjoy.


## Contributing

To contribute to the application, you can fork the repository and make a pull request.

A good contribution is to add a new feature or fix a bug.

For example, if you want to add a new feature, you can create a new module and add it to the application.

## License

This project is licensed under the MIT license

This means that you can use the code for any purpose, as long as you give credit to the original author.

## Questions

Q: Why can't the captcha be solved automatically?
A: The captcha is solved by the user becasue the whole point of the capcha is to stop this from being fully automatic.
<br>
Q: How do I get large lists of usernames?
A: A method I use is to get a list of usernames from a discord server with [this Discord User Scraper](https://github.com/Necrownyx/Discord-User-Scraper) then parseing the list to a text file using a script like [this](https://gist.github.com/Necrownyx/b586fa87908135012e65757e7772359e)
<br>
If you have any questions, feel free to create an issue on the [Github repository](https://github.com/Necrownyx/Twitch-Account-Toolbox/issues)







