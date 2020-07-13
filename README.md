# 🗄️ Renamer

Python script for renaming files by given names or regular expression. Originally written to rename episodes of serials/cartoons but can be easily changed for any purpose.

![Renamer screenshot](https://habrastorage.org/webt/zf/4o/3u/zf4o3udqbsf3tatcuwoxybl9kae.png)


## 📦 Requirements
* python 3.6+


## 🚀 Usage
0. Download [script](https://raw.githubusercontent.com/alsolovyev/renamer/master/main.py)
1. Add list of names
2. Run the script
```
python main.py -d "~/Movies/According to Jim" -e mkv
```


## Options
```
-h, --help            show this help message and exit
-d DIRECTORY, --directory DIRECTORY
                      path to the directory with files
-e EXTENSION, --extension EXTENSION
                      files extension for search
-r, --regex           use regular expressions
```


## Task list
- [x] ~~Add arguments for easy use~~


## Authors
* **[Aleksey Solovyev](https://github.com/alsolovyev)** - [solovyev.a@icloud.com](mailto:solovyev.a@icloud.com)


## License
This project is licensed under the [MIT](./LICENSE) License
