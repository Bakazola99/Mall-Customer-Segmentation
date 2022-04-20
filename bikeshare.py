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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    df = pd.read_csv(CITY_DATA [city])
    view_data = input("Would you like to view 5 rows of City data? Enter yes or no?")
    start_loc = 0
    while ("yes"):
        print(df.iloc[:5])
        start_loc += 5
        view_display = input("Do you wish to continue?:").lower()
        start_loc = 5
        while ("yes"):
            print(df.iloc[:5])
            start_loc += 5
    else:
        print("Thank you")
        
                                 

    # TO DO: get user input for month (all, january, february, ... , june)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] =df['Start Time'].dt.month
                       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    df['day of week'] = df['Start Time'].dt.weekday_name

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month =  df['month'].mode()
    # TO DO: display the most common day of week
    common_week = df['day of week'].mode()
    


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station =(df['Start Station']).mode()

    # TO DO: display most commonly used end station
    popular_end_station = (df['End Station']).mode()
    

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = df['Start Station'].append(df['End Station'])
    freq_com = (combination_start_end).mode()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_travel = sum(df['Trip Duration'])

    # TO DO: display mean travel time
    mean_time_travel = df['Trip Duration'].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    number_of_user = df['User Type'].count()
    number_of_each_user = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    if 'Gender' in df:
    number_of_gender = df['Gender'].count()
    number_of_each_gender = df['Gender'].value_counts()
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
    earliest_birth = sorted(df['Birth Year'])
    most_recent = sorted(df['Birth Year'])
    most_common_year = (df['Birth Year']).mode()
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
