import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Prompt the user to specify a city, month, and day for analysis.

    Input validation is performed in a loop until the user enters a supported city,
    month, and day of week.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Validate city name until a supported city is entered.
    while True:
        city = input('Which city would you like to analyze? (chicago, new york city, washington)\n').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please choose from chicago, new york city, or washington.')

    # Validate month until a supported month or 'all' is entered.
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('Which month would you like to filter by? (january, february, march, april, may, june, or all)\n').lower()
        if month in months:
            break
        else:
            print('Invalid input. Please choose from january, february, march, april, may, june, or all.')

    # Validate day of week until a supported day or 'all' is entered.
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input('Which day of week would you like to filter by? (monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all)\n').lower()
        if day in days:
            break
        else:
            print('Invalid input. Please choose from monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Load the city data and apply month/day filters.

    Args:
        city (str): name of the city to analyze
        month (str): name of the month to filter by, or "all" for no month filter
        day (str): name of the day of week to filter by, or "all" for no day filter

    Returns:
        df (DataFrame): filtered data for the selected city
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Calculate and print the most frequent travel times."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Determine the most common month in the filtered dataset.
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].mode()[0]
    print('Most common month: {}'.format(months[most_common_month - 1].title()))

    # Determine the most common day of week in the filtered dataset.
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day: {}'.format(most_common_day))

    # Determine the most common start hour in the filtered dataset.
    most_common_hour = df['hour'].mode()[0]
    print('Most common start hour: {}:00'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Calculate and print popular station and trip statistics."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Compute the most commonly used start station.
    most_common_start = df['Start Station'].mode()[0]
    print('Most commonly used start station: {}'.format(most_common_start))

    # Compute the most commonly used end station.
    most_common_end = df['End Station'].mode()[0]
    print('Most commonly used end station: {}'.format(most_common_end))

    # Compute the most frequent combination of start and end station.
    most_common_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most frequent trip: {}'.format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Calculate and print trip duration totals and averages."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Compute total travel time for all trips in the filtered dataset.
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {} seconds ({} hours)'.format(int(total_travel_time), int(total_travel_time / 3600)))

    # Compute average travel time for trips in the filtered dataset.
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: {} seconds ({} minutes)'.format(int(mean_travel_time), int(mean_travel_time / 60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Calculate and print statistics on bikeshare user demographics."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Print the number of users by type.
    print('User Types:')
    print(df['User Type'].value_counts())

    # Print gender counts, if available for the selected city.
    if 'Gender' in df.columns:
        print('\nGender:')
        print(df['Gender'].value_counts())
    else:
        print('\nGender data not available for this city.')

    # Print birth year statistics, if available for the selected city.
    if 'Birth Year' in df.columns:
        print('\nBirth Year:')
        print('Earliest birth year: {}'.format(int(df['Birth Year'].min())))
        print('Most recent birth year: {}'.format(int(df['Birth Year'].max())))
        print('Most common birth year: {}'.format(int(df['Birth Year'].mode()[0])))
    else:
        print('\nBirth year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Display raw data in an interactive manner, 5 rows at a time, upon user request.
def display_raw_data(df):
    """Prompt the user and print raw data rows in batches of 5."""
    view_raw_data = input('\nWould you like to see the raw data? Enter yes or no.\n').lower()
    start_row = 0
    while view_raw_data == 'yes':
        print(df.iloc[start_row:start_row+5])
        start_row += 5
        view_raw_data = input('Would you like to see 5 more rows of data? Enter yes or no.\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
