import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Please enter the city do you want to analyze like Chicago, New York City or Washington \n>').lower()
        if city in cities:
            break

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('Which months do you want to get data. e.g: "January", or "all" to apply no month filter\n>').lower()
        if month in months:
            break
                      
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'none']
    while True:
        day = input('Please type a day which you want to analyze. e.g: "Monday", or "all" to apply no day filter \n').lower()
        if day in days:
            break
            
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name

    # filter by month to create the new dataframe
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week to create the new dataframe
    if day != 'all':
        df = df[df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is :", most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['weekday'].mode()[0]
    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour
    hour = df['Start Time'].dt.hour
    most_common_start_hour = hour.mode()[0]
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_start_station)

    # display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", most_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_combination = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most frequent combination of start station and end station trip : {}, {}"\
            .format(most_frequent_combination[0], most_frequent_combination[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    counts_user_types = df['User Type'].value_counts()     
    print("Counts of user types:\n", counts_user_types)
    
    if 'Gender' in df.columns:
        # display counts of gender
        counts_of_gender = df['Gender'].value_counts()
        print("Counts of gender:\n", counts_of_gender)
    else:
        print("There is no 'Gender' column")
        
    if 'Birth Year' in df.columns:         
        # display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        # the most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)
        # the most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)
        # the most common birth year
        most_common_year = birth_year.mode()[0]
        print("The most common birth year:", most_common_year)
    else:
        print("There is no 'Birth Year' column")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_row_data(df):
    """Displays rows of data from the csv file for the selected city."""
    
    # list of user responses
    user_response_list = ['yes', 'no']
    # user input variable
    row_data = ''
    # initial number of row variable
    number_of_row = 0
    
    # get user input for displaying row data
    while True:
        if row_data not in user_response_list:
           row_data = input("\nWould you like to view the raw data?\n").lower()
        else:
            if row_data == "yes":
                print(df.head())
                break
            else:
                break
    
    # while loop to get more data if user want
    while row_data == "yes":
        row_data = input("\nWould you like to view more data?\n").lower()
        number_of_row += 5
        if row_data == "yes":
            print(df[number_of_row:number_of_row+5])
        else:
            break
            
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()