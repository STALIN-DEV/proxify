from bs4 import BeautifulSoup
import requests
import csv
from urllib.request import urlopen

url = 'https://freeproxylist.ru/protocol/http'
flname = 'Proxy.csv'

def console_pic(): #console picture
    print ("  ______    #  ______       # ______      # __     __     # ________     # ______    # __  __    #")
    print ("/ _____ /\  # /_____/\      #/_____/\     #/__/\ /__/\    #/_______/\    #/_____/\   #/_/\/_/\   #")
    print ("\:::_   \ \ # \:::_ \ \     #\:::_ \ \    #\ \::\\:.\ \   #\__.::._\/    #\::::_\/_  #\ \ \ \ \  #")
    print (" \:(_)   \ \#  \:(_) ) )_   # \:\ \ \ \   # \_\::_\:_\/   #   \::\ \     # \:\/___/\ # \:\_\ \ \ #")
    print ("  \: ___  \/#   \: __ `\ \  #  \:\ \ \ \  #   _\/__\_\_/\ #   _\::\ \__  #  \:::._\/ #  \::::_\/ #")
    print ("   \ \ \    #    \ \ `\ \ \ #   \:\_\ \ \ #   \ \ \ \::\ \#  /__\::\__/\ #   \:\ \   #    \::\ \ #")
    print ("    \_\/    #     \_\/ \_\/ #    \_____\/ #    \_\/  \__\/#  \________\/ #    \_\/   #     \__\/ #")
    print ("           ##              ##            ##              ##             ##          ##          ##")
    print ("                                         Licensed by GPL-3.0")
    print ("                                       Read README.md before use.")
    print ("* Running...")
    print (" ")

console_pic()

def pr(): #parsing
    res = {'IP': [], 'Port': [], 'Country': [], 'Protocol': []}
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    fin = soup.find_all('th', class_='w-30 tblport')
    ports = soup.find_all('td', class_='w-10 tblport')
    ct = soup.find_all('span', class_='cntrytbl')
    pt = soup.find_all('a', class_='http')
    for th in fin:
        res['IP'].append(th.text)
    for td in ports:
        res['Port'].append(td.text)
    for span in ct:
        res['Country'].append(span.text)
    for a in pt:
        res['Protocol'].append(a.text)
    ''' for i in range(len(res)):
        print(*res[list(res.keys())[i]]) '''
    def save(res,path): #creating csv file
        with open(path,'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('IP','Port','Country','Protocol'))
            writer.writerow((res['IP']))
            writer.writerow((res['Port']))
            writer.writerow((res['Country']))
            writer.writerow((res['Protocol']))
    save(res, 'Proxy.csv')
    print ('* Successfully!')

def connection_conf(): #checking connection
    try:
        urlopen(url)
        pr()
    except IOError:
        '* Failed! Check your internet connection!'

connection_conf()
