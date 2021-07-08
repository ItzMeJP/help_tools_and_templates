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

The code below allow to open a process and get the pid (command like roslaunch could be a problem since it generates several pids). This approach also does NOT recognize termination process, thus do not kill the subprocesses when the code is finished or destroyed.(This approach need to be better designed) :

```
#include <unistd.h>
#define READ   0
    #define WRITE  1
    FILE * popen2(std::string command, std::string type, int & pid)
    {
        pid_t child_pid;
        int fd[2];
        pipe(fd);

        if((child_pid = fork()) == -1)
        {
            perror("fork");
            exit(1);
        }

        /* child process */
        if (child_pid == 0)
        {
            if (type == "r")
            {
                close(fd[READ]);    //Close the READ end of the pipe since the child's fd is write-only
                dup2(fd[WRITE], 1); //Redirect stdout to pipe
            }
            else
            {
                close(fd[WRITE]);    //Close the WRITE end of the pipe since the child's fd is read-only
                dup2(fd[READ], 0);   //Redirect stdin to pipe
            }

            setpgid(child_pid, child_pid); //Needed so negative PIDs can kill children of /bin/sh
            execl("/bin/sh", "/bin/sh", "-c", command.c_str(), NULL);
            exit(0);
        }
        else
        {
            if (type == "r")
            {
                close(fd[WRITE]); //Close the WRITE end of the pipe since parent's fd is read-only
            }
            else
            {
                close(fd[READ]); //Close the READ end of the pipe since parent's fd is write-only
            }
        }

        pid = child_pid;

        if (type == "r")
        {
            return fdopen(fd[READ], "r");
        }

        return fdopen(fd[WRITE], "w");
    }
```
