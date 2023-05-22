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
  if country in seasons:
         # Prompt the user to choose the type of season for Australia
         if country == 'Australia':
             season_type = input("Choose the type of season (1: Meteorological Seasons, 2: Noongar Seasons): ")
             if season_type == '1':
                 season_dict = seasons[country]['Meteorological Seasons']
             elif season_type == '2':
                 season_dict = seasons[country]['Noongar Seasons']
             else:
                 return 'Unknown'
         else:
             season_dict = seasons[country]['Meteorological Seasons']
         
         if month in season_dict:
             return season_dict[month] # Return the corresponding season
         else:
             return 'Unknown' # Return 'Unknown' if the month is not found
     else:
         return 'Unknown' # Return 'Unknown' if the country is not found
 
 # Main function to handle user interactions
 def main():
     # Prompt the user to enter the country and month
     country = input("Enter the country: ")
     month = input("Enter the month: ")
     
     # Call the find_season function and get the result
     season = find_season(country, month)
     
     # Display the result in text format
     print(f"The season in {country} during {month} is {season}")
    # Display the result using the graphics symbols (assuming the images are stored in the 'ISEimages' folder)
     if season == 'Summer':
         print("Insert summer image here") # Insert the appropriate image for summer
     elif season == 'Autumn':
         print("Insert autumn image here") # Insert the appropriate image for autumn
     elif season == 'Winter':
         print("Insert winter image here") # Insert the appropriate image for winter
     elif season == 'Spring':
         print("Insert spring image here") # Insert the appropriate image for spring
     else:
         print("Unknown season")