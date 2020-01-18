#!/usr/bin/env python
# coding: utf-8

# ***Scraping the data***

# In[1]:


# Import the needed packages
import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import numpy as np


# In[2]:


### Scrap movies of Steven Spielberg ###
## IMDB_Spider1
# Create the Spider class1
class IMDB_Spider1(scrapy.Spider):
  name = "IMDB_spider1"
  # start_requests method
  def start_requests( self ):
    url = 'https://www.imdb.com/name/nm0000229/?ref_=nv_sr_srsg_0'
    yield scrapy.Request( url = url,
                         callback = self.parse_front )
  # First parsing method
  def parse_front(self, response):
    links_to_follow = response.xpath('//*[contains(@class,"filmo-row even")]/b/a/@href').extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
 # Second parsing method
  def parse_pages(self, response):
    title = response.css('h1::text').extract_first().strip()
    year = response.css('#titleYear a::text').extract_first()
    rating = response.css('.subtext::text').extract_first().strip() or None
    users_rating = response.xpath('//span[contains(@itemprop, "ratingValue")]/text()').extract_first()
    votes = response.xpath('//span[contains(@itemprop, "ratingCount")]/text()').extract_first()
    metascore = response.xpath('//div[contains(@class, "metacriticScore")]/span/text()').extract_first()
    countries = response.xpath('//div[contains(@class, "txt-block") and contains(.//h4, "Country")]/a/text()').extract()
    countries = [country.strip() for country in countries]
    languages = response.xpath('//div[contains(@class, "txt-block") and contains(.//h4, "Language")]/a/text()').extract()
    languages = [language.strip() for language in languages]
    actors = response.xpath('//td[not(@class)]/a/text()').extract()
    actors = [actor.strip() for actor in actors]
    tagline = response.xpath('//div[contains(string(), "Tagline")]/text()').extract()
    tagline = ''.join(tagline).strip() or None
    directors = response.xpath("//div[contains(@class, 'credit_summary_item') and contains(.//h4, 'Director')]/a/text()").extract() or None
    directors = [director.strip() for director in directors]
    genres =  response.xpath("//*[@id='titleStoryLine']/div[4]/a/text()").extract()
    budget = response.xpath("//*[@id='titleDetails']/div[7]/text()").extract()
    opening_week_us =response.xpath("//*[@id='titleDetails']/div[8]/text()").extract() 
    gross_usa = response.xpath("//*[@id='titleDetails']/div[9]/text()").extract()
    world_wide_box_office = response.xpath("//*[@id='titleDetails']/div[10]/text()").extract()
    imdb_url = response.url.replace('?ref_=adv_li_tt', '')
    budget_1 = response.xpath("//*[@id='titleDetails']/div[6]/text()").extract()
    opening_week_us_1 =response.xpath("//*[@id='titleDetails']/div[7]/text()").extract() 
    gross_usa_1 = response.xpath("//*[@id='titleDetails']/div[8]/text()").extract()
    world_wide_box_office_1 = response.xpath("//*[@id='titleDetails']/div[9]/text()").extract()
    mv1_dict[title] = year, rating, users_rating, votes, metascore, countries, languages, actors, tagline, directors, genres, budget, opening_week_us, gross_usa, world_wide_box_office, imdb_url, budget_1, opening_week_us_1, gross_usa_1, world_wide_box_office_1
    
## IMDB_Spider2
# Create the Spider class2
class IMDB_Spider2(scrapy.Spider):
  name = "IMDB_spider2"
  # start_requests method
  def start_requests( self ):
    url = 'https://www.imdb.com/name/nm0000229/?ref_=nv_sr_srsg_0'
    yield scrapy.Request( url = url,
                         callback = self.parse_front )
  # First parsing method
  def parse_front(self, response):
    links_to_follow = response.xpath('//*[contains(@class,"filmo-row odd")]/b/a/@href').extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
 # Second parsing method
  def parse_pages(self, response):
    title = response.css('h1::text').extract_first().strip()
    year = response.css('#titleYear a::text').extract_first()
    rating = response.css('.subtext::text').extract_first().strip() or None
    users_rating = response.xpath('//span[contains(@itemprop, "ratingValue")]/text()').extract_first()
    votes = response.xpath('//span[contains(@itemprop, "ratingCount")]/text()').extract_first()
    metascore = response.xpath('//div[contains(@class, "metacriticScore")]/span/text()').extract_first()
    countries = response.xpath('//div[contains(@class, "txt-block") and contains(.//h4, "Country")]/a/text()').extract()
    countries = [country.strip() for country in countries]
    languages = response.xpath('//div[contains(@class, "txt-block") and contains(.//h4, "Language")]/a/text()').extract()
    languages = [language.strip() for language in languages]
    actors = response.xpath('//td[not(@class)]/a/text()').extract()
    actors = [actor.strip() for actor in actors]
    tagline = response.xpath('//div[contains(string(), "Tagline")]/text()').extract()
    tagline = ''.join(tagline).strip() or None
    directors = response.xpath("//div[contains(@class, 'credit_summary_item') and contains(.//h4, 'Director')]/a/text()").extract() or None
    directors = [director.strip() for director in directors]
    genres =  response.xpath("//*[@id='titleStoryLine']/div[4]/a/text()").extract()
    budget = response.xpath("//*[@id='titleDetails']/div[7]/text()").extract()
    opening_week_us =response.xpath("//*[@id='titleDetails']/div[8]/text()").extract() 
    gross_usa = response.xpath("//*[@id='titleDetails']/div[9]/text()").extract()
    world_wide_box_office = response.xpath("//*[@id='titleDetails']/div[10]/text()").extract()
    imdb_url = response.url.replace('?ref_=adv_li_tt', '')
    budget_1 = response.xpath("//*[@id='titleDetails']/div[6]/text()").extract()
    opening_week_us_1 =response.xpath("//*[@id='titleDetails']/div[7]/text()").extract() 
    gross_usa_1 = response.xpath("//*[@id='titleDetails']/div[8]/text()").extract()
    world_wide_box_office_1 = response.xpath("//*[@id='titleDetails']/div[9]/text()").extract()
    mv2_dict[title] = year, rating, users_rating, votes, metascore, countries, languages, actors, tagline, directors, genres, budget, opening_week_us, gross_usa, world_wide_box_office, imdb_url, budget_1, opening_week_us_1, gross_usa_1, world_wide_box_office_1

### Scrap movies of Martin Scorsese ###
## IMDB_Spider3
# Create the Spider class3
class IMDB_Spider3(scrapy.Spider):
  name = "IMDB_spider3"
  # start_requests method
  def start_requests( self ):
    url = 'https://www.imdb.com/name/nm0000217/?ref_=nv_sr_srsg_0'
    yield scrapy.Request( url = url,
                         callback = self.parse_front )
  # First parsing method
  def parse_front(self, response):
    links_to_follow = response.xpath('//*[contains(@class,"filmo-row even")]/b/a/@href').extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
 # Second parsing method
  def parse_pages(self, response):
    title = response.css('h1::text').extract_first().strip()
    year = response.css('#titleYear a::text').extract_first()
    rating = response.css('.subtext::text').extract_first().strip() or None
    users_rating = response.xpath('//span[contains(@itemprop, "ratingValue")]/text()').extract_first()
    votes = response.xpath('//span[contains(@itemprop, "ratingCount")]/text()').extract_first()
    metascore = response.xpath('//div[contains(@class, "metacriticScore")]/span/text()').extract_first()
    countries = response.xpath('//div[contains(@class, "txt-block") and contains(.//h4, "Country")]/a/text()').extract()
    countries = [country.strip() for country in countries]
    languages = response.xpath('//div[contains(@class, "txt-block") and contains(.//h4, "Language")]/a/text()').extract()
    languages = [language.strip() for language in languages]
    actors = response.xpath('//td[not(@class)]/a/text()').extract()
    actors = [actor.strip() for actor in actors]
    tagline = response.xpath('//div[contains(string(), "Tagline")]/text()').extract()
    tagline = ''.join(tagline).strip() or None
    directors = response.xpath("//div[contains(@class, 'credit_summary_item') and contains(.//h4, 'Director')]/a/text()").extract() or None
    directors = [director.strip() for director in directors]
    genres =  response.xpath("//*[@id='titleStoryLine']/div[4]/a/text()").extract()
    budget = response.xpath("//*[@id='titleDetails']/div[7]/text()").extract()
    opening_week_us =response.xpath("//*[@id='titleDetails']/div[8]/text()").extract() 
    gross_usa = response.xpath("//*[@id='titleDetails']/div[9]/text()").extract()
    world_wide_box_office = response.xpath("//*[@id='titleDetails']/div[10]/text()").extract()
    imdb_url = response.url.replace('?ref_=adv_li_tt', '')
    budget_1 = response.xpath("//*[@id='titleDetails']/div[6]/text()").extract()
    opening_week_us_1 =response.xpath("//*[@id='titleDetails']/div[7]/text()").extract() 
    gross_usa_1 = response.xpath("//*[@id='titleDetails']/div[8]/text()").extract()
    world_wide_box_office_1 = response.xpath("//*[@id='titleDetails']/div[9]/text()").extract()
    mv3_dict[title] = year, rating, users_rating, votes, metascore, countries, languages, actors, tagline, directors, genres, budget, opening_week_us, gross_usa, world_wide_box_office, imdb_url, budget_1, opening_week_us_1, gross_usa_1, world_wide_box_office_1

## IMDB_Spider4
# Create the Spider class4
class IMDB_Spider4(scrapy.Spider):
  name = "IMDB_spider4"
  # start_requests method
  def start_requests( self ):
    url = 'https://www.imdb.com/name/nm0000217/?ref_=nv_sr_srsg_0'
    yield scrapy.Request( url = url,
                         callback = self.parse_front )
  # First parsing method
  def parse_front(self, response):
    links_to_follow = response.xpath('//*[contains(@class,"filmo-row odd")]/b/a/@href').extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
 # Second parsing method
  def parse_pages(self, response):
    title = response.css('h1::text').extract_first().strip()
    year = response.css('#titleYear a::text').extract_first()
    rating = response.css('.subtext::text').extract_first().strip() or None
    users_rating = response.xpath('//span[contains(@itemprop, "ratingValue")]/text()').extract_first()
    votes = response.xpath('//span[contains(@itemprop, "ratingCount")]/text()').extract_first()
    metascore = response.xpath('//div[contains(@class, "metacriticScore")]/span/text()').extract_first()
    countries = response.xpath('//div[contains(@class, "txt-block") and contains(.//h4, "Country")]/a/text()').extract()
    countries = [country.strip() for country in countries]
    languages = response.xpath('//div[contains(@class, "txt-block") and contains(.//h4, "Language")]/a/text()').extract()
    languages = [language.strip() for language in languages]
    actors = response.xpath('//td[not(@class)]/a/text()').extract()
    actors = [actor.strip() for actor in actors]
    tagline = response.xpath('//div[contains(string(), "Tagline")]/text()').extract()
    tagline = ''.join(tagline).strip() or None
    directors = response.xpath("//div[contains(@class, 'credit_summary_item') and contains(.//h4, 'Director')]/a/text()").extract() or None
    directors = [director.strip() for director in directors]
    genres =  response.xpath("//*[@id='titleStoryLine']/div[4]/a/text()").extract()
    budget = response.xpath("//*[@id='titleDetails']/div[7]/text()").extract()
    opening_week_us =response.xpath("//*[@id='titleDetails']/div[8]/text()").extract() 
    gross_usa = response.xpath("//*[@id='titleDetails']/div[9]/text()").extract()
    world_wide_box_office = response.xpath("//*[@id='titleDetails']/div[10]/text()").extract()
    imdb_url = response.url.replace('?ref_=adv_li_tt', '')
    budget_1 = response.xpath("//*[@id='titleDetails']/div[6]/text()").extract()
    opening_week_us_1 =response.xpath("//*[@id='titleDetails']/div[7]/text()").extract() 
    gross_usa_1 = response.xpath("//*[@id='titleDetails']/div[8]/text()").extract()
    world_wide_box_office_1 = response.xpath("//*[@id='titleDetails']/div[9]/text()").extract()
    mv4_dict[title] = year, rating, users_rating, votes, metascore, countries, languages, actors, tagline, directors, genres, budget, opening_week_us, gross_usa, world_wide_box_office, imdb_url, budget_1, opening_week_us_1, gross_usa_1, world_wide_box_office_1


# In[3]:


# Initialize the dictionary **outside** of the Spider class
mv1_dict = dict()
mv2_dict = dict()
mv3_dict = dict()
mv4_dict = dict()


# In[4]:


# Run the Spider IMDB_Spider1
process = CrawlerProcess()
process.crawl(IMDB_Spider1)
process.crawl(IMDB_Spider2)
process.crawl(IMDB_Spider3)
process.crawl(IMDB_Spider4)
process.start()


# ***Making dataframe***

# In[5]:


# Convert dictionaries to dataframes
df1 = pd.DataFrame.from_dict(mv1_dict, orient = 'index')
df2 = pd.DataFrame.from_dict(mv2_dict, orient = 'index')
df3 = pd.DataFrame.from_dict(mv3_dict, orient = 'index')
df4 = pd.DataFrame.from_dict(mv4_dict, orient = 'index')


# In[6]:


# Print the shapes of the dataframes
print(df1.shape)
print(df2.shape)
print(df3.shape)
print(df4.shape)


# In[7]:


# Append all the dataframes
df = df1.append(df2)
df = df.append(df3)
df = df.append(df4)


# In[8]:


# Print the shape of the final dataframe
print(df.shape)


# In[9]:


# Change the indexes
df = df.reset_index()


# In[10]:


# Assign names to columns
df.columns = ['title', 'year', 'rating', 'IMDB_rating', 'votes', 'metascore', 'countries', 'languages', 'actors', 'tagline', 'directors', 'genres', 'budget', 'opening_week_us', 'gross_usa', 'world_wide_box_office', 'imdb_url', 'budget_1', 'opening_week_us_1', 'gross_usa_1', 'world_wide_box_office_1']


# ***Cleaning the data***

# In[11]:


# Info of dataframe
df.info()


# In[12]:


# Types of dataframe
df.dtypes


# In[13]:


# Clean 'votes' column (remove commas)
df['votes'] = df['votes'].str.replace(',','')


# In[14]:


# Clean the directors column as we want to select the movies of Steven Spielberg and Martin Scorsese ONLY
directors = df['directors']
df_directors = pd.DataFrame.from_records(directors)
df_directors.columns = ['director1','director2','director3']
print(df_directors)


# In[15]:


# Check if columns director2 and director3 contain 'Steven Spielberg' or 'Martin Scorsese'
if df_directors['director2'].str.contains('Martin Scorsese').any():
    print ("Martin Scorsese is there")
# FOUND that Column 2 contains 'Martin Scorsese'


# In[16]:


# Concat df and df_directors
df = pd.concat([df.reset_index(drop=True), df_directors], axis=1)


# In[17]:


# Create a subset in whick director1 = 'Steven Spielberg' | 'Martin Scorsese' | director2 = 'Steven Spielberg' | 'Martin Scorsese'
df = df[(df.director1 == 'Steven Spielberg') | (df.director1 == 'Martin Scorsese') | (df.director2 == 'Martin Scorsese') | (df.director2 == 'Steven Spielberg')]


# In[18]:


# Look through the FINAL dataframe
df = df.reset_index()


# In[19]:


## Cleaning the final dataset
# Drop column director3
df =  df.drop(['director3'], axis=1)


# In[20]:


world_wide_box_office = df['world_wide_box_office']
df_world_wide_box_office = pd.DataFrame.from_records(world_wide_box_office)
df_world_wide_box_office.columns = ['world_wide_box_office2', 'world_wide_box_office3',' world_wide_box_office4', 'world_wide_box_office5', 'world_wide_box_office6', 'world_wide_box_office7']


# In[21]:


# Drop world_wide_box_office 5, 6, 7
df_world_wide_box_office =  df_world_wide_box_office.drop(['world_wide_box_office5', 'world_wide_box_office6', 'world_wide_box_office7'], axis=1)


# In[22]:


# Concat the two datasets
df = pd.concat([df.reset_index(drop=True), df_world_wide_box_office], axis=1)


# In[23]:


# Make new column 'check' where world_wide_box_office3 contains $ sign
df['check'] = df.world_wide_box_office3.str.contains('$', regex=False)


# In[24]:


# Making new columns based on the value of the coulmn 'check'
df['budget_final'] = np.select([df.check == True, df.check == False], [df.budget, df.budget_1], default=df.budget)
df['opening_week_us_final'] = np.select([df.check == True, df.check == False], [df.opening_week_us, df.opening_week_us_1], default=df.opening_week_us)
df['gross_usa_final'] = np.select([df.check == True, df.check == False], [df.gross_usa, df.gross_usa_1], default=df.gross_usa)
df['world_wide_box_office_final'] = np.select([df.check == True, df.check == False], [df.world_wide_box_office, df.world_wide_box_office_1], default=df.world_wide_box_office)


# In[25]:


# Drop the following columns: budget, opening_week_us, gross_usa, world_wide_box_office, budget_1, opening_week_us_1, gross_usa_1, world_wide_box_office_1, world_wide_box_office2, world_wide_box_office3, world_wide_box_office4, check
df =  df.drop(['budget', 'opening_week_us', 'gross_usa', 'world_wide_box_office', 'budget_1', 'opening_week_us_1', 'gross_usa_1', 'world_wide_box_office_1', 'world_wide_box_office2','world_wide_box_office3',' world_wide_box_office4','check'], axis=1)


# In[26]:


# Clean Budget Final Column
budget = df['budget_final']
df_budget = pd.DataFrame.from_records(budget)
df_budget.columns = ['budget1','budget2','budget3','budget4','budget5','budget6']


# In[27]:


# Cleaning budget column
df_budget =  df_budget.drop(['budget1','budget3', 'budget4', 'budget5', 'budget6'], axis=1)


# In[28]:


# Clean 'budget' column -> remove commas, remove \n, remove >>, remove $ sign, remove space
df_budget['budget2'] = df_budget['budget2'].str.replace(',','')
df_budget['budget2'] = df_budget['budget2'].str.replace('\n','')
df_budget['budget2'] = df_budget['budget2'].str.replace(' ','')
df_budget['budget2'] = df_budget['budget2'].str.replace('»','')
df_budget['budget2'] = df_budget['budget2'].str.replace('$','')


# In[29]:


# Make budget_in dollars column
df_budget['budget_in_dollars'] = df_budget['budget2']
df_budget =  df_budget.drop(['budget2'], axis=1)


# In[30]:


# Clean 'opening_week_us_final' Column
opening_week_us_final = df['opening_week_us_final']
df_opening_week_us_final = pd.DataFrame.from_records(opening_week_us_final)
df_opening_week_us_final.columns = ['opening_week_us_final1','opening_week_us_final2','opening_week_us_final3','opening_week_us_final4','opening_week_us_final5','opening_week_us_final6']
df_opening_week_us_final = df_opening_week_us_final.drop(['opening_week_us_final1','opening_week_us_final3','opening_week_us_final4','opening_week_us_final5','opening_week_us_final6'], axis=1)


# In[31]:


# Clean 'opening_week_us_final' Column
df_opening_week_us_final['opening_week_us_final2'] = df_opening_week_us_final['opening_week_us_final2'].str.replace(',','')
df_opening_week_us_final['opening_week_us_final2'] = df_opening_week_us_final['opening_week_us_final2'].str.replace('\n','')
df_opening_week_us_final['opening_week_us_final2'] = df_opening_week_us_final['opening_week_us_final2'].str.replace(' ','')
df_opening_week_us_final['opening_week_us_final2'] = df_opening_week_us_final['opening_week_us_final2'].str.replace('»','')
df_opening_week_us_final['opening_week_us_final2'] = df_opening_week_us_final['opening_week_us_final2'].str.replace('$','')
df_opening_week_us_final['opening_week_us_in_dollars'] = df_opening_week_us_final['opening_week_us_final2']
df_opening_week_us_final =  df_opening_week_us_final.drop(['opening_week_us_final2'], axis=1)


# In[32]:


# Clean 'gross_usa_final' Column
gross_usa_final = df['gross_usa_final']
df_gross_usa_final = pd.DataFrame.from_records(gross_usa_final)
df_gross_usa_final.columns = ['gross_usa_final1','gross_usa_final2','gross_usa_final3','gross_usa_final4','gross_usa_final5','gross_usa_final6','gross_usa_final7','gross_usa_final8','gross_usa_final9','gross_usa_final10','gross_usa_final11']
df_gross_usa_final = df_gross_usa_final.drop(['gross_usa_final1','gross_usa_final3','gross_usa_final4','gross_usa_final5','gross_usa_final6','gross_usa_final7','gross_usa_final8','gross_usa_final9','gross_usa_final10','gross_usa_final11'], axis=1)


# In[33]:


# Clean 'gross_usa_final' Column
df_gross_usa_final['gross_usa_final2'] = df_gross_usa_final['gross_usa_final2'].str.replace(',','')
df_gross_usa_final['gross_usa_final2'] = df_gross_usa_final['gross_usa_final2'].str.replace('\n','')
df_gross_usa_final['gross_usa_final2'] = df_gross_usa_final['gross_usa_final2'].str.replace(' ','')
df_gross_usa_final['gross_usa_final2'] = df_gross_usa_final['gross_usa_final2'].str.replace('»','')
df_gross_usa_final['gross_usa_final2'] = df_gross_usa_final['gross_usa_final2'].str.replace('$','')
df_gross_usa_final['gross_usa_in_dollars'] = df_gross_usa_final['gross_usa_final2']
df_gross_usa_final =  df_gross_usa_final.drop(['gross_usa_final2'], axis=1)


# In[34]:


# Clean 'world_wide_box_office_final' column
world_wide_box_office_final = df['world_wide_box_office_final']
df_world_wide_box_office_final = pd.DataFrame.from_records(world_wide_box_office_final)
df_world_wide_box_office_final.columns = ['world_wide_box_office_final1','world_wide_box_office_final2','world_wide_box_office_final3','world_wide_box_office_final4','world_wide_box_office_final5','world_wide_box_office_final6']
df_world_wide_box_office_final = df_world_wide_box_office_final.drop(['world_wide_box_office_final1','world_wide_box_office_final3','world_wide_box_office_final4','world_wide_box_office_final5','world_wide_box_office_final6'], axis=1)


# In[35]:


# Clean 'gross_usa_final' Column
df_world_wide_box_office_final['world_wide_box_office_final2'] = df_world_wide_box_office_final['world_wide_box_office_final2'].str.replace(',','')
df_world_wide_box_office_final['world_wide_box_office_final2'] = df_world_wide_box_office_final['world_wide_box_office_final2'].str.replace('\n','')
df_world_wide_box_office_final['world_wide_box_office_final2'] = df_world_wide_box_office_final['world_wide_box_office_final2'].str.replace(' ','')
df_world_wide_box_office_final['world_wide_box_office_final2'] = df_world_wide_box_office_final['world_wide_box_office_final2'].str.replace('»','')
df_world_wide_box_office_final['world_wide_box_office_final2'] = df_world_wide_box_office_final['world_wide_box_office_final2'].str.replace('$','')
df_world_wide_box_office_final['world_wide_box_office_in_dollars'] = df_world_wide_box_office_final['world_wide_box_office_final2']
df_world_wide_box_office_final =  df_world_wide_box_office_final.drop(['world_wide_box_office_final2'], axis=1)


# In[36]:


# Get the dataset with clean 'budget', 'opening_week_us', 'gross_us', and 'world_wide_box' columns
df = pd.concat([df.reset_index(drop=True), df_budget, df_opening_week_us_final, df_gross_usa_final, df_world_wide_box_office_final], axis=1)


# In[37]:


# Drop the columns index, directors, budget_final, opening_week_us_final, gross_usa_final, world_wide_box_office_final
df =  df.drop(['index', 'directors','budget_final', 'opening_week_us_final', 'gross_usa_final', 'world_wide_box_office_final'], axis=1)


# In[38]:


# Get a subset of dataframe
dfn = df[(df.budget_in_dollars != '')]
dfn['opening_week_us_in_dollars'] = dfn['opening_week_us_in_dollars'].str.replace(' ','')
dfn = dfn[dfn.opening_week_us_in_dollars != '']
dfn = dfn[dfn.gross_usa_in_dollars != '']
dfn = dfn[dfn.world_wide_box_office_in_dollars != '']
# Make the df
df = dfn


# In[39]:


# Check if columns director2 and director3 contain 'Steven Spielberg' or 'Martin Scorsese'
if df['director2'].str.contains('Martin Scorsese').any():
    print ("Martin Scorsese is there")
# FOUND that Column 2 does not contain 'Martin Scorsese'


# In[40]:


# Drop director2 column
df =  df.drop(['director2'], axis=1)


# In[41]:


# Making the final dataset by taking the rows where budget_in_dollars column is not null
df = df.dropna(subset=['budget_in_dollars'])


# In[42]:


# Create num_genres column
num_genres = []
for i in df['genres']:
    num_genres.append(len(i))
df['num_genres'] = num_genres


# In[43]:


# Create number of languages column
num_lang = []
for i in df['languages']:
    num_lang.append(len(i))
df['num_languages'] = num_lang


# In[44]:


# Create number of countries column
num_count = []
for i in df['countries']:
    num_count.append(len(i))
df['num_countries'] = num_count


# In[45]:


# reset the indexes of the final dataset
df = df.reset_index()


# In[46]:


# drop index column
df = df.drop(['index'], axis=1)


# In[47]:


# Change the types of columns to int and float
df['year'] = df.year.astype(int)
df['votes'] = df.votes.astype(int)
df['metascore'] = df.metascore.astype(int)
df['opening_week_us_in_dollars'] = df.opening_week_us_in_dollars.astype(int)
df['gross_usa_in_dollars'] = df.gross_usa_in_dollars.astype(int)
df['world_wide_box_office_in_dollars'] = df.world_wide_box_office_in_dollars.astype(int)
df['budget_in_dollars'] = df.budget_in_dollars.astype(int)
df['IMDB_rating'] = df.IMDB_rating.astype(float)


# In[48]:


df.dtypes


# In[49]:


# Change the name of director1 column to director
df = df.rename({'director1': 'director'}, axis=1)


# In[50]:


print(df)

