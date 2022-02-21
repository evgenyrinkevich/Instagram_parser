# Instagram_parser
Scrapes followers and followees lists multiple multiple accounts 

To work needs to be provided with env variables:
- your instagram email
- hashed ig password (can be obtained from devs console - 1st response from instagram as 'enc_password')

These variables to be stored in .env file

Users to parse are set in runner.py users_to_parse variable

Stores data in MongoDB on local machine (InstagramParserPipeline) and in 'data.csv' file (CSVPipeline)
