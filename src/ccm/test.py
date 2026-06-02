from ccm import OCVDetector as cvd
import unittest

import logging

#def __main__():
#    testCase = OCVDetectorTest()
#    testCase.__setUp__()
#    testCase.__testFrameRetrivable__()
#    testCase.__testUnwrapping__()


class OCVDetectorTest(unittest.TestCase):

        
    def __init__(self):
        # create logger with 'spam_application'
        logger = logging.getLogger('cam-cap-test')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('cam-cap-test.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - TEST - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        
        sep = '**************************************'
        logger.info(sep)
        logger.info('starting cam capture manipulator TESTS')
        logger.info(sep)
        
        self.Det = cvd.OCVDetector()
        self.frame = None        
    
    def __setUp__(self):
        if not self.__cap__.isOpened():
            print("Cannot open camera")
            exit()
        print('TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST')
            

            
    def retrieveFrame(self):
        while True:
            # Capture frame-by-frame
            self.frame = self.Det.run()
            if(self.frame is None):
                continue
            else:
                return self.frame
            
                    
    def __tearDown__(self):
        unittest.TestCase.tearDown(self)
    
    def __testFrameRetrivable__(self):
        self.retriveFrame()
        self.assertTrue(self.frame is not None)
        
    def __testUnwrapping__(self):
        self.retrieveFrame()
        boundingBox = self.Det.unwrap_numpy(self.frame)
        self.assertTrue(boundingBox is not None, 'a bounding box for the frame retrieved by test helper-method has been calculated')
        
 
#def __main__():
testCase = OCVDetectorTest()
testCase.__setUp__()
testCase.__testFrameRetrivable__()
testCase.__testUnwrapping__()
       
        
    
if __name__ == '__main__':
    unittest.main()

    