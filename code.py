# Function to find the season of the year when a country name and the month of the year is given
 def find_season(country, month):
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
             'Meteorological Season': {
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
 