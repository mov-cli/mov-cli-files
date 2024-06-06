<div align="center">

  # mov-cli-files 
  <sub>A mov-cli v4 plugin for watching files on your device.</sub>
  
  ![grafik](https://github.com/mov-cli/mov-cli-files/assets/132799819/5f25ac19-de39-4b26-8121-c0f58f167c6b)

</div>

## Installation 🛠️
Here's how to install and add the plugin to mov-cli.

1. Install the package.
### PIP
```sh
pip install mov-cli-files
```

### AUR
```
yay -S python-mov-cli-files
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
mov-cli -s files {query}
```

### Example 🌟
Let's say I want to play an mp4 file in my Videos folder named "osaka_america_ya.mp4", this is the command you can use:
```sh
mov-cli -s files america ya
```

### Search in literal path 🔎
If you would like to quickly search in a path that is not scanned by the plugin use the ``path`` scraper option like so:
```sh
mov-cli -s files osaka oh my gah -- --path ./Downloads
```

### Give me EVERYTHING ✴️
If you would like to search for everything use the star chatacter (``*``) instead of entering a query like so:
```sh
mov-cli -s files "*"
```
