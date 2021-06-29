# apache_airflow (2.0)

### Differences in installation of Apache Airflow 1.0 and 2.0

https://medium.com/apache-airflow/airflow-2-0-providers-1bd21ba3bd93


### System Dependencies for Apache Airflow

I am running this project off of an Xubuntu VM (Version 18.041). According to the installation guide here, https://airflow.apache.org/docs/apache-airflow/stable/installation.html#prerequisites, we will need to install some prerequisites.

**to install system dependencies**, run the command 

``./install_system_dependencies.sh``

you may need to make the script executable first if you get a permissions error, e.g.

`chmod +x install_system_dependencies.sh`

### Creating Virtual Environment

#### system dependencies

Because this is a fresh VM, I hadn't installed python's venv package. to install the package required to create the virtual environment, run

`./install_venv.sh`

you will also need to install the curl package , as the project uses this bash command

`./install_curl.sh`

#### creating the virtual environment

I named my virtual environment after the project folder. To create a virtual environment, run the following command in the project folder directory

`python3 -m venv airflow`

#### activating the virtual environment

`source airflow/bin/activate` 

##### Installing Apache Airflow

After the virtual environment is activated you should see the name of the virtual environment in on the left hand side of your user name on the command line in the terminal.

For example, mine changed from 

`tdepries@tdepries-VirtualBox:~/git_repos/apache_airflow$`

to

`(airflow) tdepries@tdepries-VirtualBox:~/git_repos/apache_airflow$`

after activating the virtual environment.

Once the virtual environment is activated, you can install apache airflow in the virtual environment by running the shell script and command













