# scenexe3
A scenexe2.io bot because I have nothing better to do. Written in Python.
## How it works
First, Playwright opens a new Chromium window and navigates to the webpage. It's faster than Selenium and better at getting screenshots. Next, Playwright takes screenshots at the chosen action rate (how many screenshots are taken each second and how many actions the bot can take each second). Then PyAutoGUI (which is limited to the browser by pygetwindow) can take actions in game, and is fed data from OCRing text onscreen.
