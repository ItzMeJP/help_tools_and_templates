## Call exec inside C++ code

### Blocked-call
To call an executable inside a C++ code, use:

```
#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>

std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

```

Pre-C++11 version:

```
include <iostream>
#include <stdexcept>
#include <stdio.h>
#include <string>

std::string exec(const char* cmd) {
    char buffer[128];
    std::string result = "";
    FILE* pipe = popen(cmd, "r");
    if (!pipe) throw std::runtime_error("popen() failed!");
    try {
        while (fgets(buffer, sizeof buffer, pipe) != NULL) {
            result += buffer;
        }
    } catch (...) {
        pclose(pipe);
        throw;
    }
    pclose(pipe);
    return result;
}

```

Replace popen and pclose with _popen and _pclose for Windows.

### Non blocked Call

In the following case, the timeout exists just to collect output from a period. Otherwise the call will be exec and no output is stored. It is just a option criteria

```
std::string exec(const char *cmd) {

        float timeout = 0, deadline = 8;

        char buffer[128];
        //std::shared_ptr<std::string> result = std::make_shared<std:string>();
        std::string result;
        FILE *pipe = popen(cmd, "r");
        int descriptor = fileno(pipe);
        fcntl(descriptor, F_SETFL, O_NONBLOCK);

        const clock_t begin_time = clock();

        while (timeout < deadline) {
            timeout = float(clock() - begin_time)/CLOCKS_PER_SEC;
            //std::cout << "timeout " << timeout << std::endl;

            ssize_t r = read(descriptor, buffer, 128);

            if (r == -1 && errno == EAGAIN){}
                //std::cout << "nada ainda " << std::endl;
            else if (r > 0) {
                result += buffer;

            } else
                std::cout << "pipe closed " << std::endl;
        }
        std::cout << "acabou  ------------- "<< result.size() << std::endl;

        return result;
    }
```
