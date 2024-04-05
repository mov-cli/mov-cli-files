<div align="center">

  # mov-cli-files 
  <sub>A mov-cli v4 plugin for watching files on your device.</sub>

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
