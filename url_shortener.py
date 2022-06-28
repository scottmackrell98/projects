Last login: Fri Jun  3 12:38:15 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) Scotts-MacBook-Pro:~ scottmackrell$ pip install pipenv
Collecting pipenv
  Downloading pipenv-2022.6.7-py2.py3-none-any.whl (3.9 MB)
     |████████████████████████████████| 3.9 MB 4.7 MB/s 
Requirement already satisfied: certifi in ./opt/anaconda3/lib/python3.9/site-packages (from pipenv) (2021.10.8)
Collecting pip>=22.0.4
  Downloading pip-22.1.2-py3-none-any.whl (2.1 MB)
     |████████████████████████████████| 2.1 MB 7.1 MB/s 
Requirement already satisfied: setuptools>=36.2.1 in ./opt/anaconda3/lib/python3.9/site-packages (from pipenv) (58.0.4)
Collecting virtualenv
  Downloading virtualenv-20.15.0-py2.py3-none-any.whl (10.1 MB)
     |████████████████████████████████| 10.1 MB 12.8 MB/s 
Collecting virtualenv-clone>=0.2.5
  Downloading virtualenv_clone-0.5.7-py3-none-any.whl (6.6 kB)
Collecting distlib<1,>=0.3.1
  Downloading distlib-0.3.4-py2.py3-none-any.whl (461 kB)
     |████████████████████████████████| 461 kB 7.0 MB/s 
Collecting platformdirs<3,>=2
  Downloading platformdirs-2.5.2-py3-none-any.whl (14 kB)
Requirement already satisfied: filelock<4,>=3.2 in ./opt/anaconda3/lib/python3.9/site-packages (from virtualenv->pipenv) (3.3.1)
Requirement already satisfied: six<2,>=1.9.0 in ./opt/anaconda3/lib/python3.9/site-packages (from virtualenv->pipenv) (1.16.0)
Installing collected packages: platformdirs, distlib, virtualenv-clone, virtualenv, pip, pipenv
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed distlib-0.3.4 pip-22.1.2 pipenv-2022.6.7 platformdirs-2.5.2 virtualenv-20.15.0 virtualenv-clone-0.5.7
(base) Scotts-MacBook-Pro:~ scottmackrell$ pipenv shell
Creating a virtualenv for this project...
Pipfile: /Users/scottmackrell/Pipfile
Using /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 (3.10.3) to create virtualenv...
⠼ Creating virtual environment...created virtual environment CPython3.10.3.final.0-64 in 2538ms
  creator CPython3Posix(dest=/Users/scottmackrell/.local/share/virtualenvs/scottmackrell-O3HS1kEP, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/scottmackrell/Library/Application Support/virtualenv)
    added seed packages: pip==22.1.2, setuptools==62.6.0, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment! 
Virtualenv location: /Users/scottmackrell/.local/share/virtualenvs/scottmackrell-O3HS1kEP
Creating a Pipfile for this project...
Launching subshell in virtual environment...
 . /Users/scottmackrell/.local/share/virtualenvs/scottmackrell-O3HS1kEP/bin/activate

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bash-3.2$  . /Users/scottmackrell/.local/share/virtualenvs/scottmackrell-O3HS1kEP/bin/activate
(scottmackrell) bash-3.2$ pipenv install Flask
Installing Flask...
Adding Flask to Pipfile's [packages]...
✔ Installation Succeeded 
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (81f117)!
Installing dependencies from Pipfile.lock (81f117)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
(scottmackrell) bash-3.2$ pipenv install Flask-Migrate
Installing Flask-Migrate...
Adding Flask-Migrate to Pipfile's [packages]...
✔ Installation Succeeded 
Pipfile.lock (81f117) out of date, updating to (86c875)...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (86c875)!
Installing dependencies from Pipfile.lock (86c875)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
(scottmackrell) bash-3.2$ pipenv install Flask-SQLAlchemy
Installing Flask-SQLAlchemy...
Adding Flask-SQLAlchemy to Pipfile's [packages]...
✔ Installation Succeeded 
Pipfile.lock (86c875) out of date, updating to (4b4803)...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (4b4803)!
Installing dependencies from Pipfile.lock (4b4803)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
(scottmackrell) bash-3.2$ pipenv install psycopg2
Installing psycopg2...
Adding psycopg2 to Pipfile's [packages]...
✔ Installation Succeeded 
Pipfile.lock (4b4803) out of date, updating to (cc09f7)...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (cc09f7)!
Installing dependencies from Pipfile.lock (cc09f7)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
(scottmackrell) bash-3.2$ pipenv install gunicorn
Installing gunicorn...
Adding gunicorn to Pipfile's [packages]...
✔ Installation Succeeded 
Pipfile.lock (cc09f7) out of date, updating to (a79cf2)...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (a79cf2)!
Installing dependencies from Pipfile.lock (a79cf2)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
(scottmackrell) bash-3.2$ pipenv install python-decouple
Installing python-decouple...
Adding python-decouple to Pipfile's [packages]...
✔ Installation Succeeded 
Pipfile.lock (a79cf2) out of date, updating to (89d892)...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (89d892)!
Installing dependencies from Pipfile.lock (89d892)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
(scottmackrell) bash-3.2$ mkdir core
(scottmackrell) bash-3.2$ cd core
(scottmackrell) bash-3.2$ touch __init__.py
(scottmackrell) bash-3.2$ cd ..
(scottmackrell) bash-3.2$ from decouple import config
from: can't read /var/mail/decouple
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ DATABASE_URI = config("DATABASE_URL")
bash: syntax error near unexpected token `('
(scottmackrell) bash-3.2$ if DATABASE_URI.startswith("postgres://"):
bash: syntax error near unexpected token `"postgres://"'
(scottmackrell) bash-3.2$     DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)
bash: syntax error near unexpected token `('
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ class Config(object):
bash: syntax error near unexpected token `('
(scottmackrell) bash-3.2$     DEBUG = False
bash: DEBUG: command not found
(scottmackrell) bash-3.2$     TESTING = False
bash: TESTING: command not found
(scottmackrell) bash-3.2$     CSRF_ENABLED = True
bash: CSRF_ENABLED: command not found
(scottmackrell) bash-3.2$     SECRET_KEY = config('SECRET_KEY', default='guess-me')
bash: syntax error near unexpected token `('
(scottmackrell) bash-3.2$     SQLALCHEMY_DATABASE_URI = DATABASE_URI
bash: SQLALCHEMY_DATABASE_URI: command not found
(scottmackrell) bash-3.2$     SQLALCHEMY_TRACK_MODIFICATIONS = False
bash: SQLALCHEMY_TRACK_MODIFICATIONS: command not found
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ class ProductionConfig(Config):
bash: syntax error near unexpected token `('
(scottmackrell) bash-3.2$     DEBUG = False
bash: DEBUG: command not found
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ class StagingConfig(Config):
bash: syntax error near unexpected token `('
(scottmackrell) bash-3.2$     DEVELOPMENT = True
bash: DEVELOPMENT: command not found
(scottmackrell) bash-3.2$     DEBUG = True
bash: DEBUG: command not found
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ class DevelopmentConfig(Config):
bash: syntax error near unexpected token `('
(scottmackrell) bash-3.2$     DEVELOPMENT = True
bash: DEVELOPMENT: command not found
(scottmackrell) bash-3.2$     DEBUG = True
bash: DEBUG: command not found
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ 
(scottmackrell) bash-3.2$ class TestingConfig(Config):
bash: syntax error near unexpected token `('
(scottmackrell) bash-3.2$     TESTING = True
bash: TESTING: command not found
(scottmackrell) bash-3.2$ exit
exit
(base) Scotts-MacBook-Pro:~ scottmackrell$ pip3 install pyshorteners
Collecting pyshorteners
  Downloading pyshorteners-1.0.1.tar.gz (10.0 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: requests in ./opt/anaconda3/lib/python3.9/site-packages (from pyshorteners) (2.26.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./opt/anaconda3/lib/python3.9/site-packages (from requests->pyshorteners) (1.26.7)
Requirement already satisfied: charset-normalizer~=2.0.0 in ./opt/anaconda3/lib/python3.9/site-packages (from requests->pyshorteners) (2.0.4)
Requirement already satisfied: certifi>=2017.4.17 in ./opt/anaconda3/lib/python3.9/site-packages (from requests->pyshorteners) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in ./opt/anaconda3/lib/python3.9/site-packages (from requests->pyshorteners) (3.2)
Building wheels for collected packages: pyshorteners
  Building wheel for pyshorteners (setup.py) ... done
  Created wheel for pyshorteners: filename=pyshorteners-1.0.1-py3-none-any.whl size=17496 sha256=28aeffa217a81d1037dd21839a9d37b2787dd4d09274219d2885c1c5c1301cf0
  Stored in directory: /Users/scottmackrell/Library/Caches/pip/wheels/51/56/d8/765ad4c919190fbd24541487735547e6c665c9381d4d689ae8
Successfully built pyshorteners
Installing collected packages: pyshorteners
Successfully installed pyshorteners-1.0.1
(base) Scotts-MacBook-Pro:~ scottmackrell$ pip3 install requests
Requirement already satisfied: requests in ./opt/anaconda3/lib/python3.9/site-packages (2.26.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./opt/anaconda3/lib/python3.9/site-packages (from requests) (1.26.7)
Requirement already satisfied: charset-normalizer~=2.0.0 in ./opt/anaconda3/lib/python3.9/site-packages (from requests) (2.0.4)
Requirement already satisfied: certifi>=2017.4.17 in ./opt/anaconda3/lib/python3.9/site-packages (from requests) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in ./opt/anaconda3/lib/python3.9/site-packages (from requests) (3.2)
(base) Scotts-MacBook-Pro:~ scottmackrell$ pip3 show pyshortener
WARNING: Package(s) not found: pyshortener
(base) Scotts-MacBook-Pro:~ scottmackrell$ pip3 show pyshortener
WARNING: Package(s) not found: pyshortener
(base) Scotts-MacBook-Pro:~ scottmackrell$ pip install pyshorteners
Requirement already satisfied: pyshorteners in ./opt/anaconda3/lib/python3.9/site-packages (1.0.1)
Requirement already satisfied: requests in ./opt/anaconda3/lib/python3.9/site-packages (from pyshorteners) (2.26.0)
Requirement already satisfied: certifi>=2017.4.17 in ./opt/anaconda3/lib/python3.9/site-packages (from requests->pyshorteners) (2021.10.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./opt/anaconda3/lib/python3.9/site-packages (from requests->pyshorteners) (1.26.7)
Requirement already satisfied: charset-normalizer~=2.0.0 in ./opt/anaconda3/lib/python3.9/site-packages (from requests->pyshorteners) (2.0.4)
Requirement already satisfied: idna<4,>=2.5 in ./opt/anaconda3/lib/python3.9/site-packages (from requests->pyshorteners) (3.2)
(base) Scotts-MacBook-Pro:~ scottmackrell$ import pyshorteners
-bash: import: command not found
(base) Scotts-MacBook-Pro:~ scottmackrell$ 
(base) Scotts-MacBook-Pro:~ scottmackrell$ s = pyshorteners.Shortener()
-bash: syntax error near unexpected token `('
(base) Scotts-MacBook-Pro:~ scottmackrell$ print(s.tinyurl.short('http://www.g1.com.br'))
-bash: syntax error near unexpected token `s.tinyurl.short'
(base) Scotts-MacBook-Pro:~ scottmackrell$ import pyshorteners
-bash: import: command not found
(base) Scotts-MacBook-Pro:~ scottmackrell$ pip3 show pyshorteners
Name: pyshorteners
Version: 1.0.1
Summary: A Python lib to wrap and consume the most used shorteners APIs
Home-page: https://github.com/ellisonleao/pyshorteners/
Author: Ellison Leão
Author-email: ellisonleao@gmail.com
License: GPLv3
Location: /Users/scottmackrell/opt/anaconda3/lib/python3.9/site-packages
Requires: requests
Required-by: 
(base) Scotts-MacBook-Pro:~ scottmackrell$ vi url_shortener.py

import pyshorteners

s = pyshorteners.Shortener()
print(s.tinyurl.short('https://www.flexmind.co'))
print(s.isgd.short('https://www.flexmind.co'))
print(s.osdb.short('https://www.flexmind.co'))
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
-- ^X mode (^]^D^E^F^I^K^L^N^O^Ps^U^V^Y)
