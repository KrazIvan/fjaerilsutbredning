# Fjärilsutbredning #
The purple emperor butterfly (sälgskimmerfjäril) can be found in many parts of Europe, but has until recently
only been seen occasionally in the southernmost parts of Sweden. In the past several years, however, it has
begun to spread north. This program investigates its spread over Sweden in the past 25 years with the
help of observation data from Artdatabanken (a site from SLU, Sveriges lantbruksuniversitet).


## This program answers the following questions: ##
• At what rate has the purple emperor spread northward?

• How has the number of observations changed over time?

• When did the purple emperor arrive in Gotland?

• What time of the year is the purple emperor active?

## Data ##
The data used is in the 25_years_of_salgskimmer.csv file, which contains
four comma-separated columns with information on observations of the purple emperor. The two first columns
are latitude and longitude, which describe where the observation took place (though hardly with the implied
precision). The third column contains information on the date and time in a somewhat mysterious format.
Take for example 2021-07-28T22:00:00.0000000Z: the date is in the standard format, but separated from the
time with the character T.

The time is also in the standard format, but with a bizarre amount of precision and
terminated with the letter Z. The fourth column contains the number of butterflies reported in the observation.
In total, the data contains 5239 observations.

This is a filtered version of the data you can download from
SLU’s site https://www.artdatabanken.se. Irrelevant data and personal information (the observers’ names)
have been removed.
