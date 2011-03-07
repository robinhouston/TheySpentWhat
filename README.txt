INTRODUCTION

@theyspentwhat is a Twitter bot that answers queries about local government spending, using the spending data councils are now required to publish.


TWEET FORMAT

Here are some example tweets, with explanation:

Give the name of a council and the name of a company:
  @theyspentwhat in Islington on Alphatrack?
  @theyspentwhat with Alphatrack in Islington?

Time periods (months or years) can also be specified:
  @theyspentwhat in Islington on Alphatrack during 2010?
  @theyspentwhat in Islington on Alphatrack during April 2010?

You can also use a leading dot in your tweet, so your followers will see the question too:
  .@theyspentwhat in Islington on Alphatrack?

The bot looks for the following keywords in the tweet to determine its meaning:
  in <council name>
  on/with <company name>
  during <month/year>

If no time period is specified, the bot will answer for the whole year of 2010.

If a tweet has multiple equally-good interpretations then the bot will choose
the most interesting of the possible answers. To the bot, "more interesting"
is synonymous with "involving a larger amount of money".

For example, the laconic query "@theyspentwhat in Cambridgeshire" will elicit
the response: "Cambridgeshire County Council spent £94,335,430.63 total during
2010" on the grounds that Cambridgeshire County Council is more interesting
than either East Cambridgeshire or South Cambridgeshire. On the other hand,
"@theyspentwhat with Invicta in Cambridgeshire" gives "South Cambridgeshire
spent £4,833,341.26 with INVICTA TELECARE LTD during 2010", since South
Cambridgeshire spent more with Invicta Telecare during 2010 than did either of
the other councils with Cambridgeshire in their name.


HOW TO RUN IT

See the file RUNNING.txt


STRUCTURE

The application is structured as three modules that are chained together like
so:

  twitter-search "@theyspentwhat" | theyspentwhat | tweet

Data is passed between processes as a stream of JSON-formatted tweets, one per
line. The processes are as follows:

twitter-search: Uses the Twitter streaming API to stream all tweets addressed
to @theyspentwhat, and print them to standard output.

theyspentwhat: The core of the application. Reads tweets on standard input,
parses the text of the tweet, and composes a reply which is written to standard
output.

tweet: Reads tweets from standard input and posts them to Twitter.

-- [Author name redacted], 2011-03
