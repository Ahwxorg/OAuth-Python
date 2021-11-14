# OAuth2-Python
#### Discord Inplementation for OAuth2 login systems.

This is a simple Python 'app' made to inplement in your programs that require (shitty) Discord ID verification.

![OAuth2 Showcase](https://raw.githubusercontent.com/Prifixy/OAuth-Python/main/assets/showcase.gif)


## How to install?

###### Cloning the repo
Just clone this repo inside of any directory. It really doesn't matter. For this 'tutorial' I will be using /home/$USER/OAuth2/, clone to there using:
```bash
git clone https://github.com/Prifixy/OAuth2-Python.git ~/OAuth2
```

###### Dependencies (pip)
All dependencies are in the requirements.txt file, just install all of them by running the following command inside your directory.
```bash
pip install -r requirements.txt
```

###### Editing the configuration
You need to edit both the `app.py` and `oauth.py` files. Add your Discord OAuth bot information, your redirect URL and configure the files to your needs.

###### Running
```bash
python3 ~/OAuth2/app.py
```

## Contributing
You can make pull requests, and I will review them.

## Issues
Please make a pull request if you know a fix, and otherwise make a issue, at [the issues tab](https://github.com/Prifixy/OAuth2-Python/issues)
