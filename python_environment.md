# Spot Python Development Environment for Ubuntu 18.04

The Boston Dynamics [QUICKSTART](https://dev.bostondynamics.com/docs/python/quickstart#install-spot-python-packages) provides information on setting up the development environment.

The following information provides the process for setting up the Python 3.7 development environment for Spot on [Ubuntu 18.04 Desktop](https://releases.ubuntu.com/18.04/). There is more than one way to do this and the following shows what I am using. We could use the pre-installed Python 3.6, but I wanted to go with the latest supported version of Python, Python 3.7.

*Google:* version of python in Ubuntu 18.04

>"the Python package distributed with Ubuntu 18.04 is version 3.6."

From the Boston Dynamics Python requirements:

>"Spot Python SDK works with Python 3.6 or Python 3.7 only. Python 3.8 is not supported."

The following instructions include installing Python 3.7 and making ```python3``` point to the installed Python 3.7. 

Note: ```python``` should point to Python 2 and left that way. Changing this may break things on the system. ```python3``` should point to the version of Python 3 that is desired.

## Install Python 3.7

To install Python 3.7 and create a symbolic link between python3.7 and python3 in /usr/bin, do the following.

*Assumptions:* The user doing the installation has **sudo** access.

### Install Python 3.7 using apt

>sudo apt install python3.7

Note: I didn't have any dependency issues with install Python 3.7 on Ubuntu 18.04. If you do have issues, check out [How to Install Python 3.7 on Ubuntu 18.04](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/).

### Create a symbolic link between python3.7 and /usr/bin/python3

Creating a symbolic link between python3.7 and /usr/bin/python3 means that when ```python3``` is run, Python 3.7 is used. A link already exists between python3.6 and /usr/bin/python3. The python3.6 link is deleted and then a new link is created that uses python3.7. The ```-f``` option for ```ln``` removes existing destination files (in this case /usr/bin/python3). This means the new symbolic link replaces the existing symbolic link.

>sudo ln -fs /usr/bin/python3.7 /usr/bin/python3

After the link is created, using ```python3``` runs python3.7. To verify this is the case, run:

>python3 -V

A version of Python 3.7 should be displayed like is shown in the following.

>dale@p1:~$ python3 -V

```Python 3.7.5```

Also check that ```python``` runs a version of Python 2.

>python -V

A version of Python 2 should be displayed like is shown in the following.

>dale@p1:~$ python -V

```Python 2.7.1```

## Installing pip

```pip``` is the Python package manager/installer. It is used to install the Spot SDK as well as other packages used in the development of Spot apps.

First check if you already have ```pip``` installed for the version of Python 3.7 being used.

>python3 -m pip --version

If ```pip``` is not found, then use the following to install it.

>sudo apt install python3-pip

After is installed, check again to see if it is installed.

>python3 -m pip --version

A version of pip should be displayed like is shown in the following.

>dale@p1:~$ python3 -m pip --version

```pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.7)```

Notes:

* ```pip``` is run using ```python -m pip``` to ensure that the ```pip``` associated with the Python we are using is run. If you just run ```pip``` or ```pip3```, you may be executing the ```pip``` for the wrong version of Python.
* My Ubuntu command prompt shown is ```dale@p1:~$```. ```dale``` is my user ID.  ```p1``` is the name of my computer. After the ```:``` is the current directory that is set to ```~``` which is my home directory. The ```$``` is at the end of the prompt and before where a command is entered.
* Why is my computer named p1? I read the book [The Adolescence of P1](https://en.wikipedia.org/wiki/The_Adolescence_of_P-1) and it was influential in getting me where I am today. "It features a hacker who creates an artificial intelligence named P-1, which goes rogue and takes over computers in its desire to survive and seek out its creator." Reference: [The Adolescence of P-1, Wikipedia](https://en.wikipedia.org/wiki/The_Adolescence_of_P-1).

## Installing and Using the Python Virtual Environment

A Python virtual environment contains a version of Python and the packages that are required for the application being developed. Virtual environments make it easy to have the environment that is needed for each project. There is more than one option for virtual environments for Python. The Python ```virtualenv``` is used because it  is used in the Boston Dynamics documentation.

### Installing ```virtualenv```

Using ```virtualenv``` allows each project to have the version of Python and the required packages that are needed. You activate an environment, work in it, then deactivate it when you are done. The command prompt is changed to let you know you are working in a virtual environment.

The following is used to install ```virtualenv```.

>python3 -m pip install virtualenv

To test that virtualenv is installed and working, follow the steps to create a new project and make it a virtual environment.

### Creating a virtual environment using ```virtualenv```

A directory is the container for a project.  To create a new virtual environment, create a directory for the project and execute the command for making it a virtual environment. If that works, it is installed.

I put my projects in ```~/Documents/spot```, so I create a directory inside the ```spot``` directory for the project.

Change to the directory where you want to create the new directory.

>cd ~/Documents/spot

Then, make the new directory.

>mkdir spotproject1

Make the new directory a virtual environment.

>python3 -m virtualenv spotproject1

When I do the above, I get the following.

>dale@p1:~/Documents/spot$ python3 -m virtualenv spotproject1

>created virtual environment CPython3.7.5.final.0-64 in 107ms
  creator CPython3Posix(dest=/home/dale/Documents/spot/spotproject1, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/dale/.local/share/virtualenv)
    added seed packages: pip==21.0.1, setuptools==53.0.0, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

We can now take a look at what was created in the directory. Change to the directory and then use ```ls``` to display its contents.

>dale@p1:~/Documents/spot/spotproject1$ ls

```bin  lib  pyvenv.cfg```

The directories ```bin``` and ```lib``` were created along with the ```pyvenv.cfg``` file. 

To list the contents of ```bin``` do the following. It contains the programs that are needed including ```python3.7```, ```pip``` and ```wheel```. The ```activate``` program is used to activate the virtual environment.

>dale@p1:~/Documents/spot/spotproject1$ ls -al bin

```
total 64
drwxr-xr-x 2 dale dale 4096 Mar  3 19:46 .
drwxr-xr-x 4 dale dale 4096 Mar  3 19:46 ..
-rw-r--r-- 1 dale dale 2384 Mar  3 19:46 activate
-rw-r--r-- 1 dale dale 1446 Mar  3 19:46 activate.csh
-rw-r--r-- 1 dale dale 3077 Mar  3 19:46 activate.fish
-rw-r--r-- 1 dale dale 1751 Mar  3 19:46 activate.ps1
-rw-r--r-- 1 dale dale 1199 Mar  3 19:46 activate_this.py
-rw-r--r-- 1 dale dale 1168 Mar  3 19:46 activate.xsh
-rwxr-xr-x 1 dale dale  254 Mar  3 19:46 pip
-rwxr-xr-x 1 dale dale  254 Mar  3 19:46 pip3
-rwxr-xr-x 1 dale dale  254 Mar  3 19:46 pip-3.7
-rwxr-xr-x 1 dale dale  254 Mar  3 19:46 pip3.7
lrwxrwxrwx 1 dale dale   16 Mar  3 19:46 python -> /usr/bin/python3
lrwxrwxrwx 1 dale dale    6 Mar  3 19:46 python3 -> python
lrwxrwxrwx 1 dale dale    6 Mar  3 19:46 python3.7 -> python
-rwxr-xr-x 1 dale dale  241 Mar  3 19:46 wheel
-rwxr-xr-x 1 dale dale  241 Mar  3 19:46 wheel3
-rwxr-xr-x 1 dale dale  241 Mar  3 19:46 wheel-3.7
-rwxr-xr-x 1 dale dale  241 Mar  3 19:46 wheel3.7
```

The directory ```lib``` is where the Python packages are held. When pip is used to install a package in an activated virtual environment, the files are placed in a directrory in ```lib```.

### Using a Virtual Environment

To use a virtual environment:

1. Activate the virtual environment.
2. Do work in the activated virtual environment.
3. Deactivate the virtual environment.

To activate a virtual environment, do the following. The path to ```activate``` needs to be based on the current working directory, the name of your project/virtual environment directory, and the path to the ```activate``` program inside the project directory. The following assumes I am currently in the ~/Documents/spot folder that holds ```spotproject1``` and ```activate``` is inside ```bin```.

>source spotproject1/bin/activate

When the virtual environment is activated, the command prompt changes to the name of the directory for the environment. The following shows what happens when I run the command to activate.

>dale@p1:~/Documents/spot$ source spotproject1/bin/activate

```(spotproject1) dale@p1:~/Documents/spot$```

The above indicates that the ```spotproject1``` virtual environment has been activated.

While in the activated state, work on the project including installing packages that are placed in ```lib``` in the directory for the virtual environment.

To deactivate the virtual environment, do the following.

>deactivate

When I run deactivate, I get the following.

>(spotproject1) dale@p1:~/Documents/spot$ deactivate

>dale@p1:~/Documents/spot$

Notice that ```(spotproject1)``` is removed from the prompt after deactivating.

### Installing the Spot and other packages int the virtual environment

```pip``` is used to install packages in the virtual environment. Activate the virtual environment (see above) before doing any package management.

First make sure your virtual environment is activated. It is activated if the project directory is displayed in the prompt.

Use pip to install the Spot packages.

>$ python3 -m pip install --upgrade bosdyn-client bosdyn-mission bosdyn-choreography-client

You should see the installation taking place and it should end with no errors. The following is a partial display (middle part has been removed) of the installation that I performed.

>dale@p1:~/Documents/spot$ source spotproject1/bin/activate

```
(spotproject1) dale@p1:~/Documents/spot$ python3 -m pip install --upgrade bosdyn-client bosdyn-mission bosdyn-choreography-client
Collecting bosdyn-client
  Using cached bosdyn_client-2.3.2-py2.py3-none-any.whl (187 kB)
Collecting bosdyn-mission
  Using cached bosdyn_mission-2.3.2-py2.py3-none-any.whl (13 kB)
Collecting bosdyn-choreography-client
  Using cached bosdyn_choreography_client-2.3.2-py2.py3-none-any.whl (5.6 kB)
Collecting bosdyn-core==2.3.2
  Using cached bosdyn_core-2.3.2-py2.py3-none-any.whl (29 kB)
Collecting bosdyn-api==2.3.2
  Using cached bosdyn_api-2.3.2-py2.py3-none-any.whl (327 kB)
Collecting bosdyn-choreography-protos==2.3.2
.
.
.
bosdyn-core-2.3.2 bosdyn-mission-2.3.2 certifi-2020.12.5 chardet-4.0.0 grpcio-1.36.1 idna-2.10 numpy-1.20.1 protobuf-3.15.4 pyjwt-2.0.1 requests-2.25.1 six-1.15.0 urllib3-1.26.3 wrapt-1.12.1
```
>(spotproject1) dale@p1:~/Documents/spot$ 

If the files in the directory holding the packages are listed, the ```bosdyn``` packages are shown. The following is a partial listing from my installation.

>(spotproject1) dale@p1:~/Documents/spot/spotproject1/lib/python3.7/site-packages$ ls -al

```
total 224
drwxr-xr-x 42 dale dale  4096 Mar  3 20:30 .
drwxr-xr-x  3 dale dale  4096 Mar  3 19:46 ..
drwxr-xr-x  8 dale dale  4096 Mar  3 20:30 bosdyn
drwxr-xr-x  2 dale dale  4096 Mar  3 20:30 bosdyn_api-2.3.2.dist-info
drwxr-xr-x  2 dale dale  4096 Mar  3 20:30 bosdyn_choreography_client-2.3.2.dist-info
drwxr-xr-x  2 dale dale  4096 Mar  3 20:30 bosdyn_choreography_protos-2.3.2.dist-info
drwxr-xr-x  2 dale dale  4096 Mar  3 20:30 bosdyn_client-2.3.2.dist-info
drwxr-xr-x  2 dale dale  4096 Mar  3 20:30 bosdyn_core-2.3.2.dist-info
drwxr-xr-x  2 dale dale  4096 Mar  3 20:30 bosdyn_mission-2.3.2.dist-info
.
.
.
```

Packages other than those from Boston Dynamics can be installed in the virtual environment in the same way.

>python3 -m pip install --upgrade <package_name>

### Writing and running Python programs in the virtual environment

To write and run Python progrtam in the virtual environment do the following.

1. Activate the virtual environment.
2. Write/place your Python code in the directory for the virtual environment.
3. Run using: ```python3 <program_file.py>```
   
When you are done, deactivate the virtual environment.

