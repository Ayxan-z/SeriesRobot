import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import re
import sqlite3

class Series():
    
    def __init__(self):
        self.connection = sqlite3.connect("C:\\Users\\shahs\\Documents\\Data_base\\Series_reminder.db")
        self.cursor = self.connection.cursor()
        self._createTable()
        
    def _createTable(self):
        query = 'CREATE TABLE IF NOT EXISTS Series (Name TEXT,Link TEXT,Season TEXT,Episode TEXT)'
        self.cursor.execute(query)
        self.connection.commit()
    
    def _seriesRollCall(self, name):
        self.cursor.execute("SELECT * FROM Series where name=?",(name,))
        incoming_data = self.cursor.fetchall()
        
        return incoming_data

    def seriesAdd(self, name, link, season, episode):
        incoming_data = self._seriesRollCall(name)
        
        if incoming_data:
            print('\nBu adda dizi vardı!')
        
        elif Series.searchEpisode(link, season, episode) == 'Link və ya bölüm sırası səhvdi!':
            print('\nLink və ya bölüm sırası səhvdi!')
            
        else:
            self.cursor.execute("INSERT INTO Series VALUES(?,?,?,?)", (name, link, season, episode))
            self.connection.commit()
            print('\nDizi əlavə olundu')
    
    def searchSeries(self, name):
        incoming_data = self._seriesRollCall(name)
        
        if not incoming_data:
            print('\nBu adda dizi yoxdu!')
            
        else:
            x = Series.searchEpisode(incoming_data[0][1], incoming_data[0][2], incoming_data[0][3])
            print(f'\n{name} dizisinin {x}\nİzlənilən son bölüm: sezon-{incoming_data[0][2]} bölüm-{incoming_data[0][3]}')
    
    def allSearchSeries(self):
        self.cursor.execute("SELECT * FROM Series")
        incoming_data = self.cursor.fetchall()
        control = 0
        for i in incoming_data:
            x = Series.searchEpisode(i[1], i[2], i[3])
            if 'var' in x:
                control = 1
                print(f'\n{i[0]} dizisinin {x}\nİzlənilən son bölüm: sezon-{i[2]} bölüm-{i[3]}\n**************************')
        
        if control == 0:
            print('\nHeç bir dizinin yeni bölümü yoxdu :(')
            
    def seriesShow(self, name):
        incoming_data = self._seriesRollCall(name)
        
        if not incoming_data:
            print('\nBu adda dizi yoxdu!')
        
        else:
            print(f'\nAd: {incoming_data[0][0]}\nLink: {incoming_data[0][1]}\nSezon: {incoming_data[0][2]}\nBölüm: {incoming_data[0][3]}')
    
    def allSeriesShow(self):
        self.cursor.execute("SELECT * FROM Series")
        incoming_data = self.cursor.fetchall()
        
        if not incoming_data:
            print('\nDizi yoxdu')
        
        else:
            for i in incoming_data:
                print(f'\nAd: {i[0]}\nLink: {i[1]}\nSezon: {i[2]}\nBölüm: {i[3]}')
    
    def seriesArrangement(self, name):
        name_copy = name
        incoming_data = self._seriesRollCall(name)
        
        if not incoming_data:
            print('\nBu adda dizi yoxdu!')
        
        else:
            name = input('\nYeni ad daxil edin (dəyişməmək üçün boş buraxın): ')
            name_new = name if name else incoming_data[0][0]
            link = input('Yeni link daxil edin (dəyişməmək üçün boş buraxın): ')
            link = link if link else incoming_data[0][1]
            season = input('Baxdığınız sonuncu sezonu daxil edin (dəyişməmək üçün boş buraxın): ')
            season = season if season else incoming_data[0][2]
            if int(season) > 0:
                episode = input('Baxdığınız sonuncu bölümü daxil edin (dəyişməmək üçün boş buraxın): ')
                episode = episode if episode else incoming_data[0][3]
                if int(episode) > 0:
                    if Series.searchEpisode(link, season, episode) == 'Link və ya bölüm sırası səhvdi!':
                        print('\nLink və ya bölüm sırası səhvdi!')

                    else:
                        self.cursor.execute("UPDATE Series SET Name = ? WHERE Name = ?", (name_new, name_copy))
                        self.cursor.execute("UPDATE Series SET Link = ? WHERE Name = ?", (link, name_copy))
                        self.cursor.execute("UPDATE Series SET Season = ? WHERE Name = ?", (season, name_copy))
                        self.cursor.execute("UPDATE Series SET Episode = ? WHERE Name = ?", (episode, name_copy))
                        self.connection.commit()
                        print('\nDizi güncəlləndi')
                else:
                    print(f'Bölüm sırası {episode} olanmaz!')
            else:
                print(f'Sezon sırası {season} olanmaz!')
            
    def seriesDelete (self, name):
        incoming_data = self._seriesRollCall(name)
        
        if not incoming_data:
            print('\nBu adda dizi yoxdu!')
        
        else:
            self.cursor.execute("DELETE FROM Series where Name = ?",(name,))
            self.connection.commit()
            print('\nDizi silindi')
    
    def allSeriesDelete(self):
        x = input('\nBütün diziləri silmək istədiyiniə əminsiniz? (h/y): ')
        
        if x == 'h':
            self.cursor.execute("DELETE FROM Series")
            self.connection.commit()
            self._createTable()
            print('\nDizilər silindi')
    
    @classmethod
    def searchEpisode(cls, url, season, episode):
        
        season_copy = season
        season_url =  url[:url.find('?')] + 'episodes' + '?' + 'season='
        date_now = datetime.strptime(datetime.strftime(datetime.now(),'%d %b %Y'), '%d %b %Y')
        cnt = 0
        
        while 1:
            input_season_url_copy = season_url + season

            response = requests.get(input_season_url_copy)
            html = response.content

            soup = bs(html,"html.parser")
            find_episode = soup.find_all('div',{'class':'hover-over-image zero-z-index'})
            find_date = soup.find_all('div',{'class':'airdate'})

            for i, j in zip(find_episode, find_date):
                i = i.text
                j = j.text
                
                i = i.strip()
                i = i.replace('\n','')

                j = j.strip()
                j = j.replace('\n','')
                j = j.replace('.','')

                if i == '' or j == '' or len(j) == 4:
                    break

                x = re.search("([0-9]+)\D+([0-9]+)",i)
                if x.group(1) == season_copy:

                    if int(x.group(2)) >= int(episode) and (datetime.strptime(j, '%d %b %Y') - date_now).days < 0:
                        cnt += 1

                else:
                    if (datetime.strptime(j, '%d %b %Y') - date_now).days < 0:
                        cnt += 1

            if not soup.find_all('a',{'id':'load_next_episodes'}):
                break 
            
            season = str(int(season) + 1)

        if cnt == 0:
            return 'Link və ya bölüm sırası səhvdi!'
        elif cnt == 1:
            return 'izlənməyən bölümü yoxdu'
        else:
            return str(cnt - 1) + ' ədəd izlənməyən bölümü var'
            
            
while 1:
    series = Series()
    
    x = input('''
    1) Dizi əlavə elə
    2) Dizinin yeni bölümü olub olmadığına bax
    3) Yeni bölümü olan diziləri göstər
    4) Diziyi göstər
    5) Bütün diziləri göstər
    6) Diziyi güncəllə
    7) Diziyi sil
    8) Bütün diziləri sil
    9) Çıxış
    
    ---> ''')

    if x == '1':
        name = input('Dizinin adın daxil edin: ')
        link = input('Dizinin linkin daxil edin: ')
        season = input('Dizinin baxdığınız son sezonunu daxil edin: ')
        episode = input('Dizinin baxdığınız son bölümünü daxil edin: ')
        
        if not name or not link or not season or not episode:
             print('\nDaxil edilənləri boş buraxanmarsız!')
        
        else:
            series.seriesAdd(name, link, season, episode)
    
    elif x == '2':
        series.searchSeries(input('Dizinin adını daxil edin: '))
    
    elif x == '3':
        series.allSearchSeries()
    
    elif x == '4':
        series.seriesShow(input('Dizinin adını daxil edin: '))
    
    elif x == '5':
        series.allSeriesShow()
        
    elif x == '6':
        series.seriesArrangement(input('Güncəlləmək istədiyiniz dizinin adını daxil edin: '))
    
    elif x == '7':
        series.seriesDelete(input('Silmək istədiyiniz dizinin adını daxil edin: '))
            
    elif x == '8':
        series.allSeriesDelete()

    elif x == '9':
        quit()
    
    else:
        print('Düzgün seçim daxil edin!')
    
    series.connection.close()