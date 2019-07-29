{% set app_class_name = cookiecutter.formal_name.title().replace(' ','').replace('-','').replace('!','').replace('.','').replace(',','') -%}
{% if cookiecutter.gui_framework == 'Toga' %}import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class {{ app_class_name }}(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box
        main_box = toga.Box()

        # Add the content on the main window
        self.main_window.content = main_box

        # Show the main window
        self.main_window.show()


def main():
    return {{ app_class_name }}('{{ cookiecutter.formal_name }}', '{{ cookiecutter.bundle }}.{{ cookiecutter.app_name }}')
% elif {cookiecutter.gui_framework == 'PySide2' %}

import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
count=1;
left_pupil_comp=0
right_pupil_comp=0

while True:

    _, frame = webcam.read()


    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Count: " + str(count), (90,200), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    left_pupil_x = gaze.pupil_left_xcoord()
    left_pupil_int = str(left_pupil_x)

    if left_pupil_int == "None":
        left_pupilx=0
    else:
        left_pupilx=int(left_pupil_int )

    left_pupil_comp += left_pupilx
    left_pupil_average = left_pupil_comp/count

    right_pupil_x=gaze.pupil_right_xcoord()
    right_pupil_int = str(right_pupil_x)

    if right_pupil_int == "None":
        right_pupilx = 0
    else:
        right_pupilx = int(right_pupil_int)

    right_pupil_comp += right_pupilx
    right_pupil_average = right_pupil_comp/count

    cv2.putText(frame, "Left Pupil Average: " + str(left_pupil_average), (90, 235), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right Pupil Average: " + str(right_pupil_average), (90, 270), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    count +=1;


    cv2.imshow("DemoPS", frame)

    if cv2.waitKey(1) == 27:
        break
