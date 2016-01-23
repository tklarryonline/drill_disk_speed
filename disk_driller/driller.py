import os
from time import time


class DiskDriller(object):
    # Default to be 1 MB, converted to Bytes
    # 1 MB = 1024 KB = 1024^2 Bytes = 2^20 Bytes
    DRILLER_FILE_SIZE = 10 ** 6
    DRILLER_FILE_NAME = 'driller_testing.txt'
    DRILLING_TIME_LIMIT = 5  # in seconds

    @staticmethod
    def write_drilling_file(file_name, file_size=DRILLER_FILE_SIZE):
        '''
        Write a text file which is of file_size MB big. Then remove it. Just to test.
        '''

        with open(file_name, 'wb') as f:
            f.write(os.urandom(file_size))

        os.remove(file_name)

        return True

    @classmethod
    def drill(cls, directory, file_size=DRILLER_FILE_SIZE):
        '''
        Perform drilling the input directory (if it is writable).

        Every drill is to write a file to the input directory.
        The bytes written will be divided by the time consumed to measure the velocity/speed.
        '''

        # Gets the file path
        file_name = os.path.join(directory, cls.DRILLER_FILE_NAME)

        start_time = time()
        loop_counter = 0

        while True:
            loop_counter += cls.write_drilling_file(file_name=file_name, file_size=file_size)
            consumed_time = time() - start_time

            if consumed_time > cls.DRILLING_TIME_LIMIT:
                break

        # At first, we need to convert file_size to MB
        file_size = file_size * 1.0 / cls.DRILLER_FILE_SIZE

        # Speed = MBs written / consumed time
        speed = (loop_counter * file_size) / consumed_time

        return speed


if __name__ == '__main__':
    dirname = os.getcwd()
    speed = DiskDriller.drill(dirname)

    print('Speed: {speed:.2f} MBs per second'.format(
        speed=speed
    ))
