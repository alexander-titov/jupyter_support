# Intro
The repository contains scripts and notebooks implementing common functionality for [Jupyter](http://jupyter.org/) notebooks like hiding row code cells or an open file dialog.


# Installation
There are two modes of using the repository:
 * Git submodule (preferable for long usage)
 * Direct upload (fits for quick exploration)

## Submodule
This is a right way to include another repository into yours. As it is a large topic, only a very brief explanation is provided here. It is highly recommended to read [the full documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

In your repository, execute the following commands to add this repository as a submodule:
```
git submodule add https://github.com/alexander-titov/jupyter_support.git
git push origin master
```
It creates folder ```jupyter_support``` and uploads all the scripts and notebooks there. Then, you can start using them in your notebooks:

```python
from jupyter_support.hide_code_cells import hide_code_cells

hide_code_cells()
```

*Note!* If your clone a repository with submodules, you need to add ```--recursive``` argument in order to clone the submodules too. Thus, your repository now should be cloned as the following:
```
git clone --recursive https://github.com/username/project
```

## Direct upload
You can upload any script directly in your Notebook cell without any installation. The example below demonstrates how it can be done for ```hide_code_cells``` module:

```python
# Upload the script as a text string
import requests
url = 'https://raw.githubusercontent.com/alexander-titov/jupyter_support/master/hide_code_cells.py'
text = requests.get(url).text

# Execute the text string, which makes all the functions available
exec(text)

# Then, you can invoke them
hide_code_cells()
```
*Warining!* This approach is neither secure nor robust (e.g., the script can be suddenly moved or renamed). However, it works well for temporal notebooks or quick exploration of provided functionality.

### Proxy
If you work through a proxy, you have to configure it before uploading anything from github. Put the configuration parameters of your proxy into the following code and execute it in your notebook:
```python
import os
os.environ['http_proxy'] =  "http_proxy_url:port" 
os.environ['https_proxy'] = "https_proxy_url:port"
```

# Modules
## <code>hide_code_cells</code>
__In progress...__
