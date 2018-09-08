from goprocam import GoProCamera
from goprocam import constants

# (1) Creates an instance of GoPro connection
gopro = GoProCamera.GoPro()

# (2) Streams to udp port 10000
gopro.stream("udp://127.0.0.1:10000")
