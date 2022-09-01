## 💰🦝 thievius!
<img src='https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white'/> <img src='https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white'/> <img src ='https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue'/> 

- [⚠️ **disclaimer**](https://github.com/cr-0w/thievius#-disclaimer)
- [💽 **download**](https://github.com/cr-0w/thievius#-installation)
- [🎉 **usage**](https://github.com/cr-0w/thievius#-usage)
- [🚧 **to-do**](https://github.com/cr-0w/thievius#-to-do)
- [💖 **credits**](https://github.com/cr-0w/thievius#-credits)

Welcome back! I've created my second tool; a username generator called `thievius!`. Picture the following scenario, you land on a web-application, start crawling through it only to find the faces of the company's employees plastered all over the site. Oh, and their first and last names are there as well. Hm. What do you do? Well, you could barbarically type out their names and transform them into common usernames by hand. Or... you could use `thieveus!`

![demo](https://github.com/cr-0w/thievius/blob/main/demo/demo.gif)

This tool uses the amazing work of [Dzmitry Savitski](https://github.com/dzmitry-savitski)'s John the Ripper username generation [rules](https://dzmitry-savitski.github.io/2020/04/generate-a-user-name-list-for-brute-force-from-first-and-last-name). 

## ⚡ Disclaimer! 
This tool generates usernames from first and last names. Lord knows what you're going to end up doing with those usernames but this tool, and its author, do not condone the use of using `thievius!` for malicious and unauthorized activities against anything you do not have explicit permission to do so.
- This is my second tool now, but I'm still far from being a "good" programmer so I'll try to update this script with more QoL-stuff and I'll try to fix any issues that may arise!


## ⭐ Installation
To install the program, you can just download this repository and run the `install.sh` script.
```
git clone https://github.com/cr-0w/thievius.git && cd thievius/
python3 -m pip install -r requirements.txt
chmod +x install.sh
./install.sh
```
![install](https://github.com/cr-0w/thievius/blob/main/demo/install.gif)

## 🩸 Usage 
For now, since I haven't implemented user-args, you can just run the script and enter in data one-by-one: 
```
python thievius.py # or ./thievius.py
```
> *Fret not, good friend. I'm currently working on parsing user arguments for the program to make this more efficient.*

## 🚧 To-Do 
- `add in support for user-supplied arguments`
- `add in support to create emails by specifing a domain`

## 💖 Credits 
A special thank you goes out to **Dzmitry Savitski** and his super cool blog post!
> @[Dzmitry Savitski](https://github.com/dzmitry-savitski),
["Generate a user name list for brute force from first and last name"](https://dzmitry-savitski.github.io/2020/04/generate-a-user-name-list-for-brute-force-from-first-and-last-name)
