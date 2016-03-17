/**
        Project: Mechanics of Extreme Thin Composite Layers for Aerospace applications
         Author: Luca Di Stasio
    Institution: Université de Lorraine & Luleå University of Technology
        Version: 10.2015
  Creation date: October 20th, 2015
    Last update: February 1st, 2016

    Description: 
          Input: 
         Output:
         
    @author Luca Di Stasio
    @version 10.2015
*/

//#include <boost/program_options/options_description.hpp>
//#include <boost/program_options/parsers.hpp>
//#include <boost/program_options/variables_map.hpp>

#include <iostream>

#include "datetime.h"

using namespace std;
//using namespace boost;
//using namespace boost::program_options;

//==================  MAIN  =======================
int main(int argc, char** argv)
{
  datetime today;
  
  today.format_year();
  cout << "Year " << today.get_year() << endl;
  
  today.format_fullmonth();
  cout << "Month " << today.get_month() << endl;
  
  today.format_abbrmonth();
  cout << "Month " << today.get_month() << endl;
  
  today.format_nummonth();
  cout << "Month " << today.get_month() << endl;
  
  today.format_week();
  cout << "Week " << today.get_week() << endl;
  
  today.format_dayofweek();
  cout << "Day of week " << today.get_day() << endl;
  
  today.format_dayofmonth();
  cout << "Day of month " << today.get_day() << endl;
  
  today.format_dayofyear();
  cout << "Day of year " << today.get_day() << endl;
  
  today.format_hour24();
  cout << "Hour " << today.get_hour() << endl;
  
  today.format_hour12();
  cout << "Hour " << today.get_hour() << endl;
  
  today.format_minute();
  cout << "Minute " << today.get_minute() << endl;
  
  today.format_second();
  cout << "Second " << today.get_second() << endl;
  
  today.format_UTCoffset();
  cout << "UTC offset " << today.get_UTCoffset() << endl;
  
  today.format_timezone();
  cout << "Timezone " << today.get_timezone() << endl;
  
  cin.get();
  
  today.refresh();
  
  today.format_year();
  cout << "Year " << today.get_year() << endl;
  
  today.format_fullmonth();
  cout << "Month " << today.get_month() << endl;
  
  today.format_abbrmonth();
  cout << "Month " << today.get_month() << endl;
  
  today.format_nummonth();
  cout << "Month " << today.get_month() << endl;
  
  today.format_week();
  cout << "Week " << today.get_week() << endl;
  
  today.format_dayofweek();
  cout << "Day of week " << today.get_day() << endl;
  
  today.format_dayofmonth();
  cout << "Day of month " << today.get_day() << endl;
  
  today.format_dayofyear();
  cout << "Day of year " << today.get_day() << endl;
  
  today.format_hour24();
  cout << "Hour " << today.get_hour() << endl;
  
  today.format_hour12();
  cout << "Hour " << today.get_hour() << endl;
  
  today.format_minute();
  cout << "Minute " << today.get_minute() << endl;
  
  today.format_second();
  cout << "Second " << today.get_second() << endl;
  
  today.format_UTCoffset();
  cout << "UTC offset " << today.get_UTCoffset() << endl;
  
  today.format_timezone();
  cout << "Timezone " << today.get_timezone() << endl;
  
  string ref1 = "H:i:s, M Y, B";
  string ref2 = "H:i:s Y-n-a";
  string ref3 = "Y-n-a H:i:s";
  string ref4 = "Y-n-a -> A/a/X/b/B";
  string ref5 = "Y-n-a -> W";
  string ref6 = "Y-n-a H:i:s <-> Y-n-a h:i:s";
  
  cout << endl;
  cout << today.get_customtimestamp(ref1) << endl;
  cout << endl;
  cout << today.get_customtimestamp(ref2) << endl;
  cout << endl;
  cout << today.get_customtimestamp(ref3) << endl;
  cout << endl;
  cout << today.get_customtimestamp(ref4) << endl;
  cout << endl;
  cout << today.get_customtimestamp(ref5) << endl;
  cout << endl;
  cout << today.get_customtimestamp(ref6) << endl;
  cout << endl;
  
  return 0;
}