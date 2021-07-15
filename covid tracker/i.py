#importing libraries

import requests
import bs4
import plyer
import tkinter as tk
import time 
import datetime
import threading


# defininfg functions
def get_data(url):

	data = requests.get(url)
	return data


def get_corona_details_india():
	url = "https://www.mohfw.gov.in/"

	html_view = get_data(url)

	#use of beautifulsoup
	bs = bs4.BeautifulSoup(html_view.text , 'html.parser')
	info_div = bs.find("div" , class_ = "site-stats-count")

	info_li = info_div.find_all("li")
	all_details =""
	x = 0
	for l in info_li:
		if x < 4:
			count = l.find("strong").get_text()
			text = l.find("span").get_text()
			x = x+1
			all_details = all_details + text + " : " + count + "\n"


	return all_details


#refresh function
def refr():
	newdata = get_corona_details_india()
	main_label['text'] = newdata
	print("Refreshing...")

#notification funtion
def notify_me():
	while True:

		plyer.notification.notify(title="COVID ALERT" , message=get_corona_details_india(), timeout =20 )
		time.sleep(1800)

#print data in creative way
#frontend
root = tk.Tk()
root.geometry("600x400")
root.title("CORONA DATA : INDIA")
root.configure(background="white")
f = ("poppins" , 25 , "bold")
main_label = tk.Label(root,text=get_corona_details_india() , font=f , bg="white" )
main_label.pack()

#refresh button
refresh= tk.Button(root, text="REFRESH",font = f, relief='solid' , command =refr)
refresh.pack()

#new thread

th1 = threading.Thread(target = notify_me)
th1.setDaemon(True)
th1.start()


#initializing root
root.mainloop()


#main funtion
def main():

	get_corona_details_india()


if __name__ == '__main__':
		main();




