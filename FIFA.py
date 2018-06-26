import pandas as pd
import matplotlib.pyplot as plt
print (plt.style.available)
plt.style.use('ggplot')
df=pd.read_csv('G:\\data\\results.csv')
df_FIFA_all=df[df['tournament'].str.contains('FIFA',regex=True)]
df_FIFA=df_FIFA_all[df_FIFA_all['tournament']=='FIFA World Cup']
df_FIFA.loc[:,'date']=pd.to_datetime(df_FIFA.loc[:,'date'])
df_FIFA['year']=df_FIFA['date'].dt.year
df_FIFA['diff_score']=df_FIFA['home_score']-df_FIFA['away_score']
df_FIFA['win_team']=''
df_FIFA['diff_score']=pd.to_numeric(df_FIFA['diff_score'])
df_FIFA.loc[df_FIFA['diff_score']>0,'win_team']=df_FIFA.loc[df_FIFA['diff_score']>0,'home_team']
df_FIFA.loc[df_FIFA['diff_score']<0,'win_team']=df_FIFA.loc[df_FIFA['diff_score']<0,'away_team']
df_FIFA.loc[df_FIFA['diff_score']==0,'win_team']='Draw'
s=df_FIFA.groupby('win_team')['win_team'].count()
s.sort_values(ascending=False,inplace=True)
s.drop(labels=['Draw'],inplace=True)
#获取世界杯所有比赛获胜场数最多的前20强数据
s.head(20).plot(kind='bar',figsize=(10,6),title='Top 20 Winners of World Cup')
s.sort_values(ascending=True,inplace=True)
s.tail(20).plot(kind='barh', figsize=(10,6), title='Top 20 Winners of World Cup')
s_percentage = s/s.sum()
s_percentage
s_percentage.head(20).plot(kind='pie', figsize=(10,10), autopct='%.1f%%',startangle=200, title='Top 20 Winners of World Cup', label='')
plt.show()

df_score_home=df_FIFA[['home_team','home_score']]
column_update=['team','score']
df_score_home.columns=column_update
df_score_away=df_FIFA[['away_team', 'away_score']]
df_score_away.columns=column_update
df_score=pd.concat([df_score_home,df_score_away],ignore_index=True)
s_score=df_score.groupby('team')['score'].sum()
s_score.sort_values(ascending=True,inplace=True)
s_score.tail(20).plot(kind='barh',figsize=(10,6),title='Top 20 in Total Scores of World Cup')
plt.show()

team_list = ['Russia', 'Germany', 'Brazil', 'Portugal', 'Argentina', 'Belgium', 'Poland', 'France',
             'Spain', 'Peru', 'Switzerland', 'England', 'Colombia', 'Mexico', 'Uruguay', 'Croatia',
            'Denmark', 'Iceland', 'Costa Rica', 'Sweden', 'Tunisia', 'Egypt', 'Senegal', 'Iran',
            'Serbia', 'Nigeria', 'Australia', 'Japan', 'Morocco', 'Panama', 'Korea Republic', 'Saudi Arabia']

df_top32=df_FIFA[(df_FIFA['home_team'].isin(team_list))&(df_FIFA['away_team'].isin(team_list))]
#赢球场数情况
s_32=df_top32.groupby('win_team')['win_team'].count()
s_32.drop(labels=['Draw'],inplace=True)
s_32.sort_values(ascending=True,inplace=True)
s_32.plot(kind='barh',figsize=(12,30),title='Top 32 of World Cup since year 1872')
plt.show()

#进球数据情况
df_score_home_32 = df_top32[['home_team', 'home_score']]
column_update = ['team', 'score']
df_score_home_32.columns = column_update
df_score_away_32 = df_top32[['away_team', 'away_score']]
df_score_away_32.columns = column_update
df_score_32 = pd.concat([df_score_home_32,df_score_away_32], ignore_index=True)
s_score_32 = df_score_32.groupby('team')['score'].sum()
s_score_32.sort_values(ascending=False, inplace=True)
s_score_32.sort_values(ascending=True, inplace=True)
s_score_32.plot(kind='barh', figsize=(8,12), title='Top 32 in Total Scores of World Cup since year 1872')
plt.show()
#分析结论:自2002年以来，32强之间的世界杯比赛，从赢球场数和进球数量来看，德国、阿根廷、巴西三支球队实力最强。其中，德国队的数据优势更明显。





