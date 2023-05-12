"""This module contains methods to get folders """
import os, shutil
from datetime import datetime


def get_datetime():
    """
        Get the actual date and time

        Returns
        -------
        str
            actual_datetime : returns a string with the actual date and time
    """
    now = datetime.now()

    actual_datetime = now.strftime("%I:%M %p %d/%m%/%Y")

    return actual_datetime

def screenshot_path(path, screenshot_name):
    """
        Get the path of the folder of the screenshots

        Returns
        -------
        str
            new_path : returns a string with the path of screenshots's folder
    """
    new_path = '{path}/{screenshot_name}_{datetime}.png'
    today_format = datetime.now().strftime("%m-%d-%Y_%H_%M_%S.%f")
    return new_path.format(path=path, screenshot_name=screenshot_name, datetime=today_format)


def remove_evidence(path, folder_name):
    """
        Remove all the evidence of the folder

        Arguments
        -------
        path: (str)
            Path of the folder of the screenshots are saved
    """
    files = []
    no_files = 0
    folder_path = f'{path}{folder_name}'.format(path=path,folder_name=folder_name)
    message = f'({no_files})'.format(no_files=str(len(files)))
    # for row,o,file_n in os.walk(folder_path):
    #     for file in file_n:
    #         if '.png' in file:
    #             files.append(os.path.join(row,file))
    # print(folder_path)
    # for file_n in files:
    #     os.remove(file_n)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    print(message + 'files deleted from evidence folder.')