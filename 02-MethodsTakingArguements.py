import time

class FileLogger:
    filename = "log.txt"

    def write_message(self,message):
        # This appends messages to log file
        line = "{} {}\n" .format(int(time.time()),message)
        with open(self.filename, "a") as outfile:
            outfile.write(line)


logger = FileLogger()
logger.write_message("Hello")