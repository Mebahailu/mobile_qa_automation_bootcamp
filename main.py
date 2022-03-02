import pytest
import inspect
import logging
from appium.webdriver.webdriver import WebDriver



logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s : %(message)s')



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

    @pytest.mark.parametrize('os', [('android')])
    def test_01(self, os):
        Test01Android.main_os = os
        # assert self.current_called_process() == 'Andriod'
        # logging.info(f'{self.__class__.__name__}, {self.caller_name}')
        assert self.main_os == 'android'
        logging.info(
            f'{Test01Android.caller_name}, OS = {Test01Android.main_os}')

    @classmethod
    def setup_class(cls):
        tag = Test01Android()
        tag.current_called_process()
        logging.info(f'{cls.caller_name}')

    @classmethod
    def teardown_class(cls):
        tag = Test01Android()
        tag.current_called_process()
        logging.info(f'{cls.caller_name}')


    def setup_method(self):
        self.current_called_process()
        logging.info(f'{Test01Android.caller_name}')

    def teardown_method(self):
        self.current_called_process()
        logging.info(f'{Test01Android.caller_name}')

    @pytest.mark.xfail(reason='Unable to execute test')
    def test_02_xfail(self):
        assert self.current_called_process() == 'test_02_xfail'
        logging.info(f'{Test01Android.caller_name}')

    @pytest.mark.skip(reason='Unable to execute test')
    def test_03_skip(self):
        assert self.current_called_process() == 'test_03_skip'
        logging.info(f'{Test01Android.caller_name}')
