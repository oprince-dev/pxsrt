import subprocess
import os
import numpy as np
from PIL import Image  # type: ignore
from pxsrt import reader, args
from typing import Tuple


def generate_preview(data: np.ndarray,
                     thresh_data: np.ndarray) -> Tuple[np.ndarray, dict]:
    """Generate a preview of the pixels to be sorted.

    White -- Pixels to be sorted.
    Black -- Pixels that will be ignored.
    """
    sub_path = './pxsrt_previews/'
    if not os.path.exists(sub_path):
        os.makedirs(sub_path)

    while True:
        preview_img = Image.fromarray(thresh_data,
                                      mode='HSV').convert(mode='RGB')
        preview_img.save('./pxsrt_previews/preview.png')

        p = subprocess.Popen(['eog', './pxsrt_previews/preview.png'])

        choice = (input('Continue with this threshold map? Y/N: ')).lower()
        if choice == 'y':
            p.kill()
            break
        else:
            while True:
                try:
                    L_threshold = int(input(
                            'Enter a new lower boundary (0-255): '))
                    U_threshold = int(input(
                            'Enter a new upper boundary (0-255): '))
                    o = input('Target outer pixels? (Y/N): ')
                    outer = True if o.lower() == 'y' else False
                    mode = input('Mode (H, S, V, R, G, B): ')
                    p.kill()
                    thresh_data = reader.read_thresh(data,
                                                     outer=outer,
                                                     mode=mode,
                                                     L=L_threshold,
                                                     U=U_threshold)
                    break
                except ValueError as e:
                    print(f'{type(e).__name__}: '
                          f'Invalid number. '
                          f'Numbers must be within the range of 0 and 255')
                except Exception as e:
                    print(f'{type(e).__name__}: {e}')

    final_args = {
            'threshold': [L_threshold, U_threshold],
            'outer': outer,
            'mode': mode,
    }
    return thresh_data, final_args


def save_sort(output: Image, f_args: dict) -> None:
    """Save pixel sorted image ('./pxsrt_exports/')"""
    _args = args.parse_args()
    sub_path = './pxsrt_exports/'
    base, file_extension = os.path.splitext(
            os.path.basename(_args['input_image']))
    if not os.path.exists(sub_path):
        os.makedirs(sub_path)

    save_choice = (input('Would you like to save? Y/N: ')).lower()
    if save_choice == 'y':
        save_as_choice = (input('Save as (leave blank for auto renaming): '))
        print('Saving Image..')
        if save_as_choice == '':
            output_base = '{}_{}{}({}-{}){}{}'.format(base,
                                                      f_args['mode'],
                                                      _args['direction'],
                                                      f_args['threshold'][0],
                                                      f_args['threshold'][1],
                                                      f_args['outer'],
                                                      file_extension)

        else:
            output_base = save_as_choice

        output_path = ('/').join(_args['input_image'].split('/')[:-1])
        output_file = output_path + sub_path + output_base
        output.save(output_file)
