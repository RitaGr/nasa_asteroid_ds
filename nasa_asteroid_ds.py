import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os


def load_data(file_name):
    '''
    The function gets a file of csv type and returns a Data Frame of pandas.
    :param file_name : a file of type csv
    :return: pandas.DataFrame : pandas version of the csv file
    '''
    try:
        # check if file exists
        if not os.path.isfile(file_name):
            raise FileNotFoundError(f"File '{file_name}' does not exist.")
        # check file extension (if csv)
        if not file_name.lower().endswith('.csv'):
            raise ValueError(f"File '{file_name}' is not a CSV file.")

        df = pd.read_csv(file_name, sep=',')

        if df.empty:
            raise ValueError(f"File '{file_name}' is empty.")

        return df
    # handle errors
    except FileNotFoundError as err:
        print(f"FileNotFoundError: {err}")
    except ValueError as err:
        print(f"Value Error : {err}")
    except OSError:
        print(f"OSError: Unable to open file \'{file_name}\'.")
    except Exception as err:
        print(f"An error occurred: {err}")


def mask_data(df):
    '''
    Filters the given DataFrame to exclude asteroids with a close approach date before the year 2000.
    :param df : pandas.DataFrame -  DataFrame including the info on asteroids close to earth
    :return: pandas.DataFrame: A filtered DataFrame including only rows with a close approach date from 2000 and onward
    '''
    # Keep rows where the year (first 4 characters of the date string) is >= '2000'
    filtered_df = df[df['Close Approach Date'].str[:4] >= '2000'] # filter and keep only those beyond 2000s
    return filtered_df


def data_details(df):
    '''
    The function drops the columns: 'Orbiting Body', 'Neo Reference ID', and 'Equinox' and returns a tuple containing:
    the number of rows (int), the number of columns after dropping (int), list of the remaining column names (list of str)
    :param df: pandas.DataFrame – The input DataFrame containing asteroid data
    :return: tuple = (num_rows, num_columns, list_of_updated_column_names)
    '''
    df = df.drop(columns=['Orbiting Body','Neo Reference ID', 'Equinox']) # remove specific columns
    # get the shape of the DataFrame (returns a tuple: (num_rows, num_columns))
    df_info = list(df.shape)  # convert the shape tuple to a list, so we can append to it

    # append a list of the column names to the shape info
    df_info.append(list(df.columns))  # now df_info = [num_rows, num_columns, [column names]]

    # convert the list back to a tuple for final output
    df_info = tuple(df_info)

    # return a tuple: (number of rows, number of columns, list of column names)
    return df_info


def max_absolute_magnitude(df):
    '''
    The function finds the asteroid with the highest absolute magnitude.

    :param df: pandas.DataFrame – DataFrame containing asteroid data
    :return: tuple – (asteroid_name: int, absolute_magnitude: float)
    '''
    # sort by 'Absolute Magnitude' descending
    temp_df = df.sort_values(by='Absolute Magnitude', ascending=False)

    # get the values from the first row(max) and convert to Python types
    abs_magnitude = float(temp_df.iat[0, df.columns.get_loc('Absolute Magnitude')])
    asteroid_name = int(temp_df.iat[0, df.columns.get_loc('Name')])

    # return a tuple
    return asteroid_name, abs_magnitude


def closest_to_earth(df):
    '''
    The function finds and returns the name of the asteroid that came closest to Earth,
    based on the 'Miss Dist.(kilometers)' column.
    :param df: pandas.DataFrame – DataFrame containing asteroid data
    :return: int – asteroid name as an integer
    '''
    # sort by miss distance (closest first)
    temp_df = df.sort_values(by='Miss Dist.(kilometers)', ascending=True)

    # get the name/ID of the closest asteroid
    asteroid_name = int(temp_df.iat[0, df.columns.get_loc('Name')])

    return asteroid_name

def common_orbit(df):
    '''
    The function counts how many times each Orbit ID appears in the DataFrame
    and returns a dictionary with Orbit ID as keys and counts as integer values.

    :param df: pandas.DataFrame – DataFrame containing asteroid data
    :return: dict – {orbit_id: count}
    '''
    # convert each counter to integer from numpy and create a dict with Orbit ID as keys, counts as values
    return {name: int(count) for name, count in df['Orbit ID'].value_counts().items()}

def min_max_diameter(df):
    '''
    The function calculates and returns the number of asteroids whose maximum estimated diameter
    is greater than the average maximum diameter of all asteroids in the DataFrame.

    :param df: pandas.DataFrame – DataFrame containing asteroid data
    :return: int – number of asteroids with max diameter above average
    '''
    # calculate the mean of max asteroid diameter
    avg_diameter = df['Est Dia in KM(max)'].mean()

    # count the amount of asteroids above the average max diameter
    count = (df['Est Dia in KM(max)'] > avg_diameter).sum()

    # return int count
    return int(count)


def plt_hist_diameter(df):
    '''
    The function calculates the average estimated diameter of each asteroid based on the minimum and maximum
    diameter values in the DataFrame, and plots a histogram showing the distribution of those
    average diameters using 100 continuous bins.
    :param df:  pandas.DataFrame – DataFrame containing asteroid data
    :return: None – displays a matplotlib histogram
    '''
    # calculating the average diameter size
    df['Est Dia in KM(avg)'] = (df['Est Dia in KM(min)'] + df['Est Dia in KM(max)']) / 2

    # building histogram
    plt.hist(df['Est Dia in KM(avg)'], bins=100, color='#990f02', edgecolor='black')
    # histogram title
    plt.title('Distribution of Average diameter size', fontsize=14)
    # labels for the axes
    plt.xlabel('Average Value', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    # add grid
    plt.grid(axis = 'y')

    # display the histogram
    plt.show()


def plt_hist_common_orbit(df):
    '''
    Plots a histogram of number of asteroids based on their 'Minimum Orbit Intersection' values.

    :param df: pandas.DataFrame – DataFrame containing asteroid data
    :return: None – displays a matplotlib histogram
    '''

    # Sort descending
    temp_df = df.sort_values(by='Minimum Orbit Intersection', ascending=False)
    # building histogram
    plt.hist(temp_df['Minimum Orbit Intersection'], bins=10, color='#990f02', edgecolor='black')

    # histogram title
    plt.title('Distribution of Asteroids by Minimum Orbit Intersection', fontsize=14)
    # labels for the axes
    plt.xlabel('Min Orbit Intersection', fontsize=12)
    plt.ylabel('Number of Asteroids', fontsize=12)
    # add grid
    plt.grid(axis = 'y')

    # display the histogram
    plt.show()


def plt_pie_hazard(df):
    '''
    The function plots a pie chart showing the percentage distribution of hazardous and non-hazardous asteroids.

    :param df: pandas.DataFrame –  DataFrame containing asteroid data
    :return: None – displays a matplotlib pie chart
    '''
    pie_labels = ['True', 'False']
    count_true = (df['Hazardous'] == True).sum()  # sum the amount of hazardous asteroids
    count_false = (df['Hazardous'] == False).sum()  # sum the amount of non-hazardous asteroids
    items = [count_true, count_false]  # create a list of those values
    explode = (0, 0.1)  # only "explode" the 2nd slice (part of pie chart design)
    plt.pie(items, labels=pie_labels, explode=explode, colors=['#990f02', '#d4a017'], autopct='%1.1f%%')  # create pie chart
    plt.title('Percentage of Hazardous and Non-Hazardous Asteroids')  # title of the pie chart
    # display the pie chart
    plt.show()


def plt_linear_motion_magnitude(df):
    '''
    The function performs a linear regression analysis between 'Miss Dist.(kilometers)' and 'Miles per hour' from the DataFrame,
    and if the p-value indicates statistical significance (p < 0.05), plots the data points along with the regression line.

    From the results of the plotting we can clearly see that p < 0.05 is indeed True, thus
    there is a statistically significant linear relationship between the asteroid's miss distance (in kilometers) and its speed (in miles per hour).

    :param df: pandas.DataFrame – DataFrame containing asteroid data
    :return: None – displays a scatter plot with regression line if significant
    '''
    # linear regression evaluation
    x = df['Miss Dist.(kilometers)']
    y = df['Miles per hour']
    a, b, r_value, p_value, std_err = stats.linregress(x, y)
    if p_value < 0.05:
        plt.scatter(x, y, label="Data points")
        plt.plot(x, a*x + b, label="Regression line", color="red")

        plt.legend()  # add built-in label explaining the components of the histogram
        plt.grid()  # add grid to the plot
        plt.title('Linear Regression: Absolute Magnitude vs Miles per hour')  # title of the histogram
        # labels for the axes
        plt.xlabel('Absolute Magnitude', fontsize=12)
        plt.ylabel('Miles per hour', fontsize=12)
        # display the histogram
        plt.show()

# Tester
df = load_data('nasa.csv')
print(df)
df = mask_data(df)
print(df)
print(max_absolute_magnitude(df))
print(closest_to_earth(df))
print(common_orbit(df))
print(min_max_diameter(df))
plt_hist_diameter(df)
plt_hist_common_orbit(df)
plt_pie_hazard(df)
plt_linear_motion_magnitude(df)