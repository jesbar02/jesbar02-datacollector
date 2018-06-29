This app was uploaded so i can test the online functioning using an heroku app.

For this, i used the account credentials "jesbar02@gmail.com / jesbar02heroku*". From the root of the working directory in the test server, i Logged in:

    jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ heroku login
    heroku: Enter your login credentials
    Email [jesbar02@gmail.com]:
    Password: ***************
    Logged in as jesbar02@gmail.com

    Following the course instructions, first i created the new app in heroku working place

    jesbar02@ubuntutesting:~/../Demo$ heroku create jesbar02-datacollector
    Creating ⬢ jesbar02-datacollector... done
    https://jesbar02-datacollector.herokuapp.com/ | https://git.heroku.com/jesbar02-datacollector.git


next step, create the database

    jesbar02@ubuntutesting:~/../Demo$ heroku addons:create heroku-postgresql:hobby-dev --app jesbar02-datacollector
    Creating heroku-postgresql:hobby-dev on ⬢ jesbar02-datacollector... free
    Database has been created and is available
     ! This database is empty. If upgrading, you can transfer
     ! data from another database with pg:copy
    Created postgresql-elliptical-60632 as DATABASE_URL
    Use heroku addons:docs heroku-postgresql to view documentation

Finding the URI connection string to the database and change the actual test SQLALCHEMY_DATABASE_URI at the app.py file:

    jesbar02@ubuntutesting:~/../Demo$ heroku config --app jesbar02-datacollector
     === jesbar02-datacollector Config Vars
    DATABASE_URL: postgres://bjpnwsnntybnbt:2ce93058d0a497e4ab418f0adfdd09d48a523a9bf69f215e995b2818bd0a5a0f@ec2-107-21-224-61.compute-1.amazonaws.com:5432/d57d6u704adh38

Later on, the virtual environment has to be activated to install the gunicorn package

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ pip3 install gunicorn
    Collecting gunicorn
      Using cached https://files.pythonhosted.org/packages/55/cb/09fe80bddf30be86abfc06ccb1154f97d6c64bb87111de066a5fc9ccb937/gunicorn-19.8.1-py2.py3-none-any.whl
    Installing collected packages: gunicorn
    Successfully installed gunicorn-19.8.1
    You are using pip version 8.1.1, however version 10.0.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.

Pass the virtual environment packages to a requirements file:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ pip freeze > requirements.txt
    You are using pip version 8.1.1, however version 10.0.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.

Take a look at the file:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ cat requirements.txt
    certifi==2018.4.16
    chardet==3.0.4
    click==6.7
    Flask==1.0.2
    Flask-SQLAlchemy==2.3.2
    gunicorn==19.8.1
    idna==2.7
    itsdangerous==0.24
    Jinja2==2.10
    MarkupSafe==1.0
    pkg-resources==0.0.0
    psycopg2-binary==2.7.5
    requests==2.19.1
    SQLAlchemy==1.2.8
    urllib3==1.23
    Werkzeug==0.14.1

Create a Procfile file:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ touch Procfile

Edit it:

    write this line inside :
    web: gunicorn app:app

Create the runtime text file

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ touch runtime.txt
    Note: The Following link is usefull to see the most recent supported runtime for python3 in heroku:
    https://devcenter.heroku.com/articles/python-runtimes

Create a gitignore file and write the files and directories that want to be excluded:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ touch .gitignore

Initialize the git repository:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git init
    Initialized empty Git repository in /home/jesbar02/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo/.git/

Adding current content. without the previously ignored files/directories:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git add .

Setting the github account

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git config user.email "jesbar02@gmail.com"
    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git config user.name "jesbar02"

Commit the changes:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git commit -m "First commit"
    [master (root-commit) f4f0925] First commit
     9 files changed, 211 insertions(+)
     create mode 100644 .gitignore
     create mode 100644 Procfile
     create mode 100644 app.py
     create mode 100644 requirements.txt
     create mode 100644 runtime.txt
     create mode 100644 send_email.py
     create mode 100644 static/main.css
     create mode 100644 templates/index.html
     create mode 100644 templates/success.html

I can test if we are still logged to the heroku account, before pushing files to heroku

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ heroku info jesbar02-datacollector
    === jesbar02-datacollector
    Addons:         heroku-postgresql:hobby-dev
    Auto Cert Mgmt: false
    Dynos:
    Git URL:        https://git.heroku.com/jesbar02-datacollector.git
    Owner:          jesbar02@gmail.com
    Region:         us
    Repo Size:      0 B
    Slug Size:      0 B
    Stack:          heroku-16
    Web URL:        https://jesbar02-datacollector.herokuapp.com/

Preparing the push to heroku:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ heroku git:remote --app jesbar02-datacollector
    set git remote heroku to https://git.heroku.com/jesbar02-datacollector.git

This error message is related with this requirement pkg-resources==0.0.0 , which it seams that is added after the pip3 freeze > requirements.txt command is excecuted, So i had to remove it from there.

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git push heroku master
    Counting objects: 13, done.
    Compressing objects: 100% (9/9), done.
    Writing objects: 100% (13/13), 3.55 KiB | 0 bytes/s, done.
    Total 13 (delta 0), reused 0 (delta 0)
    remote: Compressing source files... done.
    remote: Building source:
    remote:
    remote: -----> Python app detected
    remote: -----> Installing python-3.6.6
    remote: -----> Installing pip
    remote: -----> Installing requirements with pip
    remote:        Collecting certifi==2018.4.16 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 1))
    remote:          Downloading https://files.pythonhosted.org/packages/7c/e6/92ad559b7192d846975fc916b65f667c7b8c3a32bea7372340bfe9a15fa5/certifi-2018.4.16-py2.py3-none-any.whl (150kB)
    remote:        Collecting chardet==3.0.4 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 2))
    remote:          Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
    remote:        Collecting click==6.7 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 3))
    remote:          Downloading https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl (71kB)
    remote:        Collecting Flask==1.0.2 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 4))
    remote:          Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
    remote:        Collecting Flask-SQLAlchemy==2.3.2 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 5))
    remote:          Downloading https://files.pythonhosted.org/packages/a1/44/294fb7f6bf49cc7224417cd0637018db9fee0729b4fe166e43e2bbb1f1c8/Flask_SQLAlchemy-2.3.2-py2.py3-none-any.whl
    remote:        Collecting gunicorn==19.8.1 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 6))
    remote:          Downloading https://files.pythonhosted.org/packages/55/cb/09fe80bddf30be86abfc06ccb1154f97d6c64bb87111de066a5fc9ccb937/gunicorn-19.8.1-py2.py3-none-any.whl (112kB)
    remote:        Collecting idna==2.7 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 7))
    remote:          Downloading https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl (58kB)
    remote:        Collecting itsdangerous==0.24 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 8))
    remote:          Downloading https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz (46kB)
    remote:        Collecting Jinja2==2.10 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 9))
    remote:          Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl (126kB)
    remote:        Collecting MarkupSafe==1.0 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 10))
    remote:          Downloading https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz
    remote:        Collecting pkg-resources==0.0.0 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 11))
    remote:          Could not find a version that satisfies the requirement pkg-resources==0.0.0 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 11)) (from versions: )
    remote:        No matching distribution found for pkg-resources==0.0.0 (from -r /tmp/build_faa84545d589d54227786d5dbfd2c965/requirements.txt (line 11))
    remote:  !     Push rejected, failed to compile Python app.
    remote:
    remote:  !     Push failed
    remote: Verifying deploy...
    remote:
    remote: !	Push rejected to jesbar02-datacollector.
    remote:
    To https://git.heroku.com/jesbar02-datacollector.git
     ! [remote rejected] master -> master (pre-receive hook declined)
    error: failed to push some refs to 'https://git.heroku.com/jesbar02-datacollector.git'

Saving changes to the master branch

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git add .
    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git commit -m "After removed pkg-resources==0.0.0 from requirements.txt"
    [master 1fbc80a] After removed pkg-resources==0.0.0 from requirements.txt
    1 file changed, 1 deletion(-)

This time all went successful:

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ git push heroku master
    Counting objects: 16, done.
    Compressing objects: 100% (12/12), done.
    Writing objects: 100% (16/16), 3.79 KiB | 0 bytes/s, done.
    Total 16 (delta 2), reused 0 (delta 0)
    remote: Compressing source files... done.
    remote: Building source:
    remote:
    remote: -----> Python app detected
    remote: -----> Installing python-3.6.6
    remote: -----> Installing pip
    remote: -----> Installing requirements with pip
    remote:        Collecting certifi==2018.4.16 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 1))
    remote:          Downloading https://files.pythonhosted.org/packages/7c/e6/92ad559b7192d846975fc916b65f667c7b8c3a32bea7372340bfe9a15fa5/certifi-2018.4.16-py2.py3-none-any.whl (150kB)
    remote:        Collecting chardet==3.0.4 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 2))
    remote:          Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
    remote:        Collecting click==6.7 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 3))
    remote:          Downloading https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl (71kB)
    remote:        Collecting Flask==1.0.2 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 4))
    remote:          Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
    remote:        Collecting Flask-SQLAlchemy==2.3.2 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 5))
    remote:          Downloading https://files.pythonhosted.org/packages/a1/44/294fb7f6bf49cc7224417cd0637018db9fee0729b4fe166e43e2bbb1f1c8/Flask_SQLAlchemy-2.3.2-py2.py3-none-any.whl
    remote:        Collecting gunicorn==19.8.1 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 6))
    remote:          Downloading https://files.pythonhosted.org/packages/55/cb/09fe80bddf30be86abfc06ccb1154f97d6c64bb87111de066a5fc9ccb937/gunicorn-19.8.1-py2.py3-none-any.whl (112kB)
    remote:        Collecting idna==2.7 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 7))
    remote:          Downloading https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl (58kB)
    remote:        Collecting itsdangerous==0.24 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 8))
    remote:          Downloading https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz (46kB)
    remote:        Collecting Jinja2==2.10 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 9))
    remote:          Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl (126kB)
    remote:        Collecting MarkupSafe==1.0 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 10))
    remote:          Downloading https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz
    remote:        Collecting psycopg2-binary==2.7.5 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 11))
    remote:          Downloading https://files.pythonhosted.org/packages/3f/4e/b9a5cb7c7451029f67f93426cbb5f5bebedc3f9a8b0a470de7d0d7883602/psycopg2_binary-2.7.5-cp36-cp36m-manylinux1_x86_64.whl (2.7MB)
    remote:        Collecting requests==2.19.1 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 12))
    remote:          Downloading https://files.pythonhosted.org/packages/65/47/7e02164a2a3db50ed6d8a6ab1d6d60b69c4c3fdf57a284257925dfc12bda/requests-2.19.1-py2.py3-none-any.whl (91kB)
    remote:        Collecting SQLAlchemy==1.2.8 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 13))
    remote:          Downloading https://files.pythonhosted.org/packages/b4/9c/411a9bac1a471bed54ec447dc183aeed12a75c1b648307e18b56e3829363/SQLAlchemy-1.2.8.tar.gz (5.6MB)
    remote:        Collecting urllib3==1.23 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 14))
    remote:          Downloading https://files.pythonhosted.org/packages/bd/c9/6fdd990019071a4a32a5e7cb78a1d92c53851ef4f56f62a3486e6a7d8ffb/urllib3-1.23-py2.py3-none-any.whl (133kB)
    remote:        Collecting Werkzeug==0.14.1 (from -r /tmp/build_d95962b02b737e3ceb72d6815f879637/requirements.txt (line 15))
    remote:          Downloading https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
    remote:        Installing collected packages: certifi, chardet, click, itsdangerous, Werkzeug, MarkupSafe, Jinja2, Flask, SQLAlchemy, Flask-SQLAlchemy, gunicorn, idna, psycopg2-binary, urllib3, requests
    remote:          Running setup.py install for itsdangerous: started
    remote:            Running setup.py install for itsdangerous: finished with status 'done'
    remote:          Running setup.py install for MarkupSafe: started
    remote:            Running setup.py install for MarkupSafe: finished with status 'done'
    remote:          Running setup.py install for SQLAlchemy: started
    remote:            Running setup.py install for SQLAlchemy: finished with status 'done'
    remote:        Successfully installed Flask-1.0.2 Flask-SQLAlchemy-2.3.2 Jinja2-2.10 MarkupSafe-1.0 SQLAlchemy-1.2.8 Werkzeug-0.14.1 certifi-2018.4.16 chardet-3.0.4 click-6.7 gunicorn-19.8.1 idna-2.7 itsdangerous-0.24 psycopg2-binary-2.7.5 requests-2.19.1 urllib3-1.23
    remote:
    remote: -----> Discovering process types
    remote:        Procfile declares types -> web
    remote:
    remote: -----> Compressing...
    remote:        Done: 49.1M
    remote: -----> Launching...
    remote:        Released v4
    remote:        https://jesbar02-datacollector.herokuapp.com/ deployed to Heroku
    remote:
    remote: Verifying deploy... done.
    To https://git.heroku.com/jesbar02-datacollector.git
    * [new branch]      master -> master


As the database in heroku is empty (No tables), we need to create it manually using for this the heroku command lines

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ heroku run python3
    Running python3 on ⬢ jesbar02-datacollector... up, run.8429 (Free)
    Python 3.6.6 (default, Jun 28 2018, 15:14:32)
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from app import db
    /app/.heroku/python/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
      'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
    >>> db.create_all() ---->
    >>> exit

accesing the database from Heroku to see commits 

    (virtual) jesbar02@ubuntutesting:~/python_course/python_mega_course/beyond_basics/pp/flask_and_databases/Demo$ heroku pg:psql postgresql-elliptical-60632 --app jesbar02-datacollector
    --> Connecting to postgresql-elliptical-60632
    psql (10.4 (Ubuntu 10.4-2.pgdg16.04+1))
    SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
    Type "help" for help.

    jesbar02-datacollector::DATABASE=>
