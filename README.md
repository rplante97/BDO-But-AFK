# BDO-But-AFK
Humans are just meat based bots

- In order for Python to provide game inputs the script *MUST* be run as administrator (otherwise Python is not permitted to grab the window handle).
- game_input_method1 sends key scan codes directly to the directX engine in order to send input to BDO, game_input_method2 utilizes windows V_Keys. In both cases the BDO must be in focus in order for inputs to register.

# Roadmap

**Problem 1:** Send keyboard and mouse input to the game in a programmatic fashion.
- Solved by game_input_method1 or game_input_method2

**Problem 2:** Develop a system for determining player location, displacement and results of movements.
- Potentially solved? Capturing minimap image after/during movement and using image translation algorithm can provide a pixel based movement map.

**Problem 3:** Detect and recognize different in game entities from an image.
- Potential OpenCV image detection solution, currently a WIP. 

**Problem 4:** Create decision engine to formulate an in game action based on supplied inputs.
- Not started

**Problem 5:** Error handling, failsafes, etc. Bot should be robust enough to handle reasonable challenges such as pathing issues related to getting stuck on a rock or fence. Bot failure should not result in suspicious behavior.

