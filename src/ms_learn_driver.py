from ms_learn_crawler import *
import calendar
import time
import pandas as pd

f = open("portfolio.config", "r")
portfolio_urls = f.readlines()
cert_info = {}
all_cert_lp_info = pd.DataFrame()
all_cert_module_info = pd.DataFrame()
crawler = ms_learn_crawler()

for cert in portfolio_urls:

    learn_uids = crawler.get_learn_paths_for_cert(cert)
    lp_metadata = crawler.get_learn_path_metadata(learn_uids)
    df = pd.DataFrame(lp_metadata, columns = ['LearningPathUid', 'LiveUrl','TotalModules'])
    last_slash = cert.rfind("/")
    cert_name = cert[last_slash+1:]
    df['Certification'] = cert_name.strip()
    if all_cert_lp_info.size == 0:
        all_cert_lp_info = df
    else:
        all_cert_lp_info = pd.concat([all_cert_lp_info,df],sort=False)
    
#print(all_cert_lp_info)
lp_data = pd.read_csv('../data/learning_path_stats-latest.csv')
all_cert_lp_info = pd.merge(all_cert_lp_info, lp_data,on='LiveUrl')

#print(all_cert_lp_info)
#learn_urls2 = crawler.get_modules()

all_cert_lp_info.to_csv('../processed_data/portfolio_cert_lp_info.csv')

learn_path_urls = all_cert_lp_info['LiveUrl'].tolist()

for learn_path_url in learn_path_urls:

    module_uids = crawler.get_learn_path_modules(learn_path_url)
    module_metadata = crawler.get_module_metadata(module_uids)
    df = pd.DataFrame(module_metadata, columns = ['LiveUrl','Uid','Url'])
    df['Certification'] = all_cert_lp_info.loc[all_cert_lp_info['LiveUrl'] == learn_path_url]['Certification'].values[0]
    df['LearningPathUrl'] = learn_path_url
    
    all_cert_module_info = pd.concat([all_cert_module_info,df],sort=False)
    
module_data = pd.read_csv('../data/module_stats-latest.csv')
all_cert_module_info = pd.merge(all_cert_module_info, module_data,on='LiveUrl')
#print(all_cert_module_info.head())

all_cert_module_info.to_csv('../processed_data/portfolio_cert_module_info.csv')

# This final part isn't necessary if we use the export from the dashboard that contains star rating data - 

#module_urls = all_cert_module_info['Url'].tolist()
#print(module_urls)
#module_ratings = pd.DataFrame(crawler.get_module_ratings(module_urls), columns = ['ModuleUrl','AverageRating'])
#print("Module Ratings DF")
#print(module_ratings.head())
#all_cert_module_info = pd.merge(all_cert_module_info, module_ratings.set_index('ModuleUrl'),left_on='Url',right_index=True)

#print(all_cert_lp_info)
#learn_urls2 = crawler.get_modules()
#print(all_cert_module_info.head())
