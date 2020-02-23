from Weather import app
from Weather.forms import Myform
from Weather.Weather_api import get_temp, get_description, get_LocalName, get_icon, conditions
from flask import render_template, send_from_directory, url_for, request, redirect



@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
    #     zipcode = request.form.get('zipcode')  
        # TODO: ADD for validation !    
    form = Myform()
    if form.validate_on_submit():
        zipcode = request.form.get('zipcode')
        return  redirect(url_for('weather', zipcode=zipcode))
    return render_template('home.html', form=form)


@app.route('/weather')
def weather():
    zipcode = str(request.args.get('zipcode', None))
    description = str(get_description(zipcode))
    temp = str(round(get_temp(zipcode)))+'°'
    location = str(get_LocalName(zipcode))
    Weather_img = f'http://openweathermap.org/img/wn/{get_icon(zipcode)}@2x.png'
    if description in conditions['group1'] and temp >= '50':
        playList_Song = url_for('static', filename='playlists/Roddy_Ricch-The_Box.mp3')
        print(f'{description} and {temp}')
    elif description in conditions['group2'] and temp >= '35':
        playList_Song = url_for('static', filename='playlists/Ray_Charles-I_got_a_woman.mp3')
        print(f'{description} and {temp}')
    elif description in conditions['group3'] and temp >= '40':
        playList_Song = url_for('static', filename='playlists/Suicidal_Thoughts(2005_Remaster).mp3')
        print(f'{description} and {temp}')
    elif description in conditions['group4'] and temp <= '20':
        playList_Song = url_for('static', filename='playlists/Syl_Johnson-Is_It_Because_Im_Black_Single.mp3')
        print(f'{description} and {temp}')
    else:
        playList_Song = url_for('static', filename='playlists/James_Brown-Blues_and_Pants.mp3')
        print(f'{description} and {temp}')
    return render_template('weather.html', Weather_img=Weather_img, Song=playList_Song, temp=temp, location=location)


@app.route('/test')
def test():
    return render_template('layout.html')