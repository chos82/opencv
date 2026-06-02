from ccm import OCVDetector
import unittest

class TestCase(unittest.TestCase):
    __cap__ = OCVDetector()
    
    def setUp(self):
        if not self.__cap__.isOpened():
            print("Cannot open camera")
            exit()
        print('TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST')
            
    while True:
        # Capture frame-by-frame
        ret, __frame__ = __cap__.read()
        if(__frame__ is None):
            exit(-1)
                
                    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def frameRetrivable(self):
        self.assertTrue(self.__frame__ is not None)
        
        
        
    
    if __name__ == '__main__':
        unittest.main()

    