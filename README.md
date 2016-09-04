# MutualFollowFinder

MutualFollowFinder is a python console application that takes two Twitter handles as command line arguments and prints the users that they are both following on Twitter. Created using the python-twitter api. Twitter api rate limits prevent the application from being used too much within a certain timeframe, and limit the application to working with two twitter handles at a time.

<h2>Prerequisites</h2>
<ul>
  <li>Install python-twitter: <a>https://github.com/bear/python-twitter</a></li>
  <li>Go to apps.twitter.com. Create a new application using a twitter account and use the given keys to fill in the CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET variable to get permissions to use the application</li>
</ul>
  
<h2>Usage example</h2>

```
$ python mutualfollows.py porterrobinson anamanaguchi
```
