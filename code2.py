 # Run the main function
 if __name__ == '__main__':
     main().             , # Function to find if a given temperature reading is above or below the average temperature of a city
 def compare_temperature(city, temperature, time):
     temperatures = {
         'Perth': {
             'Morning': 18.2,
             'Evening': 23.0
         },
         'Melbourne': {
             'Morning': 13.5,
             'Evening': 18.9
         },
         'Sydney': {
             'Morning': 18.8,
             'Evening': 23.4
         },
         'Adelaide': {
             'Morning': 16.5,
             'Evening': 21.0
         }
     }
 
     if city in temperatures:
         if time in temperatures[city]:
             average_temperature = temperatures[city][time]
             difference = temperature - average_temperature
             
             if difference > 5:
                 return f"The temperature in {city} {time} is {temperature}°C, which is {difference}°C above the average temperature."
             elif difference < -5:
                 return f"The temperature in {city} {time} is {temperature}°C, which is {abs(difference)}°C below the average temperature."
             else:
                 return f"The temperature in {city} {time} is {temperature}°C, which is close to the average temperature."
         else:
             return 'Unknown Time'
     else:
         return 'Unknown City'
 
 # Main function to handle user interactions
 def main():
     # Prompt the user to enter the city, temperature, and time
     city = input("Enter the city: ")
     temperature = float(input("Enter the temperature: "))
     time = input("Enter the time (Morning/Evening): ")
 
     # Call the compare_temperature function and get the result
     result = compare_temperature(city, temperature, time)
 
     # Display the result
     print(result)
 
 # Run the main function
 if __name__ == '__main__':
     main()