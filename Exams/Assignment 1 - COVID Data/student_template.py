import sys


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    for (date, county, state, fips, cases, deaths) in data:  # checks each column/index of data, naming them by their respective names.
        if cases >= 1 and county == "Rockingham" and state == "Virginia": 
            first_case_rockingham = date

            break

    for (date, county, state, fips, cases, deaths) in data:
        if cases >= 1 and county == "Harrisonburg city" and state == "Virginia":  # harrisonburg city isn't harrisonburg.
            first_case_harrisonburg = date

            break      
    
    return first_case_harrisonburg, first_case_rockingham

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    prevh = None
    prevr = None
    maxh = 0
    maxr = 0

    for (date, county, state, fips, cases, deaths) in data:

        if county == "Harrisonburg city" and state == "Virginia":

            if prevh is not None:

                dailynew = int(cases) - prevh  # sets dailynew to the total cases in a day minus the previous to get the total per day.

                if dailynew > maxh:  # if the daily amount of cases is higher than the prevously set max, the set max is changed to the new high.

                    maxh = dailynew
                    hdate = date

            prevh = int(cases)  # updates the previous value for next loop iteration.

    for (date, county, state, fips, cases, deaths) in data:

        if county == "Rockingham" and state == "Virginia":

            if prevr is not None:

                dailynew = int(cases) - prevr

                if dailynew > maxr:

                    maxr = dailynew
                    rdate = date
            prevr = int(cases)
    return hdate, rdate


def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    :return:
    """
    ## Harrisonburg City
    prevh = None
    maxcases = []


    for (date, county, state, fips, cases, deaths) in data:  # same for loop as before
       
       if county == "Harrisonburg city" and state == "Virginia":
         
         if prevh is not None:
             
             maxcases.append((date, int(cases) - prevh))  # add to the empty maxcases until the full set is complete. not just 7 days.

         prevh = int(cases)
    
    max_h = 0
    max_h_date = None

    for i in range(len(maxcases) - 6): # go through the first through n-6th term (so that there are no incomplete weeks)
        temp_sum = sum(cases for (date, cases) in maxcases[i:i+7])  # look at 7 days ahead and add all cases together.
        if temp_sum > max_h:  # if the added up sum is bigger than the previous max, update the max_h varaible as well as both dates.
            max_h = temp_sum
            max_h_date1 = maxcases[i][0]
            max_h_date2 = maxcases[i+6][0]  # goes from the index being analyzed to 6 days after, encompasing the full range.
            mtotal = str(f"The worst 7-day period in Harrisonburg was {max_h_date1} through {max_h_date2}.\n")  # the date range is just the 
  
    
    return mtotal

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

   ## for (date,county, state, fips, cases, deaths) in data:
   ##     print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')

    print("\n \nMy name is Brooke McManus, and I have abided by the JMU Honor Code. \n")

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?


        # As per the code under first_question, the first positive case in Rockingham was on March 22nd, 2020.


    # When was the first positive COVID case in Harrisonburg?


        # As per the code under first_question, the first postive case in Rockingham was on March 13th, 2020.


    first_case_harrisonburg, first_case_rockingham = first_question(data)


    print(f"The date of the first case in Harrisonburg is {first_case_harrisonburg}\n")
    print(f"The date of the first case in Rockingham is {first_case_rockingham}\n")


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?


        # The date of the highest new daily cases in Harrisonburg was January 10th, 2022.


    # What day was the greatest number of new daily cases recorded in Rockingham County?


        # The date of the highest new daily cases in Rockingham was January 17th, 2022.
    
    
    hdate, rdate = second_question(data)


    print(f"Greatest new daily cases in Harrisonburg: {hdate}\n")
    print(f"Greatest new daily cases in Rockingham: {rdate}\n")
    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?


    # Harrisonburg City was selected. The 7-day period with the most cases was January 6th, 2022 to January 12th, 2022, including the 6th and 12th as a full day.
   
    mtotal = third_question(data)

    print(mtotal)



