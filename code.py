from PIL import Image
import requests
from io import BytesIO

def find_season(country_name, month_name):
    seasons = {
        'Australia': {
            'Meteorological Seasons': {
                'December': 'Summer',
                'January': 'Summer',
                'February': 'Summer',
                'March': 'Autumn',
                'April': 'Autumn',
                'May': 'Autumn',
                'June': 'Winter',
                'July': 'Winter',
                'August': 'Winter',
                'September': 'Spring',
                'October': 'Spring',
                'November': 'Spring'
            },
            'Noongar Seasons': {
                'December': 'Birak',
                'January': 'Birak',
                'February': 'Bunuru',
                'March': 'Bunuru',
                'April': 'Djeran',
                'May': 'Djeran',
                'June': 'Makuru',
                'July': 'Makuru',
                'August': 'Djilba',
                'September': 'Djilba',
                'October': 'Kambarang',
                'November': 'Kambarang'
            }
        },
        'Spain': {
            'Meteorological Seasons': {
                'December': 'Winter',
                'January': 'Winter',
                'February': 'Winter',
                'March': 'Spring',
                'April': 'Spring',
                'May': 'Spring',
                'June': 'Summer',
                'July': 'Summer',
                'August': 'Summer',
                'September': 'Autumn',
                'October': 'Autumn',
                'November': 'Autumn'
            }
        },
        'Japan': {
            'Meteorological Seasons': {
                'December': 'Winter',
                'January': 'Winter',
                'February': 'Winter',
                'March': 'Spring',
                'April': 'Spring',
                'May': 'Spring',
                'June': 'Summer',
                'July': 'Summer',
                'August': 'Summer',
                'September': 'Autumn',
                'October': 'Autumn',
                'November': 'Autumn'
            }
        },
        'Mauritius': {
            'Meteorological Seasons': {
                'December': 'Summer',
                'January': 'Summer',
                'February': 'Summer',
                'March': 'Summer',
                'April': 'Summer',
                'May': 'Autumn',
                'June': 'Winter',
                'July': 'Winter',
                'August': 'Winter',
                'September': 'Winter',
                'October': 'Spring',
                'November': 'Summer'
            }
        },
        'Malaysia': {
            'Meteorological Seasons': {
                'December': 'Northeast Monsoon',
                'January': 'Northeast Monsoon',
                'February': 'Northeast Monsoon',
                'March': 'Inter-monsoon',
                'April': 'Inter-monsoon',
                'May': 'Southeast Monsoon',
                'June': 'Southeast Monsoon',
                'July': 'Southeast Monsoon',
                'August': 'Southeast Monsoon',
                'September': 'Southeast Monsoon',
                'October': 'Inter-monsoon',
                'November': 'Inter-monsoon'
            }
        },
        'Sri Lanka': {
            'Meteorological Seasons': {
                'December': 'Northeast Monsoon',
                'January': 'Northeast Monsoon',
                'February': 'Northeast Monsoon',
                'March': 'Inter-monsoon',
                'April': 'Inter-monsoon',
                'May': 'Southeast Monsoon',
                'June': 'Southeast Monsoon',
                'July': 'Southeast Monsoon',
                'August': 'Southeast Monsoon',
                'September': 'Southeast Monsoon',
                'October': 'Inter-monsoon',
                'November': 'Inter-monsoon'
            }
        }
    }

    if country_name in seasons:
        country_seasons = seasons[country_name]
        season_type = input("Choose the type of season (1: Meteorological Seasons, 2: Noongar Seasons): ")
        
        if country_name == 'Australia' and season_type == '2':
            season_dict = country_seasons['Noongar Seasons']
        else:
            season_dict = country_seasons['Meteorological Seasons']
        
        if month_name in season_dict:
            return season_dict[month_name]
        else:
            return 'Unknown'
    else:
        return 'Unknown'


def main():
    country_name = input("Enter the country: ")
    month_name = input("Enter the month: ")
    
    season = find_season(country_name, month_name)
    
    print(f"The season in {country_name} during {month_name} is {season}")
    
    if season == 'Summer':
        response = requests.get('https://d1whtlypfis84e.cloudfront.net/guides/wp-content/uploads/2019/07/27114414/Summer-season-1024x576.jpg')
        image = Image.open(BytesIO(response.content))
        image.show()
    elif season == 'Autumn':
        response = requests.get('https://img.freepik.com/premium-photo/colorful-autumn-landscape_130291-2270.jpg?w=2000')
        image = Image.open(BytesIO(response.content))
        image.show()
    elif season == 'Winter':
        response = requests.get('https://c.tadst.com/gfx/600x337/winter-lake.jpg?1')
        image = Image.open(BytesIO(response.content))
        image.show()
    elif season == 'Spring':
        response = requests.get('https://media.cnn.com/api/v1/images/stellar/prod/210316134609-01-wisdom-project-spring.jpg?q=w_4000,h_2250,x_0,y_0,c_fill')
        image = Image.open(BytesIO(response.content))
        image.show()
    else:
        print("Unknown season")


if __name__ == '__main__':
    main()
