from flask import Flask,  render_template
#NEWTHING
app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/playlist')
def playlist():
    return render_template('playlist.html')

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/tags/Blau')
def BlauTag():
    return render_template('BlaueTag.html')

@app.route('/tags/Brau')
def BrauneTag():
    return render_template('BrauneTag.html')

@app.route('/tags/Bundestag')
def Bundestag():
    return render_template('Bundestag.html')

@app.route('/tags/Gruenen')
def Grun():
    return render_template('Grünen.html')

@app.route('/tags/Gelb')
def GelbTag():
    return render_template('OrangeTag.html')

@app.route('/tags/Schwarz')
def SchwarzTag():
    return render_template('SchwarzTag.html')
@app.route('/tags/Rot')
def RoteTag():
    return render_template('RoteTag.html')



##videos

@app.route('/videos/CDU')
def CDU():
    return render_template('/videos/CDU.html')

@app.route('/videos/CDUzerstörung')
def DieZerstörungderCDU():
    return render_template('/videos/DieZerstörungderCDU.html')

@app.route('/videos/CDUrede')
def CDUrede():
    return render_template('/videos/JungsteRede.html')

@app.route('/videos/CSU')
def CSU():
    return render_template('/videos/CSU.html')
@app.route('/videos/FDP')
def FDP():
    return render_template('/videos/FDP.html')

@app.route('/videos/AFD')
def AFD():
    return render_template('/videos/AFD.html')

@app.route('/videos/SPD')
def SPD():
    return render_template('/videos/SPD.html')

@app.route('/videos/Linke')
def dieLinke():
    return render_template('/videos/dieLinke.html')

@app.route('/videos/AFDwaehler')
def AFDwaehler():
    return render_template('/videos/AfDwähler.html')

@app.route('/videos/AFDrede')
def AFDrede():
    return render_template('/videos/AliceWeidelRede.html')

@app.route('/videos/Gruenen')
def Grünen():
    return render_template('/videos/Grünen.html')

@app.route('/videos/JanBoehmerman')
def Jan():
    return render_template('/videos/JanBöhmermann.html')

####

##playlists1
@app.route('/playlists/FAQ')
def FAQ():
    output = render_template('FAQ.html', name="CDU in 5 Minuten ", link="https://www.youtube.com/embed/g2y4WpwPBYQ",next="/playlists/FAQ/2")
    return output

@app.route('/playlists/FAQ/2')
def FAQ2():
    output = render_template('FAQ.html', name="AfD in 5 Minuten", link="https://www.youtube.com/embed/WlE6C--5Xe4",next="/playlists/FAQ/3")
    return output

@app.route('/playlists/FAQ/3')
def FAQ3():
    output = render_template('FAQ.html', name="Wie mächtig ist die CSU wirklich?", link="https://www.youtube.com/embed/Zpf3SBPXENA",next="/playlists/FAQ/5")
    return output

@app.route('/playlists/FAQ/5')
def FAQ5():
    output = render_template('FAQ.html', name="DIE LINKE in 5 Minuten", link="https://www.youtube.com/embed/1H2XtPujdQ8",next="/playlists/FAQ/6")
    return output

@app.route('/playlists/FAQ/6')
def FAQ6():
    output = render_template('FAQ.html', name="FDP in 5 Minuten", link="https://www.youtube.com/embed/lIJuuatBnhw",next="/playlists/FAQ/7")
    return output

@app.route('/playlists/FAQ/7')
def FAQ7():
    output = render_template('FAQ.html', name="Die GRÜNEN in 5 Minuten", link="https://www.youtube.com/embed/xSCt5sjWZVE",next="/playlists/FAQ/8")
    return output

@app.route('/playlists/FAQ/8')
def FAQ8():
    output = render_template('FAQ.html', name="SPD in 5 Minuten", link="https://www.youtube.com/embed/XHOI8KREZyc",next="/playlists/FAQ")
    return output

####
@app.route('/playlists/Sitzung')
def Sitzung():
    output = render_template('Sitzung.html', name="Rede von Alice Weidel zur Regierungspolitik der Bundeskanzlerin am 12.09.18", link="https://www.youtube.com/embed/S8hULQ29pT0",next="/playlists/Sitzung/1")
    return output

@app.route('/playlists/Sitzung/1')
def Sitzung1():
    output = render_template('Sitzung.html', name="'Das ist grober Unfug': Der jüngste CDU-Abgeordnete nimmt den AfD-Burka-Antrag auseinander", link="https://www.youtube.com/embed/XN70irb6-iE",next="/playlists/Sitzung")
    return output



@app.route('/playlists/Meinung')
def Meinung():
    output = render_template('Meinung.html',
                             name="Warum Russlanddeutsche die AFD wählen",
                             link="https://www.youtube.com/embed/ku-LEGVjmX0", next="/playlists/Meinung/1")
    return output

@app.route('/playlists/Meinung/1')
def Meinung1():
    output = render_template('Meinung.html',
                             name="Die Zerstörung der CDU.",
                             link="https://www.youtube.com/embed/4Y1lZQsyuSQ", next="/playlists/Meinung/2")
    return output

@app.route('/playlists/Meinung/2')
def Meinung2():
    output = render_template('Meinung.html',
                             name="Die Bundesregierung im Internet | NEO MAGAZIN ROYALE mit Jan Böhmermann - ZDFneo",
                             link="https://www.youtube.com/embed/853w0xpumTs", next="/playlists/Meinung")
    return output
###

@app.errorhandler(404)
def page_not_found(error):

   return "Такой страницы нет!"

if __name__ == '__main__':
    app.run()