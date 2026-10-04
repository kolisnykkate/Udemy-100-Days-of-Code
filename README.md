# 100 Days of Code: The Complete Python Pro Bootcamp

This repository is my ongoing work through [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Angela Yu. I add exercises and projects as I complete them, so the repository will grow over time. The programs are small, mostly independent projects rather than one installable application.

## Repository layout

- `Day N` folders contain exercises and projects grouped by course day. More days and tasks will be added as I progress.
- Folders such as `day-16-start`, `day-17-start`, `day-18-start`, `day-19`, `day-25`, and `day-26_list_comprehention` contain work organized by lesson or project.
- Folders such as `CoffeeMachine`, `Mail Merge Project`, `pong`, `snake_game`, and `turtle-crossing` contain standalone projects completed along the way.
- Many exercises include both a `task.py` and a `solution.py`; some project folders use `main.py` as the entry point.

## Getting started

Use Python 3. Each folder is intended to be explored and run on its own. Open a folder in your editor, then run its relevant script from that folder. For example:

```bash
cd pong
python3 main.py
```

Some programs read or write files using paths relative to their project folder, so run them with that folder as the working directory. Turtle graphics projects also need a Python installation with Tk support and a desktop display.

## Installing third-party packages

Most lessons use only Python's standard library. A few projects have their own `requirements.txt`; install packages from the relevant project directory:

```bash
cd day-16-start
python3 -m pip install -r requirements.txt
```

Project dependency files are located in:

- `day-16-start/requirements.txt` — PrettyTable exercise
- `day-18-start/hirst_art/requirements.txt` — Hirst painting color extraction
- `day-25/requirements.txt` — pandas exercises
- `day-25/us-states-game/requirements.txt` — pandas and Pillow

Then run the script from that project folder. The US states game has its own dependency file because it is a separate project nested under `day-25`.

## Notes

This is a work in progress. Some exercises are intentionally incomplete, and task and solution files may show different stages of a lesson. I will continue adding and updating folders as I complete more of the course.
