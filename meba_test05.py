import pytest
import inspect
import logging
from appium.webdriver.webdriver import WebDriver


# basic logger configrations
# log level is info

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s : %(message)s')


# just creating webdriver and initializing driver methods
class WebCommon(WebDriver):
    def __init__(self):
        super().__init__()


class Test01Android():
    caller_name = ''
    main_os = ''

    def current_called_process(self):
        all_stack_frames = inspect.stack()
        caller_stack_frame = all_stack_frames[1]
        Test01Android.caller_name = caller_stack_frame[3]

    def setup_method(self):
        self.current_called_process()
        logging.info(f'{Test01Android.caller_name}')

    def teardown_method(self):
        self.current_called_process()
        logging.info(f'{Test01Android.caller_name}')
