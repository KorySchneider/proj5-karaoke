# proj5-karaoke

## What is this?  
This is an essential tool for any karaoke enthusiast. Sometimes you may find yourself in Eugene, Oregon and think, "Dang, it's been a while since I've been to a karaoke joint." It's times like these when all you need to do is

    $ cd /path/to/enlightenment
    $ git clone https://github.com/koryschneider/proj5-karaoke karaoke
    $ cd karaoke
    $ bash configure && make service

and feel your troubles melt away.

## Usage

`$ make service` will start a Green Unicorn ([gunicorn](http://gunicorn.org/)) server.

`$ make run` will launch the server in debugging mode.

## Contribute

The list of hip karaoke establishments is found in `poi.json`. This is an open source project, so feel free to contribute to the list at https://github.com/koryschneider/proj5-karaoke/pulls.

## About

This is a project for CIS 322: Intro to Software Engineering at the University of Oregon; Fall 2016
