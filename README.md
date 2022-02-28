# NewsUpdate
#### By Melody Chepkorir
## Table of Content
+ [Description](#description)
+ [Installation Requirement](#Installation)
+ [Behaviour Driven Development](#Behaviour-Driven-Development)
+ [Technology Used](#technology-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

****
## Description
Application that helps one get news update incase they miss to watch news at anytime they want. The site shows different articles from different sources and authors. It consumes the NEWS API

## Live link
`https://newsupdate.herokuapp.com/`
## Installation
### Requirements
* python3.9
* pip 
### Installation process
* Open terminal
* run `git clone https://github.com/melodytowett/news-update.git`

### Dependancy Installation process
```
$ pip install -r requirements.txt

```

### Running the Application
To view the website run the command
```
$ chmod a+x start.sh
$ ./start.sh

```
To run the tests run the command
```
$ python3.9 manage.py test

```
## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display top headlines | page loads | Top headlines and a list various sources is displayed|
| Search for topic  | user searches topic of interest| News articles in that topic are displayed|
| Read an article  | user clicks on article displayed | user is redirected to  source page|
| Display news in category | user clicks on category link | News articles in that category are displayed |

****


## Licence
MIT License

Copyright (c) 2022 Melody Towett

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


****


## Aythors Infor:
Email melodytowett.student@moringaschool.com