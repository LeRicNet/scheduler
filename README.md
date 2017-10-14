# Scheduler
***
### Kivy Based Application for Scheduling Machine Space
### 
***
#### Objective

There is a common-use instrument that is currently being scheduled using a shared Google Drive.  There is always confusion about how to properly read the color coded system.  To remedy this, I will create a Kivy based application that will handle the scheduling in a more intuitive, graphics-based approach.

#### Reasoning

The underlying idea of a scheduler is an admittedly straight-forward task.  I chose an idea such as this to develop an application around to avoid getting bogged down in technicalities.  The primary exercise I am facing here is to use [Object-Oriented Programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming) in python to design and devlop a relatively pleasing graphic interface to schedule time for the machine.  This poses challenges in terms of design/aesthetics, program design aspects such as proper class implementation and error handling, and deployment cross-platform.

[Kivy](https://kivy.org/#home) is a cross-platform application interface which can be utilized in python.  I have previously used [TkInter](https://wiki.python.org/moin/TkInter), but I found the graphics to be very outdated at the default level.  Eventually, I would like to build various sized applications and would like to be able to implement them both on a mobile device as well as a desktop.  Both of these issues seemed to be addressed in the Kivy package so, at least initially, I will go down that route.

Lastly, I want to make sure I adhere to the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide to demonstrate compentency at the professional level.

As I develop this application I will upload issues I had to overcome, and how I overcame them.  I will also add renderings of my interface when I reach the point of generating them.

#### Development Notes

* Login Screen:
  + The login screen will be a fixed, borderless, non-scalable rectangular screen with a background texture.  I aim to create a professional interface on application start-up
  + In my initial handling of this task, I became aware of an important design concept: [Separation of Concerns (SoC)](https://en.wikipedia.org/wiki/Separation_of_concerns).  This concept states that applications should be constructed in a modular format such that development and maintenance of the program are efficiently managed.  SoC is achieved via OOP because information can be encapsulated in classes, with information being with hidden or available as necessary to outside classes.  SoC will be considered in my project by separating the code into a Python-based program and a [KV-based](https://kivy.org/docs/guide/lang.html) program for GUI; visual components will be constructed via KV and the functionality will be implemented via Python, thus ensuring modularity. _note_: I recognize that KV is compiled through Python, so it effectively functions as the same language but the purpose of SoC is only for the components of a program to be modular.  Alternatively, I could achieve SoC using only pure Python by separating functionality and GUI into separate python classes by importing modules such as `Config`, `Window`, & `Canvas`.
  + This process has led me to learn the proper methods for password storage including using salt and hash sha256 algorithms.  This is a complex task upon first glance, but I will make my way through it to ensure sufficient security is implemented.

* Scheduling Status Screen:
  + In Development…
