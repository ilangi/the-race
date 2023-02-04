from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from tkinter import *
import sys
player_list = []

# WSU%20Void

def get_op_gg(player_name, summoner_name):
    url = f'https://www.op.gg/summoners/na/{summoner_name}'
    request = Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0')
    page = urlopen(request)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    ranked_data = soup.find('div',{'class':"css-1v663t e1x14w4w1"})
    the_divs = ranked_data.find_all('div')
    

    tier = ranked_data.find("div",{"class":"tier"}).contents[0]

    # cast it to a string object
    division_div = str(the_divs[4]) # '<div class="tier">silver', '2</div>'
    # Splits the string into an array of 2 objects
    str_division = division_div.split('<!-- --> ')
    # Gets index 1
    new = str_division[1]
    # Gets the division number
    division = new[:1]
    
    
    lp = ranked_data.find("div",{"class":"lp"}).contents[0]
    

    return  f'{player_name}: {tier} {division} {lp} LP'
    


def display():
    #try:
        ian = get_op_gg('marshal',"WSU%20Void")
        reece = get_op_gg('reece',"YehudiCamil1")
        isaac = get_op_gg('isaac', "Greyybit")
        michael = get_op_gg('michael', "DatsOneBigBonah")
        marley = get_op_gg('marley',"ItsMounga")

        return f'{ian}\n\n{reece}\n\n{isaac}\n\n{michael}\n\n{marley}'
    #except: return "Couldn't reach the server.  Please try again"

def main():
    stocks = Tk()
    stocks.geometry("600x550")
    stocks.title('The race')
    stocks.config(bg='#0A0A0A')
    def loop():
        information = Message(stocks,text=display(),width=550, font=("Helvetica", 24)).after(500000,loop)
        return information
    


    #---- GUI Functions
    def close(event):
        sys.exit()

    # ----- GUI Controls
    information = Message(stocks,text=display(),width=550, font=("Comic Sans MS", 24), foreground="white", bg="#0A0A0A")
    information.pack()

    # ------ Bindings
    stocks.bind('<Escape>', close)

    loop()
    information.pack()
    stocks.mainloop()
if __name__ == '__main__':
    main()
