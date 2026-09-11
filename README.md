# Facial Recognition Attendance System

A Tkinter desktop application that enrols people from a webcam, trains an OpenCV LBPH face
recogniser, and marks attendance to a CSV when it recognises a face. Student/staff records are kept
in MySQL.

## What it does

`main.py` opens a full-screen dashboard with eight buttons, each backed by its own module:

| Button | Module | What it does |
| --- | --- | --- |
| User Details | `UserDetailsButton.py` | CRUD over a `userdetails` MySQL table (department, course, year, semester, ID, name, gender, DOB, email, phone, address, teacher). A "Take Photo Sample" radio option captures face crops from the webcam into a local `data/` directory, named `user.<id>.<n>.jpg` |
| Detect Face | `face_recog.py` | Opens the webcam, detects faces with a Haar cascade, runs the trained LBPH recogniser, looks the ID up in MySQL for name and department, and draws the label on the frame |
| Attendance | `attendance.py` | A table view of attendance rows with Import CSV / Export CSV buttons (Tkinter `filedialog`) |
| Help | `help.py` | Support/contact form backed by MySQL |
| Train Face | `train.py` | Reads every image in `data/`, trains `cv2.face.LBPHFaceRecognizer_create()`, writes `classifier.xml` |
| Photos | — | `os.startfile("data")` — opens the dataset folder in the file manager |
| Developer | `developer.py` | An "about the developer" panel plus a complaints table |
| Exit | — | Confirm-and-quit |

**Attendance logic** (`face_recog.py`): the LBPH prediction distance is converted to a confidence
score with `confidence = int(100 * (1 - predict / 300))`, and a row is appended to `harold.csv` when
confidence is above 86. Below that the face is drawn as "Unknown Face". The CSV columns are
name, department, id, time, date, and the literal status `Present`.

## Tech stack

- Python 3, Tkinter (GUI), Pillow (image loading for the UI)
- OpenCV with `opencv-contrib` — **required**, because `cv2.face.LBPHFaceRecognizer_create()` lives
  in the contrib modules and is absent from the plain `opencv-python` wheel
- NumPy
- MySQL via `mysql-connector-python` (and `pymysql`, imported in `face_recog.py` but unused)

## Setup

**There is no `requirements.txt`.** From the imports:

```bash
python3 -m venv venv && source venv/bin/activate
pip install opencv-contrib-python numpy pillow mysql-connector-python pymysql
```

### 1. MySQL

You need a local MySQL server with a database named `facialrecognition` containing a `userdetails`
table (columns referenced in the code include `id`, `name`, `dep`, plus the rest of the enrolment
fields). **TODO: verify** — no schema file or `CREATE TABLE` statement is committed, so the table
definition has to be reconstructed from the `INSERT`/`SELECT` statements in `UserDetailsButton.py`.

Connection details are **hardcoded in five separate files** (`UserDetailsButton.py`,
`developer.py`, `face_recog.py`, `help.py`) as
`host="localhost", user="root", passwd=<hardcoded>, database="facialrecognition"`. You must edit
each one — see the security note below.

### 2. Run

```bash
python main.py
```

The app must be started from the repository root: `main.py`, `train.py` and `face_recog.py` all open
image and cascade files by **relative path** (`Christine1.jpg`, `haarcascade_frontalface_default.xml`,
`data`, `classifier.xml`), so any other working directory raises `FileNotFoundError`.

### 3. Enrol and train

The `data/` directory is **not committed** and does not exist in a fresh clone. `train.py` calls
`os.listdir("data")` unguarded, so **"Train Face" crashes until you have enrolled at least one
person** via User Details → Take Photo Sample.

A pre-trained `classifier.xml` (10 MB) *is* committed, so "Detect Face" may appear to work
immediately — but it was trained on the original author's dataset and its numeric IDs will not match
rows in your `userdetails` table.

## Platform note

`main.py` uses `os.startfile("data")` for the Photos button. **`os.startfile` is Windows-only**; on
Linux and macOS that button raises `AttributeError`. The rest of the app is cross-platform.


## Status

**Working prototype, Windows-oriented.** Last commit June 2024. The enrolment → train → recognise →
CSV loop is implemented. Hardcoded credentials, hardcoded relative paths, no schema file and no
`requirements.txt` make it awkward to set up from a clean machine.

## Licence

None. **TODO: add a LICENSE file** — without one, the default is "all rights reserved".

The bundled `haarcascade_frontalface_default.xml` and `lbpcascade_frontalface.xml` are OpenCV's own
cascade files and carry OpenCV's licence terms.
