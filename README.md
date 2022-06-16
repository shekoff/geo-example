1.Install pyenv 

   https://github.com/pyenv/pyenv-installer
   
   https://github.com/pyenv/pyenv
   
2.Install dependances

   Ubuntu:
   
       ```sudo apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget libsqlite3-dev libbz2-dev libgdal-dev liblzma-dev```


3.Install python version i.e 3.6.1
  
  ```pyenv install 3.6.1```
  
4.Create virtual env
   
   ```pyenv virtualenv 3.6.1 geo```
   
5.Select it :
  
  ```pyenv activate geo```
  
6. Update pip
  
  ```pip install --upgrade pip```
  
7.Install python packages

```pip install -r requirements.txt```
  
8.Rund the example
  ```python convert.py````

9.open geojson.io and visualize the content of list.geojson
