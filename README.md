# Lie-brary
### "bringing clarity to the chaos of online information"


## What is Lie-brary?
Our project’s goal is to analyze subjects that were misconstrued on social media (such as health misinfo or backlash against a law) to understand the construction and spread of certain myths. We are also considering leveraging GPT/our own messaging templates to build communication to myth-bust and help counter misinformation.  Note that we will define misinformation on the basis of what has been fact-checked as false through [International Fact-Checking Network](https://www.poynter.org/ifcn/) approved sources and [InjusticeWatch](https://www.injusticewatch.org/news/prisons-and-jails/2022/safe-t-act-purge-law-illinois-fact-check/) (NGO advocating for SAFE-T Act).

## About the data
Our first step was to scrape data from social media sites, Twitter and Reddit, via their APIs. We attempted to scrape data from Meta but found that access to developers was extremely limited and largely restricted to Ads Library information -- which would mean that our data would not be balanced with other sources (inorganic Ads versus organic content from Reddit or Twitter). We already had access to a Twitter API key and found Reddit highly accessible which tipped the scales in favor of these platforms.

To ensure parallelism of our data, we also discounted YouTube or TikTok. This is because we pulled text/post information from Twitter and Reddit; the difference in entity types (videos/short reels) would corrupt our analysis as it would mean that our sample groups were unbalanced.

Note that the following impositions applied to scraping from these platforms:
- Twitter: the search index had a 7 day limit and pulled data only for the preceding week
- Reddit: limited pulls to 200 posts while using requests + difficulting in filtering specific keywords

## How our files interact?
![image](lie_brary/assets/concept.png)


## Process overview
![image](lie_brary/assets/liebrary_diagram.png)


## How to run the project?

### Using Poetry
1. Make the clone of the project repository
```sh
git clone https://github.com/uchicago-capp122-spring23/30122-project-lie-brary.git
```
2. Install virtual environment and dependencies using poetry
```sh
poetry install
```
3. Activate the virtual environment
```sh
poetry shell
```
4. Run the project

a. For running the dashboard
```sh
python -m lie_brary dashboard
```
b. For running the script to update the data
```sh
python -m lie_brary getdata
```

## Current Build:
[Dashboard](http://rezarzky.my.id:8051/)
