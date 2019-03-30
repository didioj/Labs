# Lab 9:

## Screenshots and steps taken:

### Example 00:

First, I installed Docker using their Desktop client with Hyper-V.

![installed](Images/installed.PNG)
![whalesay](Images/whalesay.PNG)


### Example 01:

I then used Docker to open up an interactive bash terminal.

![terminal](Images/bash.PNG)

Then I installed Vim in the Ubuntu container, and used it. After that, I installed cowsay and ran it.

![viminstalled](Images/vim.PNG)
![vimuse](Images/vimuse.PNG)
![cowinstalled](Images/cowinstall.PNG)
![cowuse](Images/cowsay.PNG)

### Example 02:

I then installed and started an instance of mongoDB.

![mongoinstalled](Images/mongoinstall.PNG)

Then, I installed rocketchat, and used my web browser to ensure that it was running correctly.

![rocketinstall](Images/chatinstall.PNG)
![rocketuse](Images/rocketchat.PNG)


### Example 03:

Next, I created a Dockerfile to install a Python distribution, and I built it and ran it, inspecting the output in a web browser to make sure it was functioning correctly.

![pythoninstall](Images/pythoninstall.PNG)
![success](Images/pythonsuccess.PNG)

### Example 04:

I then set up a Node.js container with a dockerfile and built it. I also ran it to confirm that it would fail to connect at first.

![node](Images/nodeinstall.PNG)
![failure](Images/connectfail.PNG)

I then created a docker compose file, built it, and hosted it.

![composebuild](Images/composebuild.PNG)
![composeup](Images/composeup.PNG)

Finally, I used curl to add and modify some messages in the container.

![curlcomplete](Images/curlmessage1.PNG)
![curlmodded](Images/curlmessage2.PNG)