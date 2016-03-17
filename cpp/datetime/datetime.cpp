#include "datetime.h"

//=====================  BODY  ==========================

//-----------------
// Constructors 
//-----------------

datetime::datetime(){
    now = time(0);
}

//-----------------
//   Destructor 
//-----------------

datetime::~datetime(){}

//-----------------
//   Refresher 
//-----------------

void datetime::refresh(){
    now = time(0);
}

//-----------------------
// Time stamp formatting 
//-----------------------

void datetime::format_year(){
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%Y", &tstruct);
    
    year = buf;
}

string datetime::get_year(){
    return year;
}

void datetime::format_fullmonth(){
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%B", &tstruct);
    
    month = buf;
}

void datetime::format_abbrmonth(){
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%b", &tstruct);
    
    month = buf;
}

void datetime::format_nummonth(){
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%m", &tstruct);
    
    month = buf;
}

string datetime::get_month(){
    return month;
}

void datetime::format_week(){
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%V", &tstruct);
    
    week = buf;
}

string datetime::get_week(){
    return week;
}

void datetime::format_dayofweek(){ // Sunday -> 0; Saturday -> 6
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%w", &tstruct);
    
    day = buf;
}

void datetime::format_dayofmonth(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%d", &tstruct);
    
    day = buf;
}

void datetime::format_dayofyear(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%j", &tstruct);
    
    day = buf;
}

string datetime::get_day(){
    return day;
}

void datetime::format_fullweekday(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%A", &tstruct);
    
    weekday = buf;
}

void datetime::format_abbrweekday(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%a", &tstruct);
    
    weekday = buf;
}

string datetime::get_weekday(){
    return weekday;
}

void datetime::format_hour24(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%H", &tstruct);
    
    hour = buf;
}

void datetime::format_hour12(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%I%p", &tstruct);
    
    hour = buf;
}

string datetime::get_hour(){
    return hour;
}

void datetime::format_minute(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%M", &tstruct);
    
    minute = buf;
}

string datetime::get_minute(){
    return minute;
}

void datetime::format_second(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%S", &tstruct);
    
    second = buf;
}

string datetime::get_second(){
    return second;
}

void datetime::format_UTCoffset(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%z", &tstruct);
    
    UTCoffset = buf;
}

string datetime::get_UTCoffset(){
    return UTCoffset;
}

void datetime::format_timezone(){ 
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%Z", &tstruct);
    
    timezone = buf;
}

string datetime::get_timezone(){
    return timezone;
}

string datetime::get_customtimestamp(string ref){
    string timestamp = "";
    string element = "";
    for(unsigned int i=0; i<ref.size(); i++){
        element = "";
        if(ref[i]=='Y'){
                format_year();
                element = year;
        }else if(ref[i]=='M'){
                format_fullmonth();
                element = month;
        }else if(ref[i]=='m'){
                format_abbrmonth();
                element = month;
        }else if(ref[i]=='n'){
            format_nummonth();
                element = month;
        }else if(ref[i]=='W'){
                format_week();
                element = week;
        }else if(ref[i]=='A'){
                format_dayofweek();
                element = day;
        }else if(ref[i]=='a'){
                format_dayofmonth();
                element = day;
        }else if(ref[i]=='X'){
                format_dayofyear();
                element = day;
        }else if(ref[i]=='B'){
                format_fullweekday();
                element = weekday;
        }else if(ref[i]=='b'){
                format_abbrweekday();
                element = weekday;
        }else if(ref[i]=='H'){
                format_hour24();
                element = hour;
        }else if(ref[i]=='h'){
                format_hour12();
                element = hour;
        }else if(ref[i]=='i'){
                format_minute();
                element = minute;
        }else if(ref[i]=='s'){
                format_second();
                element = second;
        }else if(ref[i]=='U'){
                format_UTCoffset();
                element = UTCoffset;
        }else if(ref[i]=='T'){
                format_timezone();
                element = timezone;
        }else{
                element = ref[i];
        }
        timestamp += element;
    }
    return timestamp;
}