import random

data = {
    "title": "readme-generator",
    "description": """Readme generator python script.  
The project generates readme file. """,
"features": ["Generates badges","Generate markdown file"],
"list_badges": ["javaScript","css3","html5","python","latex"],
"steps":["Edit data section python file","python readme_generator.py"],
"FAQ":{"Are there any depencdecy":"No","what are import":"random package"},
"dependencies":["random"],
}

def ufunc_lst2str(inpt_list):
    inpt_list = ["- " + item + "\n" for item in inpt_list]
    opt_str = "".join(inpt_list)
    return opt_str

def ufunc_dict2str(inpt_dict):
    opt_str = ""
    for (key, value) in inpt_dict.items():
        t_str = f"""> {key}?    \n   {value}.    \n   \n"""
        opt_str += t_str
    return opt_str

def ufunc_badgegen(list_badges):
    tlist_badgegen = []
    for i in list_badges:
        badge_label = i.capitalize()
        badge_logo = i
        badge_color = ''.join([random.choice('ABCDEF0123456789') for _ in range(6)])
        logo_color =  '000' if int(str(badge_color),16) > int(str('7FFFFF'),16) else 'fff'
        _badgegen = f"![](https://img.shields.io/badge/{badge_label}-{badge_color}?style=for-the-badge&logo={badge_logo}&logoColor={logo_color})"
        tlist_badgegen.append(_badgegen+" ")
    tstr_badgen = "".join(tlist_badgegen)
    return tstr_badgen

doc = f""" 
<!-- PROJECT Banner ![Readme](./Designer%20(3).png)-->
![SVG Banners](https://svg-banners.vercel.app/api?type=luminance&text1={data['title']}&width=1020&height=460)
<!-- PROJECT TITLE --> <!-- <a name="readme-top"></a> -->
# {data['title']} <!-- PROJECT LOGO ![Readme](./Designer%20(3).png) -->

<!-- PROJECT SHIELDS -->
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/charudatta10/{data['title']}?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/charudatta10/{data['title']})
![GitHub issues](https://img.shields.io/github/issues-raw/charudatta10/{data['title']})
![GitHub pull requests](https://img.shields.io/github/issues-pr/charudatta10/{data['title']})
![GitHub](https://img.shields.io/github/license/charudatta10/{data['title']})

<!-- Project Description -->
{data['description']}  

<!-- SHARING ON SOCIAL MEDIA -->

<!-- TABLE OF CONTENTS -->

## Project Preview 📖 <!-- Usage screenshots -->

There's a live preview on this [website](https://charudatta10.github.io/linktree/)!

<!-- <p align="right"><a href="#readme-top">Jump to Top<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand gestures/Index Pointing Up.png" alt="Pointing Up" width="25" height="25" /></a></p>
-->

## Features 🌟

{ ufunc_lst2str(data['features'])}

## Built With 🔧
{ufunc_badgegen(data['list_badges'])}

<!-- GETTING STARTED -->

## Getting Started 🌱

### Dependencies ⧉

{ ufunc_lst2str(data['dependencies'])}

### Installation ■■■■■■■■■■

1. To install from binaries:  
   Download the binary file from the release and double-click to use it.

2. To install from source:

```PowerShell
gh repo clone charudatta10/{data['title']}
```
 
### How to use 🗎

{ ufunc_lst2str(data['steps'])}

## FAQ ?

✨[Report a 🐛 or Request a ⭐](https://github.com/charudatta10/{data['title']}/issues)✨

{ufunc_dict2str(data['FAQ'])}

<!-- CONTRIBUTING -->

## Authors 👱

The author of this project is @charudatta10.  

## Contributors 👪

| ![](profile-picture.png) |
| :---: | 
| Charudatta Korde |
| [💻](#code-charudatta10)  [📖](#doc-charudatta10)  [🎨](#design-charudatta10)  [💡](#example-charudatta10)  [🤔](#ideas-charudatta10)|


### Contribution guidelines

The contribution to this project should adhere to GPL-3.0 and respect the copyright claims of charudatta10.

## License 📜

Copyright :copyright: 2024 ![ck](favicon05.svg):tm: @ charudatta10.   
The project is licensed [GPL-3.0](./LICENSE).

"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(doc)
# print(doc)
