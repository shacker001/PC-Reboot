#include <iostream>
#include <cstdlib>

#ifdef _WIN32
#include <windows.h>
#endif

int main() {
    #ifdef _WIN32 //For windows
        std::system("shutdown /r /t 1");
    #elif defined __linux__ // For linux
        std::system("sudo reboot");
    #else
        std::cout<<"Restart functionality not supported on this operating system."<< std::endl;
    #endif
    return 0;
}