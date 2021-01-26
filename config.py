#!/usr/bin/env python
# -*- coding: utf-8 -*-


ShouldBotLog = True  # If False bot will not create and keep bot.log file
BLACKLIST = ['']  # You can add words to the blacklist. If a post contains a blacklisted word, the post will be skipped

reqVer = 5.103  # version of VK API [wall.get method]
reqCount = 3  # number of posts to return (2 - 100)
reqFilter = 'all'  # Filter to apply: owner — posts by the wall owner; others — posts by someone else;
                     # all — posts by the wall owner and others (default)
                     # postponed — timed posts (only available for calls with an access_token)
                     # suggests — suggested posts on a community wall

singleStart = False
timeSleep = 60 * 2  # time in seconds
isPinned = False
skipAdsPosts = True

parsePost = True  # bot will skip just text posts if the value is False
parsePhoto = True  # bot will skip photo posts if the value is False
parseVideo = True  # bot will skip video posts if the value is False
parseLink = True  # bot will skip posts with link if the value is False
parseDoc = True  # bot will skip posts with docs/gif if the value is False

proxyEnable = False  # Set True if telegram is not available in your country
proxyLogin = "bot"  # Login for Socks5 proxy
proxyPass = "12345"  # Password for Socks5 proxy
proxyIp = "myproxy.com"  # Socks5 proxy ip
proxyPort = "1234"  # Socks5 proxy port
