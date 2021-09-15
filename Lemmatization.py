# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# paragraph =  """I have three visions for India. In 3000 years of our history, people from all over
#                the world have come and invaded us, captured our lands, conquered our minds.
#                From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
#                the French, the Dutch, all of them came and looted us, took over what was ours.
#                Yet we have not done this to any other nation. We have not conquered anyone.
#                We have not grabbed their land, their culture,
#                their history and tried to enforce our way of life on them.
#                Why? Because we respect the freedom of others.That is why my
#                first vision is that of freedom. I believe that India got its first vision of
#                this in 1857, when we started the War of Independence. It is this freedom that
#                we must protect and nurture and build on. If we are not free, no one will respect us.
#                My second vision for India’s development. For fifty years we have been a developing nation.
#                It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
#                in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
#                Our achievements are being globally recognised today. Yet we lack the self-confidence to
#                see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
#                I have a third vision. India must stand up to the world. Because I believe that unless India
#                stands up to the world, no one will respect us. Only strength respects strength. We must be
#                strong not only as a military power but also as an economic power. Both must go hand-in-hand.
#                My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of
#                space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
#                I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.
#                I see four milestones in my career"""
#
# sentences = nltk.sent_tokenize(paragraph)
# lemmatizer = WordNetLemmatizer()
#
# for i in range(len(sentences)):
#     words = nltk.word_tokenize(sentences[i])
#     words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
#     sentences = ' '.join(words)
# print(sentences)

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

paragraph = """Thank you all so very much. Thank you to the Academy. 
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               and crew. First off, to my brother in this endeavor, Mr. Tom 
               Hardy. Tom, your talent on screen can only be surpassed by 
               your friendship off screen … thank you for creating a t
               ranscendent cinematic experience. Thank you to everybody at 
               Fox and New Regency … my entire team. I have to thank 
               everyone from the very onset of my career … To my parents; 
               none of this would be possible without you. And to my 
               friends, I love you dearly; you know who you are. And lastly,
               I just want to say this: Making The Revenant was about
               man's relationship to the natural world. A world that we
               collectively felt in 2015 as the hottest year in recorded
               history. Our production needed to move to the southern
               tip of this planet just to be able to find snow. Climate
               change is real, it is happening right now. It is the most
               urgent threat facing our entire species, and we need to work
               collectively together and stop procrastinating. We need to
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""

sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

# Lemmatization
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])s
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)
print(sentences)
