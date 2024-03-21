# LethalTracker v1.31 by Artemis64

This program is meant to be an all-in-one scrap tracker for Lethal Company!
While the spreadsheets that exist are pretty nice and do give a bit more detail, i think they are generally rough on the eyes and don't have a great way to be displayed on stream. I figured making this would both simplify usage and also be easy to capture in OBS. (Improved in 1.2!)

This is also my first time making a full program like this! Let me know if you like it through [Twitter](https://twitter.com/artemis6425) or Discord (both artemis6425)

3270font (aka the Lethal Company font) was created by [Ricardo Bánffy](https://github.com/rbanffy) and others, please read `Font License.txt` and view the fonts [github page](https://github.com/rbanffy/3270font/tree/main)!

![screenshot of LethalTracker](https://i.imgur.com/l4pmPTK.png)

## Features

- All-inclusive LethalTracker.exe file so you don't have to deal with my messy code!
- Built-in overtime calculator (with possibility to calculate how much you need to sell to hit quota!) **fixed in v1.31!**
- Ability to estimate future quotas
- Option to open a window specifically designed to be captured by OBS **added in v1.2!**
- ...and more!

## Download 

[**Download the latest release**](https://github.com/Artemis6425/LethalTracker/releases/latest). No need to download the source code!

## How to Use

Once you open `LethalTracker.exe`, you'll be greeted by the credits screen. Click the `Credits` button at the top to close it and get to the main menu of it.
If you plan to go for high score runs, make sure "HIGH SCORE RUN" is selected on the top right. From there, you can start tracking your daily scrap on the left side of the screen, and watch your stats change in real time!

If you plan on going for specific quota runs, make sure "QUOTA # RUN" is selected, and fill out the box with the goal quota. By default, this sets itself to 10. From there, you will have a few extra stats on the right side, but otherwise usage is the same! Please note that if you do skip any days, put "0" in those days so the program can continue doing math correctly for you.

If you want to show the stats in OBS as well, click the OBS button on the credits screen. This will open up a dedicated window to just show the stats in a higher quality, as well as having the ability to change the font color and background color for easier chroma-keying!

## Known issues

- Using this program on a 4k monitor causes the scaling to be completely messed up. 1080p and 1440p monitors *should* be fine, with few exceptions
- My code is fairly messy, but I've never made something like this before so just pretend its ok!

## Future ideas

- Pull the data straight from the LethalCompany.exe itself during the game, removing the need to type this in. (Would be banned from the Lethal Company speedrun.com board if I were to do this. Considering alternatives, such as taking screenshots automatically)

## Changelog

### v1.0 "Initial Release"

- Initial Release!
- Includes the Overtime Calculator, along with tracking of many stats

### v1.1

- Added the "Reset Confirmation" Dialog Box. Thank you for the feedback!

### v1.2 "Better for OBS"

- Added a button on the Credits screen that opens a `LethalTracker OBS` window. This shows the stats that the main window would, but in a bigger font size, and with the ability to change the text and background color. Thank you for the feedback!

### v1.3 "Updated Calculator"

- Fixed bug where the `LethalTracker OBS` window wasn't updating the top line when resetting. Thank you for letting me know!
- Merged Tomatobird8's branch, which formats the text in the `LethalTracker OBS` window to allow for bigger numbers. Thank you for the contribution!
- Added the ability to change calculator into "Overtime" and "No OT" modes. Makes it possible to calculate how much you need to sell to hit quota, ignoring overtime. Thank you for the feedback!

### v1.31 "FIXED CALCULATOR"

- Fixed the calculator function to properly calculate the overtime needed, with help from bryanclst
- Changed the "Company Buy %" to a "Days Remaining" field, to make the calculator more accurate (and easier to use) from feedback from bryanclst.
Thank you for the feedback!

### v1.32 "fixed average"

- Fixed the average quota estimate, as the calculation was slightly off. (thanks eleventybillion!)