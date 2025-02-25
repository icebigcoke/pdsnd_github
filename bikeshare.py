gitimport time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# This filter function will ask user input for city, month and day of week to get real dataset which user want to analyze. 
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = list(CITY_DATA.keys())
    print(cities)
    city = input("Please choose city which you like:").lower()
    
    while city not in cities:
        print("Please input a valid city. Only chicago, new york city, washington accepted")
        city = input("Please choose city which you like:").lower()
    

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    print(months)
    month = input("Please choose month which you like:").lower()
    while month not in months:
        print("Please input a valid month.")
        month = input("Please choose month which you like:").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekdays = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    print(weekdays)
    day = input("Please choose day of week which you like:").lower()
    while day not in weekdays:
        print("Please input a valid day of week.")
        day = input("Please choose day of week which you like:").lower()

    print('-'*40)
    return city, month, day

# This load data function will prepare data accoring to user's input 
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Start Time'].dt.month.mode()[0]
    print("most common month is :",common_month)
    # TO DO: display the most common day of week
    common_day = df['Start Time'].dt.weekday_name.mode()[0]
    print("most common day of week is :",common_day)

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print("most commonly start hour is :",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("most commonly used start station is :",common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("most commonly used end station is :",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' - '+ df['End Station']
    common_trip = df['Trip'].value_counts().idxmax()
    print("most frequent trip is :",common_trip)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("total travel time is:",total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("average travel time is:",mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("counts of user types is:",user_types)
    
    # TO DO: Display counts of gender
    if  'Gender' not in df.columns:
        print("Gender analysis is not available in this city.")
    else:
        gender = df['Gender'].value_counts()
        print("counts of gender is:",gender)
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print("Birth year analysis is not available in this city.")
    else:
        common_year = df['Birth Year'].mode()[0]
        recent_year = df['Birth Year'].max()
        earliest_year = df['Birth Year'].min()
        print("earliest year of birth is :",earliest_year)
        print("most recent year of birth is :",recent_year)
        print("most common year of birth is :",common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays raw data 5 rows per bikeshare users request."""
    #define the scope of index 
    start_index = 1
    total_rows = len(df)
    while start_index < total_rows:
        user_ans = input("Do you want to see 5 lines of raw data:").lower()
        #Remind user to check data
        if user_ans == 'no':
            print("Exiting the data display")
            break
        
        elif user_ans == 'yes':
            end_index = min(start_index + 5, total_rows)
            print(df.iloc[start_index:end_index])
            start_index = end_index
            
        else: 
            print("Please enter yes or no for valid input.")
    
    
    if start_index >= total_rows:
        print("All data has been displayed.")
       
#This main function will generate statistic results
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
# this python file will be upload to github.com