import capture
import brighten
import time
from sys import argv

capture_times = []
convert_times = []

def main():

  iterations = int(argv[1])
  cam = capture.init()
  sess, out, in_img = brighten.init()

  for i in range(iterations):
    name = "temp%02d.png" % i
    start = time.time()
    capture.take_photo(name, cam)
    stop = time.time()
    capture_times.append(stop-start)
    print("Capture:", stop-start)

    start = time.time()
    brighten.enhance(name, sess, out, in_img)
    stop = time.time()
    convert_times.append(stop-start)
    print("Convert:", stop-start)

  capture.close(cam)

  print("Capture Times:", sum(capture_times)/iterations)
  print("Convert Times:", sum(convert_times)/iterations)

if __name__ == "__main__":
  main()


