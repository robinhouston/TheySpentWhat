INTRODUCTION

@theyspentwhat is a Twitter bot that answers queries about local government spending, using the spending data councils are now required to publish.

TWEET FORMAT

Here are some example tweets, with explanation:

Give the name of a council and the name of a company:
  @theyspentwhat in Islington on Alphatrack?

Time periods (months or years) can also be specified:
  @theyspentwhat in Islington on Alphatrack during 2010?
  @theyspentwhat in Islington on Alphatrack during April 2010?

[XXXX - the following if there is time, or possibly to be added tomorrow if there isn't time tonight]
Specifying a council by partial postcode, rather than name:
  @theyspentwhat in N1 on Alphatrack?

Using a geo-tagged tweet to describe the location:
  @theyspentwhat on Alphatrack here?
[XXXX - end of "if there is time" section]

You can also use a leading dot in your tweet, so your followers will see the question too:
  .@theyspentwhat in Islington on Alphatrack?

MODULAR STRUCTURE

The application is structured as three modules that are chained together like so:

  twitter-search "@theyspentwhat" | theyspentwhat | tweet

Data is passed between processes as a stream of JSON-formatted tweets, one per line. The processes are as follows:

twitter-search: Uses the Twitter streaming API to stream all tweets addressed to @theyspentwhat, and print them to standard output.

theyspentwhat: The core of the application. Reads tweets on standard input, parses the text of the tweet, and composes a helpful reply which is written to standard output in JSON format.

tweet: Reads tweets from standard input, one per line in JSON format, and posts them to Twitter.

[XXXX - The twitter-search and twitter-reply processes will need to receive authentication credentials somehow. Passing these on the command-line would expose them to other local users of the system, so it should be either in the environment or via a configuration file whose name is given on the command-line.]

-- [Author name redacted], 2011-03-02
