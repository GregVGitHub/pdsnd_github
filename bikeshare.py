import time
import pandas as pd
import numpy as np
from datetime import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')

    # ADD : available analysis parameters
    cities_list=['chicago','new york city','washington']
    months_list=['all','january','february','march','april','may','june']
    days_list=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=''
    while city not in cities_list:
        city=str(input("Enter the name of the city to analyze: ")).lower()
        if city not in cities_list:
            print("!Warning : cities available for analysis : {}".format(cities_list))

    # TO DO: get user input for month (all, january, february, ... , june)
    month=''
    while month not in months_list:
        month=str(input("Enter the month to analyze (enter 'all' if you want all the months): ")).lower()
        if month not in months_list:
            print("!Warning : months available for analysis : {}".format(months_list))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=''
    while day not in days_list:
        day=str(input("Enter the day to analyze (enter 'all' if you want all the days): ")).lower()
        if day not in days_list:
            print("!Warning : days available for analysis : {}".format(days_list))

    print('-'*40)
    return city, month, day


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
    
    months_dict = {'january' : 1 , 'february' : 2 , 'march' : 3 , 'april' : 4 , 'may' : 5 , 'june' : 6}
    days_dict = {'monday' : 0 , 'tuesday' : 1 , 'wednesday' : 2 , 'thursday' : 3, 'friday' : 4 , 'saturday' : 5 , 'sunday' : 6}
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != 'all':
        df = df[df['Start Time'].dt.month == months_dict[month]]

    if day != 'all':
        df = df[df['Start Time'].dt.weekday == days_dict[day]]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Month'] = df['Start Time'].dt.month
    most_common_month = df['Month'].mode()[0]
    print('Most Common Start Month:', most_common_month)
    
    # TO DO: display the most common day of week
    df['Week Day'] = df['Start Time'].dt.weekday
    most_common_weekday = df['Week Day'].mode()[0]
    print('Most Common Start Day of the Week:', most_common_weekday)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Hour'].mode()[0]
    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_stations = df['Start Station'].value_counts()
    print('Most Common Used Start Station:', start_stations.index[0])
    
    # TO DO: display most commonly used end station
    end_stations = df['End Station'].value_counts()
    print('Most Common Used End Station:', end_stations.index[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Way'] = df['Start Station'] + " > " + df['End Station']
    ways = df['Way'].value_counts()
    print('Most Common Combination Start and End Station:', ways.index[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('\nCounts by user types:\n',user_type_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts by gender:\n',gender_counts)
    except:
        print('\n Gender \n No information about gender in this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('\nEarliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', most_common_year)
    except:
        print('\n Year of Birth \n No information about year of birth in this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
                        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print('\n Raw Data (5 first lines):\n')
        with open(CITY_DATA[city], 'r') as f:
            while True:
                for i in range(5):
                    print(f.readline())
                read_more = input('\nWould you like to read 5 lines more ? Enter yes or no.\n')
                if read_more.lower() != 'yes':
                    break
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
