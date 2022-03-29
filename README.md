# Remotweet-140

This program enables its user to tweet without needing to use the Twitter client.
The tweets published through this program are also limited to 140 characters, like all tweets used to be.

Why? 
- Constraint drives not only creativity, but also impact. 
- Compressing your thoughts into 140 characters forces you to refine what you want to say:
  this is a wonderful means for training your own thinking and expression into being more succinct.
- "Simplicity is the highest sophistication." - Leonardo Da Vinci

Why would I want to tweet without having Twitter open?
- This program is intended for the tweeters who wish to channel their own ideas and thoughts without risking them being
  diluted or affected by the superstimuli on this platform. In short, to curb distraction.

NOTE: Every tweet sent through this program will show the name of the application associated with your API keys (as the device name). 
You can change it to whatever you wish in the developer portal.

******************************************************************************

INSTRUCTIONS:

Before using this app, you have to have a Twitter account with access to the Twitter API.

Input your API access keys to the text file entitled "twitterkeys.txt", in the following order:
	1. API key
	2. Secret API key
	3. Access token
	4. Secret access token.

Write the tweet you want to publish into the text file entitled "Tweet.txt".
The program reads the text file, prints out the character count of the tweet on the prompt, and asks for confirmation before the tweet is sent. 
By typing "yes" and pressing enter the tweet is published.
 
If the character count exceeds 140, the program prints out an error message
containing the number of excess characters.

******************************************************************************

V*0.2.
Under construction: a GUI remote tweeter

*C Lauri Paronen
