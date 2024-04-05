<div align="center">

  # mov-cli-files 
  <sub>A mov-cli v4 plugin for watching files on your device.</sub>
  
  ![grafik](https://github.com/mov-cli/mov-cli-files/assets/132799819/5f25ac19-de39-4b26-8121-c0f58f167c6b)

</div>


## Installation 🛠️
Here's how to install and add the plugin to mov-cli.

1. Install the pip package.
```sh
pip install mov-cli-files
```
2. Then add the plugin to your mov-cli config.
```sh
mov-cli -e
```
```toml
[mov-cli.plugins]
files = "mov-cli-files"
```

## Usage 🖱️
```sh
mov-cli -s files PATH
```
