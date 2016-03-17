#ifndef DATETIME_H
#define DATETIME_H

#include <iostream>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <complex>
#include <string>
#include <stdio.h>
#include <time.h>
#include <cmath>
#include <stdlib.h>
//#include <cstdlib>     //to get current directory
//#include <unistd.h>    //to get home directory
//#include <sys/types.h> //to get home directory
//#include <pwd.h>       //to get home directory 
//#include <sys/stat.h>     //create new directory
//#include <sys/types.h>    //create new directory
//#include <boost/filesystem.hpp>
//#include <boost/tokenizer.hpp>
//#include <boost/token_functions.hpp>
//#include <boost/algorithm/string/join.hpp>
//#include <exception>
#include <typeinfo>
#include <omp.h>

using namespace std;
//using namespace boost;
//using namespace boost::filesystem;

//===========================================================//
//===========================================================//
/*
  A class to implement a current date and time stamp generator
*/
//===========================================================//
//===========================================================//


//===================================================
//==================  HEADER  =======================
//===================================================

class datetime {

//===================================================  
//                  Variables
//===================================================
private:
// Control parameters
  time_t now;
// Output quantities
  string year,
         month,
         week,
         day,
         weekday,
         hour,
         minute,
         second,
         UTCoffset,
         timezone;
  
//===================================================  
//                      Methods
//===================================================  
public:
  
  // Constructor (default)
  datetime();
  
  //Destructor
  ~datetime();
  
  void refresh();
  
  void format_year(),                   // Reference: Y
       format_fullmonth(),              // Reference: M
       format_abbrmonth(),              // Reference: m
       format_nummonth(),               // Reference: n
       format_week(),                   // Reference: W
       format_dayofweek(),              // Reference: A
       format_dayofmonth(),             // Reference: a
       format_dayofyear(),              // Reference: X
       format_fullweekday(),            // Reference: B
       format_abbrweekday(),            // Reference: b
       format_hour24(),                 // Reference: H
       format_hour12(),                 // Reference: h
       format_minute(),                 // Reference: i
       format_second(),                 // Reference: s
       format_UTCoffset(),              // Reference: U
       format_timezone();               // Reference: T

  string get_year(),
         get_month(),
         get_week(),
         get_day(),
         get_weekday(),
         get_hour(),
         get_minute(),
         get_second(),
         get_UTCoffset(),
         get_timezone(),
         get_customtimestamp(string ref);
  
   
};

#endif