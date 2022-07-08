
#include <iostream>
#include<time.h> 
#include <sstream>
#include<typeinfo>
#include<stdlib.h>
#include<windows.h>

using namespace std;

int main(){
	time_t now = time(NULL);
	tm* tm_t = localtime(&now);
	std::stringstream ss;
	ss << "year:" << tm_t->tm_year + 1900 << " month:" << tm_t->tm_mon + 1 << " day:" << tm_t->tm_mday
		<< " hour:" << tm_t->tm_hour << " minute:" << tm_t->tm_min << " second:" << tm_t->tm_sec;
 
    std::cout << ss.str();

	int hour = tm_t->tm_hour;
	int min = tm_t->tm_min;
	int sec = tm_t->tm_sec;
	
	
	if(hour == 5 && min <= 59){
		while(min < 59){
			Sleep(60000);
			now = time(NULL);
			tm_t = localtime(&now);
			min = tm_t->tm_min;
		}
		while(min == 59 && sec <= 57){
				Sleep(1000);
				now = time(NULL);
				tm_t = localtime(&now);
				sec = tm_t->tm_sec;
				system("cls");
				cout << endl;
				ss << "year:" << tm_t->tm_year + 1900 << " month:" << tm_t->tm_mon + 1 << " day:" << tm_t->tm_mday
				<< " hour:" << tm_t->tm_hour << " minute:" << tm_t->tm_min << " second:" << tm_t->tm_sec;
 
    			std::cout << ss.str();
			}
		system("cd C:\\Users\\BlingCc\\Documents\\code");
		system("shutdown -s -t 120");
		system("python auto.py");
	}
	else if(hour == 6){
		system("cd C:\\Users\\BlingCc\\Documents\\code");
		system("shutdown -s -t 120");
		system("python auto.py");
	}
	else if(hour != 5 && hour != 6){
		exit(0);
	}
	

	
	return 0;
}
