@theyspentwhat is a Twitter bot that answers queries about local government spending, using the spending data councils are now required to publish.

It is structured as three modules that are chained together like so:

  twitter-search "@theyspentwhat" | theyspentwhat | twitter-reply

Data is passed between processes as a stream of JSON-formatted tweets, one per line. The processes are as follows:

twitter-search: Uses the Twitter streaming API to stream all tweets addressed to @theyspentwhat, and print them to standard output.

theyspentwhat: The core of the application. Reads tweets on standard input, parses the text of the tweet, and composes a helpful reply which is written to standard output in JSON format.

twitter-reply: Reads tweets from standard input, one per line in JSON format, and posts them to Twitter.

[XXXX - The twitter-search and twitter-reply processes will need to receive authentication credentials somehow. Passing these on the command-line would expose them to other local users of the system, so it should be either in the environment or via a configuration file whose name is given on the command-line.]

-- [Author name redacted], 2011-03-02
