# Ryan

Common Python Tools

A bunch of Classes and Functions you can use across projects.

## Install

```
sudo pip install ryan
```

## Usage

```
import os
import ryan

CWD = os.path.dirname(os.path.abspath(__file__))

l = ryan.Logger('AS', CWD)
l.log('Starting script')

l.log(ryan.getTime())
```

## Todo

- [ ] More documentation