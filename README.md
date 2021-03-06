# MutualFollowFinder

MutualFollowFinder is a python console application that takes two Twitter handles as command line arguments and prints the users that they are both following on Twitter. Created using the python-twitter api. Twitter api rate limits prevent the application from being used too much within a certain timeframe, and limit the application to working with two twitter handles at a time.

<h2>Prerequisites</h2>
<ul>
  <li>Install python-twitter: <a>https://github.com/bear/python-twitter</a></li>
  <li>Go to apps.twitter.com. Create a new application using a twitter account and use the given keys to fill in the CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET variables to get permissions to use the application</li>
</ul>
  
<h2>Usage</h2>

<h3>Getting the code</h3>
```
$ git clone https://github.com/GenericAlias/MutualFollowFinder.git
$ cd MutualFollowFinder
```

<h3>Usage example</h3>
```
$ python mutualfollows.py porterrobinson anamanaguchi
```

This command prints the following result:

```
Users:
['porterrobinson', 'anamanaguchi']

Mutual following:
[u'arcanekids',
 u'RUSTIE',
 u'waltzforluma',
 u'infinity_shred',
 u'Kosuke_Adam',
 u'feedme',
 u'TOKiMONSTA',
 u'Carpainter_TT',
 u'lh4l',
 u'chibitech',
 u'MisterGIF',
 u'texxyson',
 u'davidoreilly',
 u'flumemusic',
 u'wearegalantis',
 u'chromesparks',
 u'whosaazar',
 u'Tomggg',
 u'OWSLA',
 u'Popjustice',
 u'masayoshi_JP',
 u'seiho777',
 u'Arimuri',
 u'giraffage',
 u'reachyasi',
 u'Crunchyroll',
 u'Garethmcgrillen',
 u'the_roadhog',
 u'Skrillex',
 u'CAPSULEOFFICIAL',
 u'Sarah_Bonito_',
 u'knifepartyinc',
 u'nathanfielder',
 u'markredito',
 u'FLOSSTRADAMUS',
 u'PointPointParis',
 u'diversamusic',
 u'oooKoSHIooo',
 u'mikuexpo',
 u'TEEDinosaurs',
 u'AWEmygod',
 u'NESTHQ',
 u'pcmus',
 u'ALESIAmusic',
 u'ninalasvegas',
 u'fu_mou',
 u'AlvinRisk',
 u'rob_swire',
 u'georgeNjonathan',
 u'haraqlo',
 u'absrdst',
 u'netskymusic',
 u'kokosac',
 u'tiesto',
 u'mbmelodies',
 u'parkgolfeee',
 u'madeon',
 u'CHVRCHES',
 u'Hannahdiamond_',
 u'PasLamSystem',
 u'MartinGarrix',
 u'likeluke_',
 u'seimei1992',
 u'Image_Line',
 u'bloodpop',
 u'manilakilla',
 u'peterberkman',
 u'nanobii',
 u'yuzurusato',
 u'_Met0me_',
 u'_omocat',
 u'starsmith',
 u'kanyewest',
 u'tennysonmusic',
 u'toriena',
 u'DeonCustom',
 u'Andyproblems',
 u'planetofdoom',
 u'DJWILDPARTY',
 u'FL_Studio',
 u'boysnoize',
 u'chadsalty',
 u'YungGroupon',
 u'S2TB_korsk',
 u'HudMo',
 u'galaxxxy_Japan',
 u'_Qrion_',
 u'LiteralRobinson',
 u'artonaline',
 u'tanukimusic',
 u'chordslayermaxo',
 u'stereogum',
 u'sailorbee',
 u'MeishiSmile',
 u'pamyurin',
 u'bitvargen',
 u'masayoshiiimori',
 u'ConorTripler',
 u'ryanhemsworth',
 u'CalumBowen',
 u'koansound',
 u'Colasplash',
 u'charli_xcx',
 u'waveracermusic',
 u'nice__feelings',
 u'bahijd',
 u'CosmosMidnight',
 u'CRNKN',
 u'killthenoise',
 u'osheaga',
 u'pitchfork',
 u'DILLONFRANCIS',
 u'boenyeah',
 u'MUSTDIEmusic',
 u'tomad',
 u'WeAreOliver',
 u'Mat_Zo',
 u'OJessicaNigri',
 u'atrak',
 u'Elleanor_deFOB',
 u'steve_duda',
 u'Babylonian',
 u'alexyoungbased',
 u'SugarsCampaign',
 u'tofubeats',
 u'eprombeats',
 u'Groundislava',
 u'mitchgrassi',
 u'rukes',
 u'thefader',
 u'torahhorse',
 u'ericprydz',
 u'georgealways',
 u'TREKKIETRAX',
 u'RAC',
 u'lfitzmaurice',
 u'CorySchmitz',
 u'12thplanet',
 u'merlinthegirl',
 u'LILINTERNET',
 u'annalunoe',
 u'TJANI',
 u'skylar__spence',
 u'whoispenny',
 u'Ghostdad',
 u'LILBTHEBASEDGOD',
 u'rogerclark',
 u'diplo',
 u'SPF420INC',
 u'setoayumi',
 u'JonahBaseball',
 u'KeroKeroBonito',
 u'MaltineRecords',
 u'DJGammer',
 u'Astralwerks',
 u'odesza',
 u'linalovesit',
 u'sushimonstuh',
 u'Zedd',
 u'CASHMERECAT',
 u'djembahh',
 u'MAJORLAZER',
 u'ZoomLensLabel',
 u'nomak_music',
 u'ecchiparty',
 u'kylemooney',
 u'deadlyclaris',
 u'thatPoppy']
 ```

